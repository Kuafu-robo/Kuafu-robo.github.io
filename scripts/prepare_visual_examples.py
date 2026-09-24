#!/usr/bin/env python3
"""Prepare the author's video/model pairs for the static project website."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
IDS = ("0024", "0026", "0028", "0029")


def digest(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def probe(path):
    return json.loads(subprocess.check_output([
        "ffprobe", "-v", "error", "-select_streams", "v:0",
        "-show_entries", "stream=width,height,nb_frames,r_frame_rate,duration",
        "-of", "json", str(path),
    ], text=True))["streams"][0]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="Local kuafu_visual checkout")
    parser.add_argument("--refresh-models", action="store_true",
                        help="Replace verified model previews only, keeping existing input clips")
    args = parser.parse_args()
    source = args.source.resolve()
    output = ROOT / "assets" / "visual-models"
    previous = {}
    if args.refresh_models:
        previous_manifest = json.loads((output / "manifest.json").read_text())
        previous = {item["id"]: item for item in previous_manifest["examples"]}
        for key in IDS:
            for name, record in previous[key]["files"].items():
                assert digest(output / key / name) == record["sha256"], f"Locally modified file: {key}/{name}"
    elif output.exists():
        raise SystemExit("Output exists; use --refresh-models to replace verified previews only.")
    originals = json.loads((source / "video2assets/manifest.json").read_text())
    expected = {item["file"]: item["repository_sha256"] for item in originals["videos"]}
    selection = json.loads((source / "runs/selected_assets.json").read_text())
    selected = {item["id"]: item for item in selection["assets"]}
    previews = {}
    for key in IDS:
        clip = source / f"video2assets/IMG_{key}.mov"
        assert digest(clip) == expected[clip.name], f"Source video hash mismatch: {key}"
        if args.refresh_models:
            assert digest(clip) == previous[key]["source_sha256"], f"Input recording changed: {key}"
        turntable = source / "runs" / selected[key]["turntable"]
        previews[key] = turntable.parent
        report = json.loads((turntable.parent / "render.json").read_text())
        assert digest(source / "runs" / selected[key]["glb"]) == report["source_sha256"]
        for name in ("turntable.mp4", "poster.jpg"):
            assert digest(turntable.parent / name) == report["files_sha256"][name]
        info = probe(turntable)
        assert (info["width"], info["height"], info["nb_frames"], info["r_frame_rate"]) == (720, 720, "240", "30/1")
        assert abs(float(info["duration"]) - 8.0) < 0.001
        assert (source / f"runs/{key}/frames/frame_000.jpg").is_file()
    manifest = {
        "source_revision": subprocess.check_output(
            ["git", "-C", str(source), "rev-parse", "HEAD"], text=True
        ).strip(),
        "source_encoding": "H.264 CRF 23, 720x1280, full frame count and duration; AAC audio copied",
        "model_previews": "Unchanged supplied 720x720 H.264 turntables of the selected robust multi-view, lighting-corrected GLBs",
        "selection_manifest": "runs/selected_assets.json",
        "texture_fusion": selection["default_texture_fusion"],
        "lighting_correction": selection["lighting_correction"],
        "examples": [],
    }
    for key in IDS:
        folder = output / key
        folder.mkdir(parents=True, exist_ok=args.refresh_models)
        clip = source / f"video2assets/IMG_{key}.mov"
        if not args.refresh_models:
            subprocess.run([
                "ffmpeg", "-hide_banner", "-loglevel", "error", "-nostdin", "-n",
                "-i", str(clip), "-map", "0:v:0", "-map", "0:a:0?",
                "-vf", "scale=720:-2", "-c:v", "libx264", "-preset", "medium",
                "-crf", "23", "-threads", "2", "-pix_fmt", "yuv420p",
                "-c:a", "copy", "-map_metadata", "-1", "-movflags", "+faststart",
                str(folder / "input.mp4"),
            ], check=True)
        before, after = probe(clip), probe(folder / "input.mp4")
        assert before["nb_frames"] == after["nb_frames"]
        assert before["r_frame_rate"] == after["r_frame_rate"]
        assert abs(float(before["duration"]) - float(after["duration"])) < 0.001
        if not args.refresh_models:
            shutil.copy2(source / f"runs/{key}/frames/frame_000.jpg", folder / "input.jpg")
        shutil.copy2(previews[key] / "turntable.mp4", folder / "model.mp4")
        shutil.copy2(previews[key] / "poster.jpg", folder / "model.jpg")
        manifest["examples"].append({
            "id": key, "source_sha256": digest(clip), "video": after,
            "model_source": selected[key]["glb"],
            "preview_source": selected[key]["turntable"],
            "registered_views": selected[key]["registered_views"],
            "files": {p.name: {"sha256": digest(p), "bytes": p.stat().st_size}
                      for p in sorted(folder.iterdir())},
        })
        print(f"Prepared {key}: {after['nb_frames']} input frames; unchanged model preview.", flush=True)
    (output / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")


if __name__ == "__main__":
    main()

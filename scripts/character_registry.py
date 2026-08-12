#!/usr/bin/env python3
"""Register and select persistent character references for dylan-cover-generator."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHARACTERS_DIR = ROOT / "assets" / "characters"
REGISTRY_PATH = CHARACTERS_DIR / "registry.json"
ID_RE = re.compile(r"^[a-z0-9][a-z0-9_-]{0,63}$")


def load_registry() -> dict:
    if not REGISTRY_PATH.exists():
        return {"version": 1, "default_character": None, "characters": []}
    with REGISTRY_PATH.open(encoding="utf-8") as handle:
        data = json.load(handle)
    data.setdefault("version", 1)
    data.setdefault("default_character", None)
    data.setdefault("characters", [])
    return data


def save_registry(data: dict) -> None:
    CHARACTERS_DIR.mkdir(parents=True, exist_ok=True)
    tmp = REGISTRY_PATH.with_suffix(".json.tmp")
    with tmp.open("w", encoding="utf-8") as handle:
        json.dump(data, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    tmp.replace(REGISTRY_PATH)


def require_id(value: str) -> str:
    if not ID_RE.fullmatch(value):
        raise SystemExit("id must use lowercase letters, digits, hyphens, or underscores")
    return value


def add_character(args: argparse.Namespace) -> None:
    character_id = require_id(args.id)
    source = Path(args.image).expanduser().resolve()
    if not source.is_file():
        raise SystemExit(f"image not found: {source}")

    data = load_registry()
    existing = next((item for item in data["characters"] if item["id"] == character_id), None)
    if existing and not args.replace:
        raise SystemExit(f"character already exists: {character_id}; pass --replace to update it")

    target_dir = CHARACTERS_DIR / character_id
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / f"reference{source.suffix.lower() or '.jpg'}"
    shutil.copy2(source, target)
    profile = {
        "id": character_id,
        "name": args.name or character_id,
        "aliases": args.alias or [],
        "reference": str(target.relative_to(ROOT)),
        "notes": args.notes or "",
        "updated_at": datetime.now(timezone.utc).isoformat(),
    }
    profile_path = target_dir / "profile.json"
    with profile_path.open("w", encoding="utf-8") as handle:
        json.dump(profile, handle, ensure_ascii=False, indent=2)
        handle.write("\n")

    data["characters"] = [item for item in data["characters"] if item["id"] != character_id]
    data["characters"].append(profile)
    if args.set_default or data.get("default_character") is None:
        data["default_character"] = character_id
    save_registry(data)
    print(f"registered {character_id}: {target}")
    print(f"default character: {data['default_character']}")


def list_characters(_: argparse.Namespace) -> None:
    data = load_registry()
    print(f"default: {data.get('default_character') or '(none)'}")
    for item in data["characters"]:
        print(f"- {item['id']}: {item.get('name', item['id'])} -> {item['reference']}")


def use_character(args: argparse.Namespace) -> None:
    character_id = require_id(args.id)
    data = load_registry()
    if not any(item["id"] == character_id for item in data["characters"]):
        raise SystemExit(f"character not found: {character_id}")
    data["default_character"] = character_id
    save_registry(data)
    print(f"default character: {character_id}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)

    add = commands.add_parser("add", help="copy an image into a persistent profile")
    add.add_argument("--id", required=True)
    add.add_argument("--image", required=True)
    add.add_argument("--name")
    add.add_argument("--alias", action="append")
    add.add_argument("--notes")
    add.add_argument("--set-default", action="store_true")
    add.add_argument("--replace", action="store_true")
    add.set_defaults(func=add_character)

    show = commands.add_parser("list", help="list profiles and the default")
    show.set_defaults(func=list_characters)

    use = commands.add_parser("use", help="select an existing profile as default")
    use.add_argument("id")
    use.set_defaults(func=use_character)
    return parser


if __name__ == "__main__":
    try:
        parsed = build_parser().parse_args()
        parsed.func(parsed)
    except BrokenPipeError:
        sys.exit(0)

#!/usr/bin/env python3
"""Print the PDF title from info.yaml for use by gendoc/pandoc."""
import yaml
import argparse
import os

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--info", default="info.yaml", help="Path to info.yaml")
    args = p.parse_args()
    if not os.path.exists(args.info):
        print("Documentation", end="")
        return
    try:
        with open(args.info) as f:
            d = yaml.safe_load(f) or {}
        title = d.get("title")
        if title is None and isinstance(d.get("doc"), dict):
            doc = d["doc"]
            title = doc.get("title")
            if title is None and isinstance(doc.get("libraries"), dict):
                libs = list(doc["libraries"].keys())
                if libs:
                    title = libs[0]
        if title is None:
            title = d.get("library")
        title = title or "Documentation"
        # Escape underscores for LaTeX so \title{...} does not trigger math mode
        title = title.replace("_", r"\_")
        print(title, end="")
    except Exception:
        print("Documentation", end="")

if __name__ == "__main__":
    main()

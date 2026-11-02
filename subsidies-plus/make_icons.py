"""Builds icons.js for the docs page: the subsidy icons of the mod as white PNG data URIs, keyed by type folder.

The mod's icons (<type>/<type>_32@2x.tga) are single-channel masks the game tints; here they become white glyphs on
transparent ground, drawn on the purple tile of the page.

Usage: python make_icons.py <mod content/subventions folder> <output icons.js>
Requires Pillow.
"""
import base64
import io
import json
import sys
from pathlib import Path

from PIL import Image


def main():
    folder, out = Path(sys.argv[1]), Path(sys.argv[2])
    icons = {}
    for tga in sorted(folder.glob("*/*_32@2x.tga")):
        mask = Image.open(tga).convert("L")
        image = Image.new("RGBA", mask.size, (255, 255, 255, 0))
        image.putalpha(mask)
        buffer = io.BytesIO()
        image.save(buffer, "PNG", optimize=True)
        icons[tga.parent.name] = "data:image/png;base64," + base64.b64encode(buffer.getvalue()).decode()
    out.write_text("const ICONS = " + json.dumps(icons, indent=0) + ";\n", encoding="utf-8")
    print(f"{len(icons)} icons -> {out}")


if __name__ == "__main__":
    main()

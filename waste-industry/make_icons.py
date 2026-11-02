"""Builds icons.js for the Waste Industry guide: the mod's cargo icons and build-menu pictures as data URIs.

Cargo icons (content/cargos/<cargo>/<cargo>@2x.tga, 48 px) become PNG, keyed "cargo:<cargo>". Build-menu pictures
of industries and street bins (<folder>/<folder>@2x.tga, 240 x 150) become WebP to keep the page small, keyed
"build:<folder>". The Waste menu category icon (content/menu/category_waste@2x.tga, a white mask) becomes the
page's logo, "mark", and its browser tab icon on a dark tile, "favicon".

Usage: python make_icons.py <mod content folder> <output icons.js>
Requires Pillow.
"""
import base64
import io
import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw


def data_uri(image, fmt, **options):
    buffer = io.BytesIO()
    image.save(buffer, fmt, **options)
    return f"data:image/{fmt.lower()};base64," + base64.b64encode(buffer.getvalue()).decode()


def main():
    content, out = Path(sys.argv[1]), Path(sys.argv[2])
    icons = {}
    for tga in sorted((content / "cargos").glob("*/*@2x.tga")):
        if tga.parent.name != "classes":
            icons["cargo:" + tga.parent.name] = data_uri(Image.open(tga).convert("RGBA"), "PNG", optimize=True)
    for folder in ("industries", "stations/street"):
        for tga in sorted((content / folder).glob("*/*@2x.tga")):
            if tga.stem == tga.parent.name + "@2x":
                image = Image.open(tga).convert("RGBA")
                icons["build:" + tga.parent.name] = data_uri(image, "WEBP", quality=82, method=6)
    mask = Image.open(content / "menu" / "category_waste@2x.tga").convert("L")
    mark = Image.new("RGBA", mask.size, (255, 255, 255, 0))
    mark.putalpha(mask)
    icons["mark"] = data_uri(mark, "PNG", optimize=True)
    favicon = Image.new("RGBA", (64, 64), (0, 0, 0, 0))
    ImageDraw.Draw(favicon).rounded_rectangle((0, 0, 63, 63), radius=12, fill=(43, 48, 56, 255))
    favicon.alpha_composite(mark.resize((48, 48), Image.LANCZOS), (8, 8))
    icons["favicon"] = data_uri(favicon, "PNG", optimize=True)
    out.write_text("const ICONS = " + json.dumps(icons, indent=0) + ";\n", encoding="utf-8", newline="\n")
    print(f"{len(icons)} icons, {out.stat().st_size // 1024} KB -> {out}")


if __name__ == "__main__":
    main()

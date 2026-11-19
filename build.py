"""Builds every page of the site from its template.html.

A page is the site root or a folder with a template.html. The template may contain these markers:
  /*SITE_CSS*/   replaced by shared/site.css (the common look)
  <!--SITE_NAV-->  replaced by the navigation between the mod pages, with the current page marked
  /*ICONS*/      replaced by the page's icons.js (made by make_icons.py)
  <!--CHANGELOG-->  replaced by the page's CHANGELOG.md as a list of versions, newest open; the copy is refreshed from
                 the mod's CHANGELOG.md when the mod folder lies next to this repository (MOD_PAGES), and the
                 "Unreleased" section is left out until it gets its version number
Each page gets an index.html next to its template, the file GitHub Pages serves.

With --fragment DIR every page is also written to DIR/<page>.html without the document skeleton, as a Claude
artifact publishes it (the artifact adds doctype, head and body itself). Links between pages do not work there.

Usage: python build.py [--fragment DIR]
"""
import html
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
# Folder, nav label and mod folder (next to this repository, for its CHANGELOG.md) of every mod page, in nav order.
# The root page is the overview of all mods.
MOD_PAGES = [
    ("subsidies-plus", "Subsidies+", "darthbane426_subsidies_plus"),
    ("waste-industry", "Waste Industry", "darthbane426_waste_industry"),
]


def make_nav(current):
    prefix = "./" if current == "" else "../"

    def current_attr(folder):
        return ' aria-current="page"' if folder == current else ""

    links = [f'<a class="home" href="{prefix}"{current_attr("")}>Transport Fever 3 Mods</a>']
    for folder, label, _ in MOD_PAGES:
        if (HERE / folder / "template.html").exists():
            links.append(f'<a href="{prefix}{folder}/"{current_attr(folder)}>{label}</a>')
    return '<nav class="site-nav" aria-label="Mods"><div class="wrap">' + "".join(links) + "</div></nav>"


def replace_once(text, marker, value, page):
    count = text.count(marker)
    if count > 1:
        sys.exit(f"{page}/template.html has {marker} {count} times")
    return text.replace(marker, value)


def render_changelog(page_dir, mod_folder, page):
    """The <section> of the changelog from page_dir/CHANGELOG.md, refreshed from the mod's copy first."""
    source = HERE.parent / mod_folder / "CHANGELOG.md" if mod_folder else None
    target = page_dir / "CHANGELOG.md"
    if source and source.exists():
        # the public copy without the "Unreleased" section
        text = source.read_text(encoding="utf-8")
        text = re.sub(r"(?ms)^## Unreleased$.*?(?=^## )", "", text)
        target.write_text(text, encoding="utf-8", newline="\n")
    if not target.exists():
        sys.exit(f"{page}/template.html uses <!--CHANGELOG--> but {target} is missing")
    versions, current, group = [], None, None
    for line in target.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            current = {"name": line[3:].strip(), "groups": []}
            group = None
            versions.append(current)
        elif current and line.startswith("### "):
            group = {"title": line[4:].strip(), "items": []}
            current["groups"].append(group)
        elif current and line.startswith("- "):
            if group is None:
                group = {"title": "", "items": []}
                current["groups"].append(group)
            group["items"].append(line[2:].strip())
    parts = []
    for version in versions:
        if version["name"].lower() == "unreleased":
            continue
        body = []
        for group in version["groups"]:
            title = f'<h4>{html.escape(group["title"])}</h4>' if group["title"] else ""
            items = "".join(f"<li>{html.escape(item)}</li>" for item in group["items"])
            body.append(f"{title}<ul>{items}</ul>")
        state = " open" if not parts else ""
        anchor = "v" + re.sub(r"[^0-9a-z]+", "-", version["name"].lower()).strip("-")
        parts.append(f'<details id="{anchor}"{state}><summary>{html.escape(version["name"])}</summary>{"".join(body)}</details>')
    return '<section class="wrap changelog" id="changelog"><h2>Changelog</h2>' + "".join(parts) + "</section>"


def build(folder, site_css, fragment_dir, mod_folder=None):
    page_dir = HERE / folder
    page = folder or "root"
    fragment = (page_dir / "template.html").read_text(encoding="utf-8")
    fragment = replace_once(fragment, "/*SITE_CSS*/", site_css, page)
    fragment = replace_once(fragment, "<!--SITE_NAV-->", make_nav(folder), page)
    if "/*ICONS*/" in fragment:
        icons = page_dir / "icons.js"
        if not icons.exists():
            sys.exit(f"{page}/template.html uses /*ICONS*/ but {icons} is missing; run make_icons.py")
        fragment = replace_once(fragment, "/*ICONS*/", icons.read_text(encoding="utf-8").strip(), page)
    if "<!--CHANGELOG-->" in fragment:
        fragment = replace_once(fragment, "<!--CHANGELOG-->", render_changelog(page_dir, mod_folder, page), page)

    # Everything up to the end of the first style block goes into <head>, the rest into <body>.
    split = fragment.index("</style>") + len("</style>")
    head, body = fragment[:split], fragment[split:]
    html = (
        "<!doctype html>\n<html lang=\"en\">\n<head>\n"
        "<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n"
        "<style>body { margin: 0; } [hidden] { display: none !important; }</style>\n"
        f"{head}\n</head>\n<body>\n{body}\n</body>\n</html>\n"
    )
    (page_dir / "index.html").write_text(html, encoding="utf-8", newline="\n")
    print(f"{folder or '.'}/index.html", len(html))

    if fragment_dir:
        out = fragment_dir / f"{folder or 'home'}.html"
        out.write_text(fragment, encoding="utf-8", newline="\n")
        print(out, len(fragment))


def main():
    fragment_dir = None
    if "--fragment" in sys.argv:
        fragment_dir = Path(sys.argv[sys.argv.index("--fragment") + 1])
        fragment_dir.mkdir(parents=True, exist_ok=True)
    site_css = (HERE / "shared" / "site.css").read_text(encoding="utf-8").strip()
    for folder, mod_folder in [("", None)] + [(f, m) for f, _, m in MOD_PAGES]:
        if (HERE / folder / "template.html").exists():
            build(folder, site_css, fragment_dir, mod_folder)


if __name__ == "__main__":
    main()

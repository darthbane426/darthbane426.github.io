"""Builds every page of the site from its template.html.

A page is the site root or a folder with a template.html. The template may contain these markers:
  /*SITE_CSS*/   replaced by shared/site.css (the common look)
  <!--SITE_NAV-->  replaced by the navigation between the mod pages, with the current page marked
  /*ICONS*/      replaced by the page's icons.js (made by make_icons.py)
Each page gets an index.html next to its template, the file GitHub Pages serves.

With --fragment DIR every page is also written to DIR/<page>.html without the document skeleton, as a Claude
artifact publishes it (the artifact adds doctype, head and body itself). Links between pages do not work there.

Usage: python build.py [--fragment DIR]
"""
import sys
from pathlib import Path

HERE = Path(__file__).parent
# Folder and nav label of every mod page, in nav order. The root page is the overview of all mods.
MOD_PAGES = [
    ("subsidies-plus", "Subsidies+"),
    ("waste-industry", "Waste Industry"),
]


def make_nav(current):
    prefix = "./" if current == "" else "../"

    def current_attr(folder):
        return ' aria-current="page"' if folder == current else ""

    links = [f'<a class="home" href="{prefix}"{current_attr("")}>darthbane426 · TF3 mods</a>']
    for folder, label in MOD_PAGES:
        if (HERE / folder / "template.html").exists():
            links.append(f'<a href="{prefix}{folder}/"{current_attr(folder)}>{label}</a>')
    return '<nav class="site-nav" aria-label="Mods"><div class="wrap">' + "".join(links) + "</div></nav>"


def replace_once(text, marker, value, page):
    count = text.count(marker)
    if count > 1:
        sys.exit(f"{page}/template.html has {marker} {count} times")
    return text.replace(marker, value)


def build(folder, site_css, fragment_dir):
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
    for folder in [""] + [f for f, _ in MOD_PAGES]:
        if (HERE / folder / "template.html").exists():
            build(folder, site_css, fragment_dir)


if __name__ == "__main__":
    main()

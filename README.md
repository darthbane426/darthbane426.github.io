# darthbane426 TF3 mod guides

Player guides for the Transport Fever 3 mods by darthbane426, served by GitHub Pages at
https://darthbane426.github.io/.

| Folder | Page |
|---|---|
| `/` | overview of the mods |
| `subsidies-plus/` | Subsidies+ |
| `waste-industry/` | Waste Industry |

## Build

```
python build.py
```

Every page is a `template.html` in its folder. `build.py` puts in the shared look (`shared/site.css`), the
navigation between the pages and the page's icons, and writes the `index.html` next to it. Commit the built
`index.html` files too: GitHub Pages serves them as they are.

`python build.py --fragment DIR` also writes each page without the document skeleton, for a Claude artifact.

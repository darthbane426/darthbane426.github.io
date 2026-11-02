# Subsidies+ Docs

Player guide for the Transport Fever 3 mod Subsidies+: when each subsidy is offered, what it asks for, and what you
get or lose, recalculated for the difficulty and game year you pick.

## Build

```
python make_icons.py <path to darthbane426_subsidies_plus/content/subventions> icons.js
python ../build.py
```

`template.html` is the source. The site's `build.py` (one folder up) puts in the shared look, the navigation and the
icons, and writes `index.html`, the page GitHub Pages serves. Run `make_icons.py` again only when the mod's icons
change (needs Pillow).

The amounts follow the mod's constants, which are written into the `MOD` object and the rules in `template.html`.
When the mod's numbers change, update them there and rebuild.

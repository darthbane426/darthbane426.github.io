# Subsidies+ changelog

The full changelog, shown on https://darthbane426.github.io/subsidies-plus/#changelog (the site's build.py copies this
file; the "Unreleased" section stays off the page until it gets its version number). The mod.io changelog is short:
the new subsidies, then "Tweaks and bug fixes" with a link to the page.

## 1.3.1
### Fixes
- Workers' Settlement: the new town is founded big enough for its industries, and the workers it has to send follow its size: at most half of its residents in all, shared by the industries and fixed once the town has residents. Running contracts get their numbers on the next check.
- Workers' Settlement: the money follows the number of industries: a group of 2 pays 20 % less than one of 3, a group of 4 20 % more; the fine follows it (new offers).
- Transfer Hub: the transfers it asks for follow the smallest of the towns whose passengers change at the hub (the towns it already reaches, then the nearest), not the hub town; the number is fixed with the offer (new offers).
- World Exposition: the visitors it asks for follow the residents of the 6 towns nearest the host, where they come from. The exposition opens 6 months after you accept and then runs for one year; the marketing campaign starts on acceptance (new offers).
- Railway Settlement: the train passengers it asks for follow the smaller of the two towns, the same number for each town (new offers).
- Tram Network and New Market: the fine is at most three quarters of the money reward; Tram Network with income only has half the former fine (new offers).
- Regional Network: the time follows the number of towns, 30 to 42 months for 3 towns and 42 to 54 for 4; a network of 4 towns pays a quarter more money (new offers).
- Regional Network: each town pair shows in its bar whether it is connected, instead of a list in the text, so the whole window fits again.
- Subsidy windows with progress bars scroll when they are taller than the screen, instead of squeezing the window and drawing the time bar upside down.

## 1.3.0
### New subsidies
- Island Settlement: a new mostly residential settlement on an empty island; ten years to grow into a Large Hamlet.
- Mountain Settlement: a new mining settlement high in the mountains with a mine nearby (50 % chance of a second one if there is room); seven years to grow into a Hamlet.
- Fishing Settlement: a new settlement on the coast by fishing grounds nobody serves; it buys fish from the start. Ten years to grow into a Large Hamlet.
- Farm Settlement: a new farming settlement with a crop farm nearby and a second farm if there is room; it buys vegetables from the start. Seven years to grow into a Large Hamlet.
- Railway Settlement: a new town halfway along your train line between two towns; help it grow into a Hamlet in five years and carry passengers by train between it and each town.

### Settlements
- Settlements no longer come in the normal subsidy rounds: one shared timer offers one at a time, every 36, 24, 12 or 6 months by the game's subsidy setting (×1.5 on Rare, ×⅔ on Often). A site comes back after 60 months at the earliest.
- New setting "Settlement subsidies": Off switches every settlement type off, whatever their own switches say.
- A settlement offer puts a survey tripod with a flag on the spot of the new town; the offer shows in the top bar and takes the camera there.
- Workers' Settlement: the offer shows arrows from the site of the new town to the industries its residents will work at.
- Workers' Settlement: the new town is named after its industries' town, such as "New Goldville".
- Workers' Settlement: 30 to 45 months to fulfil instead of 24 to 36. Half again as much money, a third of it upfront, and a fine of three quarters of the reward instead of over three times it. 20 to 40 % reputation in the new town when fulfilled; on failure it takes 50 to 100 % there and nothing in the nearest town (new offers).
- Workers' Settlement: a new icon (houses with a plus), shared with the new settlements.

### Other changes
- Subsidies+ types come up a bit more often on every frequency setting.
- Tram Network: no more reward of money alone. It is either double income on tram rides within the town for five years, or about a third of the former money with double income for two years.
- Regional Network pays 50 % more money (upfront and on completion); its fine stays the same.
- Rail Connection: only between towns of at least 200 residents each.
- Non-stop Express: the offer tells how many passengers the express has to carry.
- Industry Expansion: the task shows a workers icon next to the boosters when the industry needs workers.
- New Market: when several industries make the good, the offer names the one nearest the town.
- The game log (stdout.txt) gets a monthly line on why each type was or was not offered, and timing lines to trace lag.

### Fixes
- Workers' Settlement: an error of the game while the town is founded no longer stops all subsidies; the subsidy ends without a fine and the upfront money goes back.
- Industry Expansion: offered only when every booster cargo the industry needs has an industry on the map that can make it, whether it runs or not.
- Rail Connection and Highway Concession: a contract left with the same town twice ends without a fine, as the Non-stop Express does.
- Non-stop Express and Highway Concession: the warning about a broken express or highway also closes when it came up after the game was loaded.

## 1.2.2
- Non-stop Express, Rail Connection, Highway Concession: a contract that ended up with the same town twice is now repaired back to its two towns instead of being ended; also contracts from saves already affected.

## 1.2.1
- Fixed a crash when opening a Non-stop Express subsidy that showed the same town twice; such a contract now ends without a fine.

## 1.2.0
- Larger subsidy types now unlock with your company rank: most from Mechanic, the biggest ones (Workers' Settlement, World Exposition, Non-stop Express, Highway Concession) from Coordinator. New companies get more of the game's easier subsidies.
- Delivery contracts no longer stop counting after an invalid delivery event.
- Income bonuses of several subsidies no longer cancel each other out.
- New Market: in a small town whose district asks for nothing yet, the delivery target now follows the town's size.
- Eco Contract: now offered only near towns whose pollution really reaches 65 dB; before, almost every town qualified.
- Highway Concession: a finished highway is no longer missed when two exits lead into the same access road.
- Industry Partnership: two partnerships with the same factory each keep their perk; the first one ending no longer takes the second one's perk.
- Industry Partnership, Eco Contract, Industry Expansion: the game no longer closes the contract's factory while the contract runs.
- Industry Partnership, Eco Contract, Industry Expansion: accepting one at some factories no longer crashes the game.

## 1.1.1
- New Market: no longer offered for a district that already asks for three kinds of goods.

## 1.1
- New subsidy: Non-stop Express, a train with stops only in two distant towns.
- New subsidy: Highway Concession, a highway between two distant towns, paid monthly for 12 years.
- New subsidy: Industry Partnership, an unserved factory pays with better vehicles.
- New docs page with the full rules of every subsidy.
- Investment Contract: goods from the new factory now count (they did not count at all before).
- Eco Contract: goods carried through a warehouse count once.
- Targets now follow what the factory can make and what the town takes in; rewards and fines grow with the target.
- Prospecting Contract pays less, as it is the easier job.
- Regional Network: every pair of towns has its own goal and progress bar; part of the money comes on acceptance.
- Workers' Settlement: part of the money comes on acceptance.
- New Market: only one per town at a time.
- Subsidies now show at the industry window and on the map for Eco Contract, Industry Partnership and Industry Expansion.
- Passenger subsidies show their target in the task row.
- Shorter offer texts.

## 1.0
- First beta release.

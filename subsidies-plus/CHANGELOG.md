# Subsidies+ changelog

The full changelog, shown on https://darthbane426.github.io/subsidies-plus/#changelog (the site's build.py copies this
file; the "Unreleased" section stays off the page until it gets its version number). The mod.io changelog is short:
the new subsidies, then "Tweaks and bug fixes" with a link to the page.

## 1.3.0
### New subsidies
- Island Settlement: a new mostly residential settlement on an empty island; help it grow into a Large Hamlet.
- Mountain Settlement: a new mining settlement high in the mountains with a mine nearby (half of them get a second mine if there is room); help it grow into a Hamlet.
- Fishing Settlement: a new settlement on the coast by fishing grounds nobody serves; it buys fish from the start.
- Farm Settlement: a new farming settlement on open plains far from towns with two farms nearby, a crop farm and a second farm of any kind the economy has; it buys vegetables from the start. Seven years to grow into a Large Hamlet.
- Railway Settlement: two towns of at least 350 residents, 7 km or more apart and served by one passenger train line, get a new town beside their railway roughly halfway between them, 150 to 300 m from the track and away from railway bridges and tunnels. Help it grow into a Hamlet in five years and carry passengers by train between it and each of the two towns; a train that runs through it from one town to the other counts for both. When one of the two towns disappears, the subsidy ends without a fine and the upfront money stays.

### Settlements
- A settlement offer puts a survey tripod with a flag on the spot of the new town; the offer shows in the top bar and takes the camera there. The tripod goes when the offer is accepted, declined or ends.
- Workers' Settlement: the offer already shows arrows from the site of the new town to the industries its residents will work at.
- Island, Mountain, Fishing, Farm and Railway Settlement take their names from the map's town-name list, also one from another mod: a name that fits (a harbour town for fishing), one made to fit, such as "Insel Kyritz" or "Port Reading", or another unused name of the list.
- Workers' Settlement: the new town is called after the town its industries are named after, such as "New Goldville"; "Goldville Settlement" if that town's name already starts with "New" or a "New Goldville" exists.
- Island, Mountain, Fishing, Farm and Railway Settlement found the town only on the site with the flag. When that site is blocked (or the first mine or farm does not fit there, or the game reports an error while founding the town), the subsidy ends without a fine, its message says so, and the next site of the offer comes as a new offer with its own flag, to accept again.
- Farm Settlement keeps the town 800 m and the farms 700 m from every industry; Mountain Settlement keeps the town 800 m and the mines 500 m from every industry.
- The settlements no longer come in the normal subsidy rounds. One shared timer offers one settlement at a time, the type offered least so far first: every 36, 24, 12 or 6 months of game time by the game's subsidy setting (none when the game's subsidies are off), 1.5 times as long on Rare and two thirds on Often. The calendar speed and the company rank do not change it; the settlements still come only from the company rank they need. When no type finds a place, the timer tries again after 1, 2, 4, 8 and 16 months, then at its normal interval; it rests while the game's subsidies are paused and in the map editor. A site offered before (for a Workers' Settlement its group of industries) comes back 60 months of game time later at the earliest, whatever the calendar speed.
- New setting "Settlement subsidies": Off switches every settlement type off, whatever their own switches say.
- Island and Fishing Settlement: ten years to grow into a Large Hamlet.
- The money of the settlements follows how hard they are: Mountain and Island 60 to 140 steps of 75 000 (before inflation), Railway, Fishing and Workers' Settlement a quarter less, Farm 40 % less. A third of it comes on acceptance, for the road or line to the new town. On failure it goes back and the fine is three quarters of the whole reward, as the town stays either way. When no site takes the town, only the upfront money goes back.
- Mountain Settlement: seven years to grow into a Hamlet, as a mountain top has no room for more.
- Mountain Settlement: the mine goes only on fairly flat ground, so it does not cut a high wall into the mountain, and on the highest such ground within reach, so it stands up in the mountains by the town rather than down in the valley.
- Mountain and Farm Settlement: the mines and farms start with a few fields and grow like the game's own industries, instead of standing fully expanded from the start.
- Workers' Settlement: 30 to 45 months to fulfil instead of 24 to 36, and the money of the other settlements: 45 to 105 steps instead of 30 to 70, a third upfront, the fine three quarters of the reward instead of 120 to 240 steps; on failure it takes reputation only in the new town (new offers).
- A founded settlement gives 20 to 40 % reputation in the new town when the subsidy is fulfilled and takes 50 to 100 % there when it fails.
- The settlement subsidies share one new icon (houses with a plus, the type below); Workers' Settlement gets it too.

### Other changes
- Subsidies+ types come up a bit more often on every frequency setting.
- Tram Network: no more reward of money alone. It is either double income on tram rides within the town for five years, or about a third of the former money with double income for two years.
- Regional Network pays 50 % more money (upfront and on completion); its fine stays the same.
- Rail Connection: only between towns of at least 200 residents each.
- Non-stop Express: the offer tells how many passengers the express has to carry.
- Industry Expansion: the task shows a workers icon next to the boosters when the industry needs workers.
- New Market: when several industries make the good, the offer names the one nearest the town.
- The game log (stdout.txt) gets a monthly line on why each type was or was not offered, and about once a minute the time the game's subsidy handling takes, to trace lag.

### Fixes
- Workers' Settlement: an error of the game while the town is founded no longer stops all subsidies; the subsidy ends without a fine and the upfront money goes back.
- Industry Expansion: offered only when every booster cargo the industry needs (tools, machines and the like) has an industry on the map that can make it, whether it runs or not; the mod builds no producer.
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

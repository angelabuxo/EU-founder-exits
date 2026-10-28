# What do European founders actually take home?

**In one sentence:** using public company registers in several European countries, we measure what startup founders end up with, and compare those who took venture capital with those who financed their company another way.

## Why it matters

- The only large founder-payoff study, Azevedo et al. (NBER w34512, 2026), is American: 88% of VC-backed founders exit with nothing, and the top 1% capture 79% of the value.
- On 23 October, a search found no study that measures founder payoffs for any European country.
- European VC-backed companies exit less often than American ones: IPO 6.2% against 13.1%, trade sale 34% against 44% (Axelson & Martinovic). Whether European founders still do better without VC is unknown.
- Nobody has compared VC-backed and self-funded founders in the same population, in any country.

## In this repo

- [`data/founder_sources.tsv`](data/founder_sources.tsv): the **source catalogue**. Every register, funding database, news archive, benchmark paper and platform considered. For each: what it gives the question, and whether its terms allow collection (usable, official route only, prohibited, or cite only).
- [`docs/sources.md`](docs/sources.md): the same catalogue as prose, with the quoted licence or prohibition for each source.
- [`docs/references-founder-payoffs.md`](docs/references-founder-payoffs.md): benchmark papers and reports, with the figures each reports.
- [`docs/design.md`](docs/design.md): which countries' registers show both owners and accounts, plus measures, checks and timeline.
- [`scripts/europe_registers.py`](scripts/europe_registers.py): the probe that tested the registers.

## Collection rules

We collect only through official APIs, bulk downloads, or the JSON endpoints a public page itself uses, and only where the terms do not prohibit it. Collection is gentle and recorded with its date. Sources whose terms forbid automated collection are listed as excluded and not used. Register data about named people is reported only in aggregate.

DTU 02805 Social Graphs and Interactions, autumn 2026. Log-Log Legends: Àngela Buxó, Gyula Kürthy, Niklas Johansen. Course group repo: https://github.com/horrrt/02805_social_graphs

# Study design: what do European founders take home? (28 October 2026)

**One sentence.** In the European countries whose registers show both who owns a company and its accounts, do founders who took venture capital end up with more or less than founders who stayed self-funded, five years after founding and at exit, and is the answer the same in every country?

**Why it is new.** A literature search on 28 October found no study that measures founder payoffs across European countries; none was found for single European countries either.
- The Norwegian register work (Alstadsæter et al.; van Praag & Raknerud) measures income or returns to entrepreneurship from restricted tax data, with no VC split.
- Montanaro et al. (Emerald) relate retained stake to exit value for 107 EU VC-backed exits [seen].
- An ETLA report follows Finnish sellers after acquisitions, but not how much they made [seen].

The US benchmark is Azevedo, Scheuer, Smetters & Yang (NBER w34512, July 2026): 88% of founders get nothing and the top 1% capture 79%.

## Where it can be done

Founder payoffs need two things: who owns the company (ideally through the founder's holding company), and that holding company's accounts. A register check on 28 October gave this.

| Country | Owners public and free? | Accounts free and machine-readable? | Verdict |
| --- | --- | --- | --- |
| **Denmark** | Yes: legal owners with 5% or more in the company register (CVR). Beneficial owners closed to the public since 1 Sep 2025 | Yes: XBRL, index open (tested; 12 of 29 recent reports were holding companies) | **Core.** The CVR API needs free credentials requested by a person |
| **Estonia** | Yes: an open shareholder file with each shareholder's contribution, stake and start and end dates (seen on the open-data page) | Annual-report key figures 2019–2025 as CSV; full reports through e-Business Register services | **Core.** Downloading needs you to accept the licence. Personal ID numbers removed since Nov 2024; beneficial owners out of open data since 10 Jul 2026 |
| **Norway** | Yes: Skatteetaten's yearly CSV of every shareholder in every limited company (name, birth year, postcode, shares at 31 Dec), delivered as a one-week link | Open accounts API covers the latest year only and is labelled temporary; PDFs free; full XML paid | **Strong for ownership, weak for accounts.** 49,908 "holding" companies in the open register (tested) |
| **UK** | Yes: shareholders in confirmation-statement PDFs (not in the API); people with significant control public | Yes: about 75% filed as iXBRL, free daily and monthly bulk (tested). Small companies may leave out the P&L, but equity is still there | **Extension.** Large and noisy. Shareholder PDFs need the document API (free key, needs an account) |
| Germany | Yes: the GmbH shareholder list, free since Aug 2022 | Balance sheet and notes only; no bulk feed; may cost about €1 each | Partial |
| Sweden | No: the share register is kept at the company | Yes: iXBRL from 2020 via a free API | Accounts only |
| Finland | No: kept at the company | Only about 5% of accounts in the free API | Weak |
| France | No, for SAS | INPI API, but small firms can make the P&L confidential | Weak |
| Netherlands, Hungary, Spain | No, or paid | Paid, or behind a CAPTCHA (Hungary's e-beszámoló) | Not for this project |

**What the EU's high-value-datasets rule adds.** It makes machine-readable company accounts free by API and bulk download, but not owner lists. The financial statements it covers include the notes listing **participating interests and subsidiaries**; that reading comes from a secondary mirror and should be confirmed on EUR-Lex. Parsing those notes rebuilds holding company → startup links from text. That would work even where shareholder registers are closed (Sweden's iXBRL, Ireland's CRO statements), which is a networks × language move in itself.

## The design

- **Core sample:** Denmark and Estonia, both small, open and complete. Add Norway for ownership, and the UK only if time allows. Keep to founders of companies set up in 2012–2020, so five-year outcomes exist.
- **Network.** People → holding companies → startups ← investors, across borders. VC funds show up as shareholders in the registers themselves, so the financing route can be read from the cap table, without a commercial database.
  - Measures: co-investment communities by country and investor centrality.
  - Question: are founders in the central investor cluster diluted more, and paid more?
- **Text.**
  - Management reviews and notes: sale events, and the participating-interest lists that rebuild ownership.
  - Company activity descriptions, plus Danish and Nordic startup descriptions from The Hub.
  - Estonian report text is not in bulk, so its text half is the activity descriptions.
- **Financing route:**
  - **VC-backed:** a fund appears as a shareholder.
  - **Angel:** individual non-founders take stakes.
  - **Grant:** from public grant lists.
  - **Self-funded:** no outside equity holder ever.
  - Crunchbase, The Hub or news can confirm it where their terms allow.
- **Payoff:** the founder's stake over time, the holding company's equity and dividends where accounts show them, and an exit, detected when a company acquirer replaces the owners. A dissolved or bankrupt company counts as zero.
- **Outcome measures:** share at zero, quantiles and top-1% share by financing route × country, against the US benchmark.

## Checks

- **Financing route from the register:** match it against Crunchbase, The Hub or news for 100 companies and report precision and recall.
- **Counts:** reproduce known totals. For Denmark, the DI Startup Barometer's roughly 3,000 funded firms. For Norway, compare returns with van Praag & Raknerud.
- **Null:** shuffle the financing route within country × founding year × industry × size.
- **Name matching:** Estonia has dropped ID numbers, so hand-verify 100 person matches across companies.

**Drop or narrow it if:**
- fewer than about 300 VC-backed founder chains resolve across countries. Then narrow to Denmark and Estonia.
- fewer than about 100 exits are found. Then make five-year holding-company equity the main outcome.

**Figure.** For each country, the payoff distribution of VC-backed against self-funded founders: share at zero, then quantiles on a log scale, with the US line from Azevedo et al. beside it.

## Steps only you can take

- **Estonia:** accept the open-data licence and download the shareholder and annual-report files.
- **Denmark:** request CVR API credentials from Erhvervsstyrelsen.
- **Norway:** request the Aksjonærregisteret CSV from Skatteetaten (the link lasts one week).
- **UK (optional):** create a Companies House account for the document API key.
- **Personal data:** names and birth years of real people. Keep raw data local, report only aggregates, and check DTU's rules for personal data in student projects.

## Plan against the course dates

| When | What |
| --- | --- |
| By 4 Nov (dataset locked) | Danish and Estonian ownership chains built for a pilot of 200 companies; matches hand-checked |
| 11 Nov | Full Danish and Estonian samples; financing-route labels checked against Crunchbase, The Hub or news |
| 18 Nov | Payoff distributions, nulls and the network analysis; Norway added if the CSV has arrived |
| 25 Nov | Paper draft in the PNAS template, figures final |
| 27 Nov | Hand-in |

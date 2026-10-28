# Open sources for "What do European founders actually take home?", checked 28 October 2026

**Rule applied.** A source is usable only if three things hold:
1. Its data is free and public.
2. Its terms or licence do not explicitly prohibit collection by an official API, bulk download, or the course's method (calling the JSON endpoints a page itself uses, gently, with an identifying user agent).
3. Its robots.txt does not disallow the paths used.

Sources were checked by two research agents and by direct requests. Tags: [opened] means the source text was read; [seen] means it was seen only in search results. Re-read the exact wording in a browser before collecting: the fetch tool paraphrases and cuts long quotes.

## Usable

| Source | Licence or terms | Access | What it gives the question |
| --- | --- | --- | --- |
| **Tech.eu Funding Explorer API** (funding.tech.eu/api/v1) | API docs: "Licensed CC BY 4.0"; cite "Tech.eu Funding Explorer" and link the URL [opened] | No key, no account. Limits: 120 per 60 s, 600 per hour, 2,000 per day per IP. robots.txt allows `/api/v1`. Endpoints `/rounds`, `/companies/{id}`, `/investors`, `/exits`, `/changes` (checked directly) | **The financing-route and exit backbone for Europe.** About 38.9k companies, 52.5k rounds with stage, EUR amount and investors, and 8.9k exits with type, EUR value and acquirer. Founder names only |
| **UK Companies House** | Open Government Licence v3.0; "We impose no rules or requirements on how the information on the public register is used" [opened] | Bulk accounts free (tested). API needs a free key, 600 requests per 5 minutes | Accounts (equity; P&L can be left out), people with significant control, officers, shareholders in confirmation-statement PDFs |
| **Norway Brønnøysund** (data.brreg.no) | Norwegian licence for open data (NLOD); no registration [opened] | Open API and nightly bulk files (tested) | Companies, roles (founders, board), beneficial-owner dataset; accounts only for the latest year (the API is temporary) |
| **Norway Aksjonærregisteret** (Skatteetaten) | No licence stated. Obligations: your own GDPR legal basis, and delete data you no longer use [opened] | Order form; CSV link valid for a week | **Every shareholder of every Norwegian limited company**: name, birth year, postcode, shares. The best ownership source found |
| **Finland PRH open data** | CC BY 4.0 [opened] | Open API (tested) | Company basics and notifications; P&L and balance sheet only for about 5% of filings. No owners |
| **Ireland CRO open data** | CC BY 4.0 [opened] | Bulk and API | Company records; financials and officers not confirmed |
| **France BODACC** | Licence Ouverte [opened] | API and bulk | Company sales, creations, insolvencies, amendments, accounts filings |
| **France INPI RNE** | INPI's free reuse licence, commercial or not; cite source and date; GDPR [opened] | Account request, then FTP or API | Company data and non-confidential accounts |
| **EU CORDIS** | CC BY 4.0 [opened] | Bulk downloads | EU grants to startups, as one non-VC financing route |
| **EU Financial Transparency System** | No licence on its help page (EC policy assumed) | Yearly files 2007–2025 | Beneficiaries of EU money and amounts |
| **Wikidata** | CC0 [opened] | API with an informative user agent; dumps for bulk | Founders, investors, acquisitions for notable firms |
| **Empire Flippers API** | Terms (8 Nov 2025) have no prohibition; API docs say no authentication and "no more than 1 request per second" [opened] | Open | Sale prices and multiples of small online businesses. Off-topic for European VC founders; useful only as a self-funded comparison |
| **Hacker News official API** | MIT, "no rate limit" [opened] | Open | Discussion text; marginal for this question |
| **Arctic Shift (Reddit archive)** | README: a few requests per second are fine [opened] | Open, monthly dumps | Founders' self-reported exits. Depends on Reddit's terms, which could not be read. Reddit stops new Data API applications on **31 Oct 2026** [seen] |
| **Danmarks Innovationsfond, EIFO pages** | No terms page found; robots.txt open [opened] | Public pages | Danish public grants and state investments, for the "grants" financing route |

## Usable only through the official route

- **Danish company register (CVR).** Executive order BEK 1243/2022 §17: "Det er ikke tilladt at crawle … eller anvende andre metoder til automatisk indeksering og opslag" [opened]. So never call datacvr's page endpoints. Bulk data comes only through Erhvervsstyrelsen's system-to-system access, with personal credentials, whose terms could not be read (403). The orders were amended in 2023 and 2025, so check §17 there.
- **Danish annual reports** (distribution.virk.dk). An official open index (tested), reportedly under Denmark's open public data licence [seen]. Confirm the licence before relying on it.
- **Estonia e-Business Register.** The open-data page offers shareholder and annual-report files after you accept a licence; the licence text could not be read (403). Accept it in a browser and read it first.
- **Sweden Bolagsverket.** The high-value-data API is free after registration, and the bulk files are CC BY 2.5 SE [seen]. No owner data.

## Excluded: terms explicitly prohibit it

| Source | Clause |
| --- | --- |
| Crunchbase | (h) "Crawls, scrapes, or spiders…"; (i) "any automated means or tools"; (j) no storing "any significant portion" (30 Sep 2026). Basic is CC BY, but no new keys are issued [seen] |
| Dealroom, including Startup Estonia's database | Art. 16.7: "may not access, query or extract data from the Platform by any automated means, including scraping, crawlers" (Oct 2026) |
| Sifted | s.7.6: no "text or data mining or web scraping" (1 Feb 2026) |
| Y Combinator directory | "you will not engage in or use any data mining, robots, scraping or similar data gathering or extraction methods". **The YC pull of 23 and 28 October in `data/raw/` must not be used for the paper** |
| The Hub | "may not otherwise copy, save or otherwise reproduce" (08.08.2024), a ban on storing. Usable only with written permission |
| Wellfound, Signal NFX | Explicit bans on harvesting, scraping and bots |
| OpenCorporates | "Using any automated system (e.g. scraping) to extract data…" |
| Germany Handelsregister | At most 60 lookups per hour and IP blocking; the Unternehmensregister forbids building a parallel register |
| GLEIF | CC0, but only through its own Access Service, with liquidated damages for breach |

**Not confirmed** (pages blocked), so treat as unusable until read: EU-Startups and its database (paid), ArcticStartup's terms (robots.txt allows articles), OpenVC, Seedtable.

## How the pieces fit the question

- **Financing route and exits, Europe-wide:** Tech.eu Funding Explorer (CC BY 4.0). Use EU CORDIS and Danish grant pages for grant-funded firms.
- **Who owns the company, and the founder's stake:** Norway's shareholder register, UK confirmation statements and PSC, and Estonia's shareholder file (after accepting its licence). Denmark only through official CVR access.
- **What the founder's holding company holds:** UK bulk accounts, Danish annual reports, Norway's latest-year accounts, Finnish iXBRL statements.
- **Text half:** company descriptions in Tech.eu, management reviews in accounts, Wikidata.
- **Network:** Tech.eu's investor–company and acquirer–target links, combined with register ownership chains (person → holding company → startup).

**Recommended core:** Tech.eu (financing and exits) × Norway (shareholders) × UK (accounts and owners), with Denmark and Estonia added once official access is in place. Norway plus the UK need no permissions beyond Skatteetaten's order form and a free Companies House key.

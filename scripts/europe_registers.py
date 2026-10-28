"""Probe: which European business registers answer an honest research client (28 October 2026)?

One or two gentle requests each. Refusals are recorded, not worked around. Prints findings; writes nothing.
"""
import json
import re
import time
import urllib.parse
import urllib.request

UA = "Mozilla/5.0 (research; 02805 DTU student project)"


def get(url, accept="application/json"):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": accept})
    with urllib.request.urlopen(req, timeout=40) as r:
        return r.read().decode("utf-8", "replace")


def run(name, fn):
    try:
        print(f"[{name}] {fn()}")
    except urllib.error.HTTPError as e:
        print(f"[{name}] HTTP {e.code}{' (not for scripts)' if e.code in (401, 403, 429) else ''}")
    except Exception as e:
        print(f"[{name}] FAILED {type(e).__name__}: {str(e)[:150]}")
    time.sleep(1.5)


def norway():
    d = json.loads(get("https://data.brreg.no/enhetsregisteret/api/enheter?navn=holding&organisasjonsform=AS&size=1"))
    total = d.get("page", {}).get("totalElements")
    org = d["_embedded"]["enheter"][0]["organisasjonsnummer"]
    time.sleep(1.0)
    roles = json.loads(get(f"https://data.brreg.no/enhetsregisteret/api/enheter/{org}/roller"))
    time.sleep(1.0)
    try:
        acc = json.loads(get(f"https://data.brreg.no/regnskapsregisteret/regnskap/{org}"))
        a = acc[0] if isinstance(acc, list) and acc else acc
        acc_info = f"accounts API answers; keys={sorted(a.keys())[:8] if isinstance(a, dict) else type(a).__name__}"
    except urllib.error.HTTPError as e:
        acc_info = f"accounts API HTTP {e.code}"
    return f"AS companies named 'holding': {total}; roles API groups={len(roles.get('rollegrupper', []))}; {acc_info}"


def uk():
    body = get("http://download.companieshouse.gov.uk/en_accountsdata.html", "text/html")
    daily = re.findall(r'href="(Accounts_Bulk_Data-[^"]+\.zip)"', body)
    body2 = get("http://download.companieshouse.gov.uk/en_monthlyaccountsdata.html", "text/html")
    monthly = re.findall(r'href="(Accounts_Monthly_Data-[^"]+\.zip)"', body2)
    return f"daily iXBRL accounts zips: {len(daily)} (e.g. {daily[:1]}); monthly archives: {len(monthly)} (e.g. {monthly[:1]})"


def finland():
    d = json.loads(get("https://avoindata.prh.fi/opendata-ytj-api/v3/companies?name=holding"))
    return f"PRH open data v3 answers; companies matching 'holding': {d.get('totalResults')}"


def hungary():
    body = get("https://e-beszamolo.im.gov.hu/oldal/kezdolap", "text/html")
    return f"e-beszamolo reachable, {len(body)} bytes; captcha mentioned: {'captcha' in body.lower()}"


def sweden():
    body = get("https://bolagsverket.se/apierochoppnadata.2531.html", "text/html")
    return f"Bolagsverket API page reachable, {len(body)} bytes; mentions 'värdefulla datamängder': {'värdefulla' in body.lower()}"


for name, fn in [("Norway Brønnøysund", norway), ("UK Companies House accounts", uk), ("Finland PRH", finland),
                 ("Hungary e-beszámoló", hungary), ("Sweden Bolagsverket", sweden)]:
    run(name, fn)

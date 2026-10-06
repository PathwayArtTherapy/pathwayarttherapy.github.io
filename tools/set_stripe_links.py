"""Fill in the Stripe payment links on /pay/.

Usage: python3 tools/set_stripe_links.py stripe-links.txt
The text file has one link per line, as  slot = https://buy.stripe.com/...
Slots: session-aud, session-gbp, session-eur, group-aud, group-eur, pd-aud
"""
import pathlib, re, sys
page = pathlib.Path(__file__).resolve().parent.parent / "pay" / "index.html"
links = {}
for line in pathlib.Path(sys.argv[1]).read_text(encoding="utf-8").splitlines():
    if "=" in line and not line.strip().startswith("#"):
        k, v = (x.strip() for x in line.split("=", 1))
        if v:
            assert v.startswith("https://"), f"{k}: not a web address: {v}"
            links[k] = v
s = page.read_text(encoding="utf-8")
for k, v in links.items():
    s = s.replace(f'href="STRIPE-LINK:{k}"', f'href="{v}"')
page.write_text(s, encoding="utf-8")
left = sorted(set(re.findall(r'STRIPE-LINK:([a-z-]+)', s)))
print("filled:", ", ".join(sorted(links)) or "none")
print("still missing:", ", ".join(left) if left else "none, ready to publish")

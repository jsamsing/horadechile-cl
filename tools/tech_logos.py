#!/usr/bin/env python3
"""Genera templates/_tech_footer.html: logos de las tecnologías que este sitio REALMENTE usa (protocolo de logos de searchlab360-com).
Íconos de simple-icons (CC0) con su color oficial; sin ícono = solo el nombre.
Uso: npm i simple-icons (en /tmp/si) y python3 tools/tech_logos.py /tmp/si/node_modules/simple-icons
Usa hoy: Google Analytics 4 (GA4 en content.py, con consentimiento), Google Search Console (archivo de verificación en el build) y SiteGround (hosting)."""
import json, os, re, sys
SI = sys.argv[1] if len(sys.argv) > 1 else "/tmp/si/node_modules/simple-icons"
D = json.load(open(os.path.join(SI, "data/simple-icons.json")))
HEX = {i.get("slug"): i["hex"] for i in (D if isinstance(D, list) else D["icons"])}
TECH = [("googleanalytics", "Google Analytics", "https://marketingplatform.google.com/about/analytics/"),
        ("googlesearchconsole", "Google Search Console", "https://search.google.com/search-console/about"),
        ("siteground", "SiteGround", "https://www.siteground.com/")]
def svg(slug):
    p = os.path.join(SI, "icons", slug + ".svg")
    if not os.path.exists(p): return ""
    s = re.sub(r"<title>.*?</title>", "", open(p).read())
    return s.replace("<svg ", f'<svg aria-hidden="true" width="20" height="20" fill="#{HEX.get(slug, "555")}" ', 1)
f = ['<ul class="ftech" aria-label="Tecnologías que usa este sitio">']
for slug, name, url in TECH:
    f.append(f'<li><a href="{url}" target="_blank" rel="nofollow noopener" data-ev="cta_click" data-label="tech_{slug}">{svg(slug)}<span>{name}</span></a></li>')
f.append('</ul>\n<p class="mut ftech-n">Marcas de sus respectivos dueños.</p>')
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "templates", "_tech_footer.html"), "w").write("".join(f) + "\n")
print("ok", len(TECH))

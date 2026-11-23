"""Genera horadechile.cl estático en dist/ (Python + Jinja2, como los otros sitios propios).
Falla si title (50-60), description (100-160), JSON-LD o enlaces internos quedan mal."""
import datetime as dt
import json
import re
import shutil
import sys
from pathlib import Path

from jinja2 import Environment, FileSystemLoader
from PIL import Image, ImageDraw, ImageFont

import content as C

ROOT = Path(__file__).resolve().parent
DIST = ROOT / "dist"
MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
DIAS = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]


def fecha_txt(iso, dia=True):
    d = dt.date.fromisoformat(iso)
    return (f"{DIAS[d.weekday()]} " if dia else "") + f"{d.day} de {MESES[d.month - 1]} de {d.year}"


def ld(p):
    url = C.DOMINIO + p["path"]
    g = [{"@type": "WebSite", "@id": C.DOMINIO + "/#web", "name": C.MARCA, "url": C.DOMINIO + "/", "inLanguage": "es-CL"},
         {"@type": "WebPage", "@id": url, "url": url, "name": p["title"], "description": p["desc"], "inLanguage": "es-CL",
          "isPartOf": {"@id": C.DOMINIO + "/#web"}, "dateModified": C.REVISADO}]
    if p["path"] != "/":
        g.append({"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Inicio", "item": C.DOMINIO + "/"},
            {"@type": "ListItem", "position": 2, "name": p["h1"], "item": url}]})
    if p.get("faqs"):
        g.append({"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faqs"]]})
    return json.dumps({"@context": "https://schema.org", "@graph": g}, ensure_ascii=False).replace("</", "<\\/")


def og(p, out):
    W, H = 1200, 630
    im = Image.new("RGB", (W, H), (14, 36, 64))
    d = ImageDraw.Draw(im)
    fb = ImageFont.truetype(str(ROOT / "fonts/Inter-ExtraBold.otf"), 76)
    fm = ImageFont.truetype(str(ROOT / "fonts/Inter-Medium.otf"), 36)
    d.ellipse((80, 80, 180, 180), outline=(255, 255, 255), width=10)
    d.line((130, 105, 130, 132), fill=(245, 180, 0), width=10); d.line((130, 132, 152, 146), fill=(245, 180, 0), width=10)
    d.text((210, 100), C.MARCA, font=fm, fill=(200, 214, 230))
    words, lines, cur = p["h1"].split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=fb) > W - 160: lines.append(cur); cur = w
        else: cur = t
    lines.append(cur)
    for i, l in enumerate(lines[:3]):
        d.text((80, 250 + i * 92), l, font=fb, fill=(255, 255, 255))
    d.rectangle((80, 540, 260, 548), fill=(245, 180, 0))
    d.text((80, 565), "horadechile.cl", font=fm, fill=(200, 214, 230))
    im.save(out, "JPEG", quality=86)


def main():
    if DIST.exists(): shutil.rmtree(DIST)
    (DIST / "og").mkdir(parents=True)
    cambios = [dict(c, txt=fecha_txt(c["sabado"])) for c in C.CAMBIOS]
    css = (ROOT / "templates/style.css").read_text()
    js = (ROOT / "templates/app.js").read_text().replace("__CAMBIOS__", json.dumps([{"utc": c["utc"], "tipo": c["tipo"], "txt": c["txt"]} for c in cambios], ensure_ascii=False)).replace("__GA4__", C.GA4)
    env = Environment(loader=FileSystemLoader(ROOT / "templates"), autoescape=True)
    errores, urls = [], []
    for p in C.PAGINAS:
        p["slug"] = p["path"].strip("/") or "inicio"
        if not p.get("noindex") and not 50 <= len(p["title"]) <= 60: errores.append(f"title {len(p['title'])}: {p['path']}")
        if not 100 <= len(p["desc"]) <= 160: errores.append(f"description {len(p['desc'])}: {p['path']}")
        html = env.get_template(p["tpl"]).render(p=p, D=C.DOMINIO, MARCA=C.MARCA, CSS=css, JS=js, LD=ld(p), ZONAS=C.ZONAS, PAISES=C.PAISES,
                                                 CAMBIOS=cambios, AVISOS=C.AVISOS, REVISADO_TXT=fecha_txt(C.REVISADO, dia=False))
        html = html.replace('<script type="application/ld+json">', '<script type="application/ld+json">', 1)
        json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', html, re.S).group(1).replace("<\\/", "</"))
        out = DIST / p["path"].strip("/") / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html)
        og(p, DIST / "og" / f"{p['slug']}.jpg")
        if not p.get("noindex"): urls.append(C.DOMINIO + p["path"])
    validas = {p["path"] for p in C.PAGINAS}
    for f in DIST.rglob("*.html"):
        for h in re.findall(r'href="(/[^"#?]*)"', f.read_text()):
            if h not in validas and not (DIST / h.strip("/")).is_file() and h != "/favicon.svg": errores.append(f"enlace roto {h} en {f}")
    (DIST / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "".join(f"  <url><loc>{u}</loc><lastmod>{C.REVISADO}</lastmod></url>\n" for u in urls) + "</urlset>\n")
    (DIST / "robots.txt").write_text("User-agent: *\nAllow: /\n\n" + "".join(f"User-agent: {b}\nDisallow: /\n\n" for b in ["GPTBot", "CCBot", "Google-Extended", "anthropic-ai", "ClaudeBot", "Bytespider", "meta-externalagent", "Applebot-Extended"])
        + "Content-Signal: search=yes, ai-input=yes, ai-train=no\n\nSitemap: " + C.DOMINIO + "/sitemap.xml\n")
    (DIST / "llms.txt").write_text(f"# {C.MARCA}\n\n> Hora oficial de Chile en vivo (continental, Aysen y Magallanes, Isla de Pascua), fechas del cambio de hora segun el Decreto Supremo 98 de 2026 y diferencia horaria con otros paises. Sitio independiente, Chile.\n\nLast updated: {C.REVISADO}\n\n## Datos clave\n- Chile continental: UTC-4 en invierno, UTC-3 en verano.\n- Aysen y Magallanes: UTC-3 todo el ano.\n- Isla de Pascua: UTC-6 en invierno, UTC-5 en verano.\n- Proximo cambio: 24:00 del sabado 3 de abril de 2027, se atrasa una hora.\n\n## Paginas\n"
        + "".join(f"- [{p['h1']}]({C.DOMINIO}{p['path']}): {p['desc']}\n".encode("ascii", "ignore").decode() for p in C.PAGINAS if not p.get("noindex"))
        + f"\n## Optional\n- [Sitemap]({C.DOMINIO}/sitemap.xml)\n")
    (DIST / f"{C.INDEXNOW_KEY}.txt").write_text(C.INDEXNOW_KEY)
    (DIST / "favicon.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="7" fill="#0e2440"/><circle cx="16" cy="16" r="10" fill="none" stroke="#fff" stroke-width="2.5"/><path d="M16 10v6l4.5 3" fill="none" stroke="#f5b400" stroke-width="2.5" stroke-linecap="round"/></svg>')
    (DIST / ".htaccess").write_text("""RewriteEngine On
RewriteCond %{HTTPS} off [OR]
RewriteCond %{HTTP_HOST} ^www\\. [NC]
RewriteRule ^(.*)$ https://horadechile.cl/$1 [R=301,L]
ErrorDocument 404 /
<IfModule mod_headers.c>
Header always set X-Content-Type-Options "nosniff"
Header always set Referrer-Policy "strict-origin-when-cross-origin"
Header always set Strict-Transport-Security "max-age=31536000"
Header always set X-Frame-Options "SAMEORIGIN"
<FilesMatch "\\.html$">
Header set Link "</llms.txt>; rel=\\"describedby\\"; type=\\"text/markdown\\""
Header set Cache-Control "public, max-age=300"
</FilesMatch>
<FilesMatch "\\.(jpg|svg)$">
Header set Cache-Control "public, max-age=2592000"
</FilesMatch>
</IfModule>
""")
    if errores:
        print("\n".join("ERROR: " + e for e in errores)); sys.exit(1)
    print(f"OK: {len(C.PAGINAS)} páginas ({len(urls)} indexables) en dist/")


if __name__ == "__main__":
    main()

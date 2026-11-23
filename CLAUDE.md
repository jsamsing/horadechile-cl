# Hora de Chile — horadechile.cl

Sitio útil de SearchLab (repo público: sin datos privados ni credenciales aquí): hora oficial de Chile en vivo, cambio de hora y diferencia horaria. Avisos de la casa SOLO a searchlab.cl y Bifrok (resuelvealtiro.cl cuando esté publicado); nunca Pieza al Tiro ni ELCOM. Monetización: avisos propios y AdSense.

## Stack
- `content.py` (todo el texto y datos) + `templates/` (Jinja2, CSS y JS inline, sin terceros salvo GA4 con consentimiento) → `python3 build.py` → `dist/`. El build FALLA si title fuera de 50-60, description fuera de 100-160, JSON-LD inválido o enlace interno roto.
- Relojes con `Intl.DateTimeFormat` y la base IANA del navegador (America/Santiago, America/Punta_Arenas, Pacific/Easter).
- Cambios de hora: `CAMBIOS` en content.py según el Decreto Supremo N.º 98 (julio 2026): verano desde las 24:00 del primer sábado de septiembre hasta las 24:00 del primer sábado de abril, hasta abril de 2029. Aysén y Magallanes UTC-3 todo el año. Revisar si sale un decreto nuevo y actualizar `REVISADO`.
- Schema: WebSite + WebPage + BreadcrumbList + FAQPage. OG 1200x630 por página (Pillow, fonts/Inter). robots.txt con Content-Signal, llms.txt, sitemap, IndexNow (`INDEXNOW_KEY`), .htaccess (https sin www, cabeceras, Link describedby).
- Deploy: push a `main` → build → FTPS a `horadechile.cl/public_html/` (secrets FTP_HOST, FTP_USER, FTP_PASS; sin ellos solo valida). Runner: Oracle por defecto (variable DEPLOY_RUNS_ON para cambiar).
- Pendiente: GA4 (`GA4` en content.py), GSC + acceso a indexador@, BigQuery, AdSense, correo alias y redes; crecer con secciones según Semrush (hora en cada país, feriados → enlazar a feriados-de-chile.cl).
- Menú móvil: hamburguesa a la DERECHA, panel desde la derecha, enlaces de 48 px.

"""Todo el texto de horadechile.cl (fuente única). Fechas de cambio de hora: Decreto Supremo N.º 98 (Ministerio del
Interior, Diario Oficial, julio de 2026): horario de verano desde las 24:00 del primer sábado de septiembre hasta las
24:00 del primer sábado de abril, con calendario fijado hasta abril de 2029. Aysén y Magallanes mantienen UTC-3 todo el año.
Revisar cada vez que el Gobierno publique un decreto nuevo (y `REVISADO`)."""

DOMINIO = "https://horadechile.cl"
MARCA = "Hora de Chile"
REVISADO = "2026-11-23"
GA4 = ""  # se completa al crear la propiedad (solo carga en el host horadechile.cl)
INDEXNOW_KEY = "7c1f4a9e2b6d48c3a5e0f9b1d2c3e4f5"

# Cambios de hora de Chile continental e Isla de Pascua (instante UTC exacto, verano = UTC-3 continental)
# atrasar: 24:00 del primer sábado de abril (UTC-3) = domingo 03:00 UTC; adelantar: 24:00 del primer sábado de septiembre (UTC-4) = domingo 04:00 UTC
CAMBIOS = [
    {"utc": "2027-04-04T03:00:00Z", "sabado": "2027-04-03", "tipo": "atrasar", "regimen": "invierno"},
    {"utc": "2027-09-05T04:00:00Z", "sabado": "2027-09-04", "tipo": "adelantar", "regimen": "verano"},
    {"utc": "2028-04-02T03:00:00Z", "sabado": "2028-04-01", "tipo": "atrasar", "regimen": "invierno"},
    {"utc": "2028-09-03T04:00:00Z", "sabado": "2028-09-02", "tipo": "adelantar", "regimen": "verano"},
    {"utc": "2029-04-08T03:00:00Z", "sabado": "2029-04-07", "tipo": "atrasar", "regimen": "invierno"},
]

ZONAS = [
    {"id": "cont", "tz": "America/Santiago", "nombre": "Chile continental", "detalle": "Santiago y todas las regiones salvo Aysén y Magallanes", "inv": "UTC-4", "ver": "UTC-3"},
    {"id": "mag", "tz": "America/Punta_Arenas", "nombre": "Aysén y Magallanes", "detalle": "Coyhaique, Punta Arenas y Puerto Natales: UTC-3 todo el año, sin cambio de hora", "inv": "UTC-3", "ver": "UTC-3"},
    {"id": "pas", "tz": "Pacific/Easter", "nombre": "Isla de Pascua", "detalle": "Rapa Nui: dos horas menos que el continente", "inv": "UTC-6", "ver": "UTC-5"},
]

PAISES = [
    ("Argentina", "America/Argentina/Buenos_Aires"), ("Perú", "America/Lima"), ("Bolivia", "America/La_Paz"),
    ("Brasil (São Paulo)", "America/Sao_Paulo"), ("Colombia", "America/Bogota"), ("México (CDMX)", "America/Mexico_City"),
    ("Venezuela", "America/Caracas"), ("Uruguay", "America/Montevideo"), ("Paraguay", "America/Asuncion"),
    ("Ecuador", "America/Guayaquil"), ("EE. UU. (Nueva York)", "America/New_York"), ("EE. UU. (Los Ángeles)", "America/Los_Angeles"),
    ("España (Madrid)", "Europe/Madrid"), ("Reino Unido", "Europe/London"), ("Alemania", "Europe/Berlin"),
    ("China", "Asia/Shanghai"), ("Japón", "Asia/Tokyo"), ("Australia (Sídney)", "Australia/Sydney"),
]

# Red de sitios útiles (se enlazan entre sí; "vivo": True solo cuando el sitio ya está publicado)
RED = [
    {"url": "https://horadechile.cl/", "nombre": "Hora de Chile", "texto": "Hora exacta y cambio de hora", "vivo": True},
    {"url": "https://feriados-de-chile.cl/", "nombre": "Feriados de Chile", "texto": "Feriados y fines de semana largos", "vivo": True},
    {"url": "https://calculadora-chile.cl/", "nombre": "Calculadora Chile", "texto": "Sueldo líquido, IVA, UF y más", "vivo": False},
    {"url": "https://formatos-chile.cl/", "nombre": "Formatos Chile", "texto": "Cartas, contratos y formularios", "vivo": False},
]

# Avisos de la casa (solo proyectos propios autorizados: searchlab.cl y Bifrok; resuelvealtiro.cl cuando esté publicado)
AVISOS = [
    {"id": "searchlab", "icono": "pin", "url": "https://www.searchlab.cl/?utm_source=horadechile&utm_medium=aviso&utm_campaign=casa",
     "titulo": "¿Tu negocio aparece en Google Maps?", "texto": "Página web, ficha de Google Maps y preparación para buscadores con IA desde $9.990 al mes.", "cta": "Ver planes"},
    {"id": "bifrok", "icono": "wifi", "url": "https://bifrok.com/es-cl/?utm_source=horadechile&utm_medium=aviso&utm_campaign=casa",
     "titulo": "¿Internet lento en tu casa?", "texto": "Compara fibra, TV y Starlink en tu comuna y habla directo con un vendedor.", "cta": "Comparar planes"},
]

PAGINAS = [
    {
        "path": "/", "tpl": "home.html",
        "title": "Hora en Chile ahora: hora exacta de Santiago y regiones",
        "desc": "Hora exacta de Chile en este momento: Santiago, Magallanes e Isla de Pascua, huso horario actual y cuánto falta para el próximo cambio de hora.",
        "h1": "Hora en Chile ahora",
        "corta": "En Chile hay tres horas oficiales: la continental (Santiago y casi todo el país), la de Aysén y Magallanes, que no cambia en el año, y la de Isla de Pascua, dos horas menos que el continente. El reloj de abajo muestra la hora exacta de cada una.",
        "faqs": [
            ("¿Qué hora es en Chile?", "La hora de Chile continental es la que muestra el primer reloj de esta página, igual para Santiago y para todas las regiones salvo Aysén y Magallanes. Hoy rige el horario de verano (UTC-3) hasta las 24:00 del sábado 3 de abril de 2027."),
            ("¿Qué huso horario tiene Chile?", "Chile continental usa UTC-4 en invierno y UTC-3 en verano. Aysén y Magallanes usan UTC-3 todo el año. Isla de Pascua usa UTC-6 en invierno y UTC-5 en verano."),
            ("¿Cuándo es el próximo cambio de hora?", "El próximo cambio es a las 24:00 del sábado 3 de abril de 2027: los relojes se atrasan una hora y vuelve el horario de invierno, salvo en Aysén y Magallanes."),
            ("¿Por qué Magallanes tiene otra hora?", "Las regiones de Aysén y Magallanes mantienen UTC-3 todo el año, para aprovechar la luz de la tarde en el extremo sur; por eso, durante el horario de invierno tienen una hora más que Santiago."),
        ],
    },
    {
        "path": "/cambio-de-hora/", "tpl": "cambio.html",
        "title": "Cambio de hora Chile 2027: fecha y si se atrasa o adelanta",
        "desc": "Fecha del próximo cambio de hora en Chile: sábado 3 de abril de 2027 se atrasa una hora. Calendario hasta 2029 y regiones que no cambian.",
        "h1": "Cambio de hora en Chile 2027",
        "corta": "El próximo cambio de hora en Chile es a las 24:00 del sábado 3 de abril de 2027: los relojes se atrasan 60 minutos y comienza el horario de invierno. Aysén y Magallanes no cambian. El horario de verano vuelve a las 24:00 del sábado 4 de septiembre de 2027.",
        "faqs": [
            ("¿Se atrasa o se adelanta la hora en abril?", "En abril se atrasa: a las 24:00 del primer sábado de abril los relojes vuelven a las 23:00 y se gana una hora de sueño. En septiembre se adelanta: a las 24:00 del primer sábado de septiembre pasan a la 01:00 del domingo."),
            ("¿Qué regiones no cambian la hora?", "Aysén y Magallanes mantienen UTC-3 todo el año y no ajustan sus relojes. Isla de Pascua sí cambia la hora, igual que el continente."),
            ("¿El celular cambia la hora solo?", "Sí, si tiene activada la hora automática o la zona «Santiago». Conviene revisar relojes de horno, auto, alarmas y equipos sin conexión, que hay que ajustar a mano."),
            ("¿Qué norma fija el cambio de hora?", "El Decreto Supremo N.º 98 del Ministerio del Interior, publicado en julio de 2026, que fija el horario de verano entre el primer sábado de septiembre y el primer sábado de abril hasta 2029."),
        ],
    },
    {
        "path": "/diferencia-horaria/", "tpl": "diferencia.html",
        "title": "Diferencia horaria entre Chile y otros países, en vivo",
        "desc": "Cuántas horas de diferencia hay entre Chile y Argentina, Perú, Colombia, México, España, Estados Unidos y más, calculado en vivo con la hora de hoy.",
        "h1": "Diferencia horaria entre Chile y otros países",
        "corta": "La diferencia horaria con Chile cambia durante el año, porque Chile y varios países cambian la hora en fechas distintas. Esta tabla la calcula en vivo con la hora de hoy, comparando con Chile continental (Santiago).",
        "faqs": [
            ("¿Cuántas horas de diferencia hay entre Chile y España?", "Depende de la época del año, porque ambos cambian la hora en fechas distintas. La tabla de esta página muestra la diferencia exacta de hoy."),
            ("¿Chile y Argentina tienen la misma hora?", "En verano de Chile, sí: ambos quedan en UTC-3. En invierno, Chile continental está una hora detrás de Argentina."),
            ("¿Cómo se calcula la diferencia?", "Se compara la hora oficial de cada país en este momento, con la base de datos de husos horarios de tu navegador, que se actualiza con cada cambio legal."),
        ],
    },
    {
        "path": "/privacidad/", "tpl": "legal.html", "noindex": True,
        "title": "Privacidad y cookies de Hora de Chile",
        "desc": "Cómo trata Hora de Chile los datos de quienes visitan el sitio: medición de visitas con consentimiento y sin datos personales.",
        "h1": "Privacidad y cookies",
    },
]

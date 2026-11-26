"""Todo el texto de horadechile.cl (fuente única). Fechas de cambio de hora: Decreto Supremo N.º 98 (Ministerio del
Interior, Diario Oficial, julio de 2026): horario de verano desde las 24:00 del primer sábado de septiembre hasta las
24:00 del primer sábado de abril, con calendario fijado hasta abril de 2029. Aysén y Magallanes mantienen UTC-3 todo el año.
Revisar cada vez que el Gobierno publique un decreto nuevo (y `REVISADO`)."""

DOMINIO = "https://horadechile.cl"
MARCA = "Hora de Chile"
REVISADO = "2026-11-23"
GA4 = "G-LZQ9PGKFC7"  # se completa al crear la propiedad (solo carga en el host horadechile.cl)
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
    {"url": "https://formatos-chile.cl/", "nombre": "Formatos Chile", "texto": "Cartas y documentos listos para usar", "vivo": True},
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
        "title": "Privacidad y datos personales de Hora de Chile",
        "desc": "Cómo trata Hora de Chile tus datos según la Ley 21.719: sin registro, medición de visitas solo con tu consentimiento y cómo ejercer tus derechos.",
        "h1": "Privacidad y datos personales",
    },
]

# Páginas por país (Semrush 2026-11-23, base Chile; volumen de la keyword principal + variantes «qué hora es en…»)
PAISES_PAG = [
    {"slug": "espana", "pais": "España", "tz": "Europe/Madrid", "kw": "hora en España", "vol": "49.500",
     "texto": "España peninsular usa la hora de Europa Central: UTC+1 en invierno y UTC+2 en verano, que va del último domingo de marzo al último domingo de octubre. Las Islas Canarias tienen una hora menos que Madrid. Como Chile y España cambian la hora en fechas opuestas, la diferencia con Santiago varía entre 4 y 6 horas según la época.",
     "faq": [("¿Cuántas horas de diferencia hay entre Chile y España?", "Entre 4 y 6 horas: España va por delante. El reloj de esta página muestra la diferencia exacta de hoy."), ("¿Qué hora es en Canarias?", "Una hora menos que en Madrid durante todo el año.")]},
    {"slug": "argentina", "pais": "Argentina", "tz": "America/Argentina/Buenos_Aires", "kw": "hora en Argentina", "vol": "27.100",
     "texto": "Argentina usa UTC-3 todo el año y no cambia la hora. Por eso, cuando Chile está en horario de verano ambos países tienen la misma hora, y durante el horario de invierno de Chile Argentina va una hora adelante. Todo el territorio argentino, de Jujuy a Tierra del Fuego, comparte el mismo huso.",
     "faq": [("¿Chile y Argentina tienen la misma hora?", "En verano de Chile sí (ambos en UTC-3). En invierno de Chile, Argentina va una hora adelante."), ("¿Argentina cambia la hora?", "No. Argentina mantiene UTC-3 todo el año.")]},
    {"slug": "mexico", "pais": "México", "tz": "America/Mexico_City", "kw": "hora en México", "vol": "27.100",
     "texto": "Ciudad de México usa UTC-6 todo el año: México eliminó el horario de verano en 2022, salvo algunos municipios de la frontera norte que siguen a Estados Unidos. El país tiene además zonas con otra hora, como Quintana Roo (Cancún), con una hora más que la capital, y la Baja California.",
     "faq": [("¿Cuántas horas de diferencia hay entre Chile y México?", "Con Ciudad de México, entre 2 y 3 horas: Chile va por delante. La diferencia exacta de hoy aparece en el reloj."), ("¿México tiene horario de verano?", "No en la mayor parte del país desde 2022; solo algunos municipios fronterizos lo mantienen.")]},
    {"slug": "brasil", "pais": "Brasil", "tz": "America/Sao_Paulo", "kw": "hora en Brasil", "vol": "22.200",
     "texto": "Brasilia y São Paulo usan UTC-3 todo el año: Brasil suspendió el horario de verano en 2019. Brasil tiene cuatro husos horarios; Manaos, por ejemplo, va una hora detrás de São Paulo. Con Chile en horario de verano, Santiago y São Paulo marcan la misma hora.",
     "faq": [("¿Brasil y Chile tienen la misma hora?", "Con São Paulo y Río de Janeiro, sí durante el horario de verano de Chile. En el invierno chileno, Brasil va una hora adelante."), ("¿Brasil cambia la hora?", "No desde 2019.")]},
    {"slug": "peru", "pais": "Perú", "tz": "America/Lima", "kw": "hora en Perú", "vol": "22.200",
     "texto": "Perú usa UTC-5 todo el año y no cambia la hora, igual en Lima, Cusco y Arequipa. Chile continental va dos horas delante de Perú en su horario de verano y una hora delante en invierno, algo útil al planificar viajes a Machu Picchu o reuniones con Lima.",
     "faq": [("¿Cuántas horas de diferencia hay entre Chile y Perú?", "Una hora en invierno de Chile y dos en verano: Chile va por delante."), ("¿Perú cambia la hora?", "No, usa UTC-5 todo el año.")]},
    {"slug": "colombia", "pais": "Colombia", "tz": "America/Bogota", "kw": "hora en Colombia", "vol": "18.100",
     "texto": "Colombia usa UTC-5 todo el año, sin horario de verano, en todo su territorio: Bogotá, Medellín, Cali y la costa caribe tienen la misma hora. La diferencia con Chile continental es de una hora durante el invierno chileno y de dos durante el verano chileno.",
     "faq": [("¿Cuántas horas de diferencia hay entre Chile y Colombia?", "Una o dos horas según la época: Chile va por delante."), ("¿Colombia cambia la hora?", "No, Colombia mantiene UTC-5 todo el año.")]},
    {"slug": "miami", "pais": "Miami", "tz": "America/New_York", "kw": "hora en Miami", "vol": "18.100",
     "texto": "Miami, en Florida, usa la hora del Este de Estados Unidos: UTC-5 en invierno y UTC-4 con el horario de verano, que va del segundo domingo de marzo al primer domingo de noviembre. Es la misma hora de Nueva York y Washington, y la diferencia con Santiago cambia entre 0 y 2 horas durante el año: en el invierno chileno coinciden.",
     "faq": [("¿Qué diferencia horaria hay entre Chile y Miami?", "Entre 0 y 2 horas, con Chile por delante o igual: varía porque ambos cambian la hora en fechas distintas."), ("¿Miami tiene la misma hora que Nueva York?", "Sí, ambas usan la hora del Este.")]},
    {"slug": "estados-unidos", "pais": "Estados Unidos (Nueva York)", "tz": "America/New_York", "kw": "hora en Estados Unidos", "vol": "14.800",
     "texto": "Estados Unidos tiene seis husos horarios principales: Este (Nueva York), Centro (Chicago), Montaña (Denver), Pacífico (Los Ángeles), Alaska y Hawái. Este reloj muestra la hora del Este, la más consultada; Los Ángeles tiene tres horas menos. Casi todo el país adelanta la hora el segundo domingo de marzo y la atrasa el primer domingo de noviembre.",
     "faq": [("¿Cuántas horas de diferencia hay entre Chile y Estados Unidos?", "Con Nueva York, entre 0 y 2 horas; con Los Ángeles, entre 3 y 5. Chile va por delante o igual."), ("¿Qué estados no cambian la hora?", "Hawái y la mayor parte de Arizona no usan horario de verano.")]},
    {"slug": "china", "pais": "China", "tz": "Asia/Shanghai", "kw": "hora en China", "vol": "12.100",
     "texto": "China usa una sola hora oficial para todo el país, la hora de Pekín: UTC+8 todo el año y sin horario de verano, aunque el territorio cruza cinco husos geográficos. Con Chile la diferencia es de 11 o 12 horas: cuando en Santiago es de noche, en Pekín y Shanghái ya es el día siguiente.",
     "faq": [("¿Cuántas horas de diferencia hay entre Chile y China?", "11 horas durante el verano de Chile y 12 en invierno; China va por delante."), ("¿China cambia la hora?", "No, usa UTC+8 todo el año.")]},
    {"slug": "francia", "pais": "Francia", "tz": "Europe/Paris", "kw": "hora en Francia", "vol": "12.100",
     "texto": "Francia metropolitana usa UTC+1 en invierno y UTC+2 en verano, igual que España y Alemania, con el cambio el último domingo de marzo y de octubre. Los territorios de ultramar, como Guadalupe, Martinica o la Polinesia Francesa, tienen su propia hora.",
     "faq": [("¿Cuántas horas de diferencia hay entre Chile y Francia?", "Entre 4 y 6 horas, con Francia por delante, según la época del año."), ("¿París tiene la misma hora que Madrid?", "Sí, ambas usan la hora de Europa Central.")]},
    {"slug": "australia", "pais": "Australia (Sídney)", "tz": "Australia/Sydney", "kw": "hora en Australia", "vol": "9.900",
     "texto": "Australia tiene tres husos principales y no todos sus estados cambian la hora. Sídney, Melbourne y Canberra usan UTC+10 y UTC+11 en su horario de verano, que va del primer domingo de octubre al primer domingo de abril; Queensland (Brisbane) no cambia. Con Chile, la diferencia ronda las 13 a 14 horas.",
     "faq": [("¿Cuántas horas de diferencia hay entre Chile y Australia?", "Con Sídney, entre 13 y 14 horas según la época; Australia va por delante."), ("¿Brisbane tiene la misma hora que Sídney?", "En invierno australiano sí; en verano Brisbane queda una hora detrás porque no cambia la hora.")]},
    {"slug": "londres", "pais": "Londres", "tz": "Europe/London", "kw": "hora en Londres", "vol": "9.900",
     "texto": "Londres usa la hora de Greenwich (UTC+0) en invierno y la hora de verano británica (UTC+1) del último domingo de marzo al último domingo de octubre. Es una hora menos que en Madrid y París. Con Santiago, la diferencia va de 3 a 5 horas según la época.",
     "faq": [("¿Cuántas horas de diferencia hay entre Chile y Londres?", "Entre 3 y 5 horas, con Londres por delante."), ("¿Londres tiene la misma hora que España?", "No, va una hora detrás de Madrid todo el año.")]},
    {"slug": "venezuela", "pais": "Venezuela", "tz": "America/Caracas", "kw": "hora en Venezuela", "vol": "9.900",
     "texto": "Venezuela usa UTC-4 todo el año y no cambia la hora, en Caracas, Maracaibo y el resto del país. Durante el horario de invierno de Chile ambos países tienen la misma hora, y en el horario de verano chileno Santiago va una hora adelante.",
     "faq": [("¿Venezuela y Chile tienen la misma hora?", "Sí durante el invierno de Chile. En el verano chileno, Chile va una hora adelante."), ("¿Venezuela cambia la hora?", "No, usa UTC-4 todo el año.")]},
]
for _p in PAISES_PAG:
    _n = _p["pais"].split(" (")[0]
    PAGINAS.insert(-1, {"path": f"/hora-en-{_p['slug']}/", "tpl": "pais.html", "pais": _p,
        "title": f"Hora en {_n} ahora y diferencia horaria con Chile" if len(_n) > 5 else f"Hora en {_n} ahora y la diferencia horaria con Chile",
        "desc": f"Qué hora es en {_n} ahora, en vivo, y cuántas horas de diferencia hay con Chile hoy. Huso horario, horario de verano y equivalencias de hora.",
        "h1": f"Hora en {_n}", "corta": None, "texto": _p["texto"], "faqs": _p["faq"]})


# 404 amigable (Johans 2026-11-26): layout completo, buscador, enlaces más usados, noindex; build.py lo deja en /404.html (ErrorDocument)
PAGINAS.append({"path": "/404/", "tpl": "404.html", "noindex": True, "title": "Página no encontrada | " + MARCA,
    "desc": "La página que buscas no existe o cambió de dirección. Revisa la hora oficial de Chile, el cambio de hora o la diferencia horaria.",
    "h1": "Esta hora no existe en el reloj", "buscar": [[x["h1"], x["path"]] for x in PAGINAS if not x.get("noindex")]})

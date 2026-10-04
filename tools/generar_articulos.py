# -*- coding: utf-8 -*-
"""
Genera: articulo-<slug>.html (x6) y blog.html a partir de tools/articulos_data.py
Uso (desde la raíz del sitio):   python tools/generar_articulos.py
Cada texto lleva data-en="..." con su traducción; js/sitio.js hace el cambio ES/EN.
"""
import os, sys, html as H
sys.path.insert(0, os.path.dirname(__file__))
from articulos_data import ARTICULOS, AUTORA, MESES_ES, MESES_EN

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DOMINIO = "https://gabrielagonzalezvazquez.github.io"
WA = "https://wa.me/525537179626?text="
esc = lambda s: H.escape(s, quote=True)

# ------------------------------------------------------------------ MULTIMEDIA DE INTERNET
PX = "https://cdn.pixabay.com/photo/"
PE = "https://images.pexels.com/photos/"
MEDIA = {
 "ai-governance-mexico": dict(
    thumb=PX+"2020/11/20/05/45/artificial-intelligence-5760547_1280.jpg",
    hero=PX+"2020/11/20/05/45/artificial-intelligence-5760547_1280.jpg",
    youtube="OaND_omLEng",
    hero_cap=("Inteligencia Artificial y regulación: el reto de gobernar los sistemas que ya operan en la empresa.",
              "Artificial Intelligence and regulation: the challenge of governing the systems already running inside the company."),
    cap=("Video: guía del AI Act de la Unión Europea y su enfoque basado en riesgo.",
         "Video: guide to the EU AI Act and its risk-based approach.")),
 "lfpdppp-vs-gdpr": dict(
    thumb=PX+"2024/12/22/07/35/data-protection-9283905_1280.png",
    hero=PX+"2024/12/22/07/35/data-protection-9283905_1280.png", contain=True,
    imgs=[PX+"2014/04/03/00/32/padlock-308589_1280.png"],
    hero_cap=("Protección de datos personales: un mismo principio, dos marcos jurídicos.",
              "Personal data protection: one principle, two legal frameworks."),
    cap=("La seguridad y la privacidad se diseñan desde el producto.",
         "Security and privacy are designed into the product.")),
 "gobernanza-startups": dict(
    thumb=PE+"933964/pexels-photo-933964.jpeg?auto=compress&cs=tinysrgb&w=1280",
    hero=PE+"933964/pexels-photo-933964.jpeg?auto=compress&cs=tinysrgb&w=1600",
    imgs=[PE+"7097/people-coffee-tea-meeting.jpg?auto=compress&w=1000",
          PE+"7096/people-woman-coffee-meeting.jpg?auto=compress&w=1000",
          PE+"7093/coffee-desk-notes-workspace.jpg?auto=compress&w=1000"],
    hero_cap=("Equipos fundadores: gobernar con reglas claras desde las primeras decisiones.",
              "Founding teams: governing with clear rules from the very first decisions."),
    cap=("Reuniones de socios, actas y acuerdos claros: la base de una startup lista para invertir.",
         "Partner meetings, minutes and clear agreements: the foundation of an investment-ready startup.")),
 "propiedad-intelectual-digital": dict(
    thumb=PX+"2017/04/10/07/57/processor-2217771_1280.jpg",
    hero=PX+"2017/04/10/07/57/processor-2217771_1280.jpg",
    imgs=[PX+"2016/09/09/20/44/robot-1658023_1280.jpg"],
    hero_cap=("Software, algoritmos y modelos de IA: activos intangibles que conviene proteger.",
              "Software, algorithms and AI models: intangible assets worth protecting."),
    cap=("Los modelos de IA y el código también son propiedad intelectual.",
         "AI models and code are also intellectual property.")),
 "compliance-ventaja-competitiva": dict(
    thumb=PX+"2017/09/05/12/20/business-2717427_1280.jpg",
    hero=PX+"2017/09/05/12/20/business-2717427_1280.jpg",
    imgs=[PX+"2014/08/02/11/21/contract-408216_1280.jpg"],
    hero_cap=("Compliance: cumplir bien también abre puertas comerciales.",
              "Compliance: doing it right also opens commercial doors."),
    cap=("Un programa de cumplimiento sólido genera confianza ante clientes, aliados e inversionistas.",
         "A solid compliance program builds trust with clients, partners and investors.")),
 "contratos-internacionales": dict(
    thumb=PX+"2018/01/23/03/48/conclusion-of-the-contract-3100579_1280.jpg",
    hero=PX+"2018/01/23/03/48/conclusion-of-the-contract-3100579_1280.jpg",
    imgs=[PX+"2018/01/19/07/58/shaking-hands-3091908_1280.jpg",
          PX+"2019/02/21/14/09/handshake-4011419_1280.jpg",
          PX+"2018/08/30/08/56/shaking-hands-3641642_1280.jpg"],
    hero_cap=("Contratos internacionales: claridad en jurisdicción, idioma y ley aplicable.",
              "International contracts: clarity on jurisdiction, language and governing law."),
    cap=("Negociar con claridad evita disputas entre sistemas jurídicos distintos.",
         "Negotiating clearly prevents disputes between different legal systems.")),
}

def T(es, en, tag="span", cls="", extra=""):
    c = f' class="{cls}"' if cls else ""
    return f'<{tag}{c} {extra} data-en="{esc(en)}">{es}</{tag}>'.replace("  ", " ")

def fecha_corta(f):  # 13 Ene 2026
    y, m, d = f
    return (f"{d:02d} {MESES_ES[m][:3].capitalize()} {y}", f"{MESES_EN[m][:3]} {d}, {y}")
def fecha_larga(f):
    y, m, d = f
    return (f"{d} de {MESES_ES[m]} de {y}", f"{MESES_EN[m]} {d}, {y}")
def mins(a): return (f"{a['mins']} min de lectura", f"{a['mins']} min read")

def autor_img(cls="", alt=True):
    return (f'<img {("class="+chr(34)+cls+chr(34)) if cls else ""} src="{AUTORA["foto"]}" alt="{AUTORA["nombre"]}" '
            f'onerror="this.onerror=null;this.src=\'{AUTORA["foto_respaldo"]}\'">')

def media_tag(kind, src):
    if kind == "img":   return f'<img class="ph-media" src="{src}" alt="" loading="lazy" referrerpolicy="no-referrer">'
    if kind == "video": return f'<video class="ph-media" src="{src}" controls preload="metadata" playsinline></video>'
    if kind == "audio": return f'<audio class="ph-media" src="{src}" controls preload="none"></audio>'

def ph(kind, label, hint, src, css="ph-16x9", icon="fa-regular fa-image", mkind="img"):
    """Placeholder multimedia. Si existe el archivo `src`, se muestra solo. Si no, se ve el placeholder."""
    return (f'<div class="ph {css}">{media_tag(mkind, src)}'
            f'<span class="ph-ico"><i class="{icon}"></i></span>'
            f'<span class="ph-label" data-en="{esc(label[1])}">{label[0]}</span>'
            f'<span class="ph-hint" data-en="{esc(hint[1])}">{hint[0]}</span></div>')

def thumb(a):
    return (f'<a class="ph ph-thumb" href="articulo-{a["slug"]}.html" aria-label="{esc(a["titulo"][0])}" data-en-aria-label="{esc(a["titulo"][1])}">'
            f'{media_tag("img", MEDIA[a["slug"]]["thumb"])}'
            f'<span class="ph-ico"><i class="fa-regular fa-image"></i></span>'
            f'<span class="ph-label" data-en="Cover image">Imagen de portada</span></a>')

def cat_html(a):
    return f'<div class="blog-categoria"><i class="fa-solid {a["icon"]}"></i> {T(a["cat"][0], a["cat"][1])}</div>'

def card(a, fade=False):
    f = fecha_corta(a["fecha"]); m = (f'{a["mins"]} min lectura', f'{a["mins"]} min read')
    return f'''<article class="blog-card{' fade-in' if fade else ''}" data-cat="{a["slug"]}" data-catname="{esc(a["cat"][0])}">
                {thumb(a)}
                <div class="blog-body">
                    {cat_html(a)}
                    <h4>{T(a["titulo"][0], a["titulo"][1], "span")}</h4>
                    <p>{T(a["deck"][0], a["deck"][1], "span")}</p>
                    <div class="blog-by">{autor_img()} <span>{AUTORA["nombre"]}</span></div>
                    <div class="blog-meta">
                        <span><i class="fa-regular fa-calendar"></i> {T(f[0], f[1])}</span>
                        <span><i class="fa-regular fa-clock"></i> {T(m[0], m[1])}</span>
                    </div>
                    <a href="articulo-{a["slug"]}.html" class="blog-link">{T("Leer artículo", "Read article")} <i class="fa-solid fa-arrow-right"></i></a>
                </div>
            </article>'''

NAV_LANG = '<button class="lang-btn" id="lang-toggle" type="button" aria-label="Cambiar idioma / Change language"><i class="fa-solid fa-globe"></i><span>EN</span></button>'

def head(titulo, desc, path, extra=""):
    t_es, t_en = titulo; d_es, d_en = desc
    return f'''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title data-en="{esc(t_en)}">{t_es}</title>
    <meta name="description" content="{esc(d_es)}" data-en-content="{esc(d_en)}">
    <meta name="author" content="{AUTORA["nombre"]}">
    <meta property="og:type" content="article">
    <meta property="og:url" content="{DOMINIO}/{path}">
    <meta property="og:title" content="{esc(t_es)}">
    <meta property="og:description" content="{esc(d_es)}">
    <meta property="og:image" content="{DOMINIO}/assets/foto-sobre-mi.jpg">
    <meta name="twitter:card" content="summary_large_image">
    <link rel="canonical" href="{DOMINIO}/{path}">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;0,8..60,700;1,8..60,400;1,8..60,600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="css/styles.css">
    <link rel="stylesheet" href="css/negocios.css">{extra}
</head>
<body>
'''

def footer(links):
    return f'''
    <footer>
        <p>{T("© 2026 Gabriela L. González Vázquez. Todos los derechos reservados.", "© 2026 Gabriela L. González Vázquez. All rights reserved.")}</p>
        <p>{links}</p>
    </footer>
    <script src="js/sitio.js"></script>
</body>
</html>
'''
FOOT_LINKS = (f'<a href="privacidad.html">{T("Aviso de Privacidad", "Privacy Notice")}</a> | '
              f'<a href="index.html">{T("Inicio", "Home")}</a> | <a href="blog.html">{T("Perspectivas", "Insights")}</a>')

# ------------------------------------------------------------------ ARTÍCULO
def render_blocks(a, lang_i):
    es, en = a["es"], a["en"]
    assert [b[0] for b in es] == [b[0] for b in en], a["slug"]
    out = []
    for (t, ves), (_, ven) in zip(es, en):
        if t == "h2":    out.append(f'<h2 {"data-en=" + chr(34) + esc(ven) + chr(34)}>{ves}</h2>')
        elif t == "p":   out.append(f'<p data-en="{esc(ven)}">{ves}</p>')
        elif t == "ul":  out.append("<ul>" + "".join(f'<li data-en="{esc(y)}">{x}</li>' for x, y in zip(ves, ven)) + "</ul>")
        elif t == "quote": out.append(f'<blockquote class="pull" data-en="{esc(ven)}">{ves}</blockquote>')
        elif t == "media": out.append(media_block(a, ves))
    return "\n            ".join(out)

def media_block(a, kind):
    m = MEDIA[a["slug"]]; cap = m["cap"]; imgs = m.get("imgs", [])
    if kind == "video" and m.get("youtube"):
        body = (f'<div class="video-embed"><iframe src="https://www.youtube-nocookie.com/embed/{m["youtube"]}" title="{esc(cap[0])}" '
                f'loading="lazy" allow="accelerometer; encrypted-media; picture-in-picture; fullscreen" allowfullscreen referrerpolicy="strict-origin-when-cross-origin"></iframe></div>')
    elif kind == "galeria":
        body = '<div class="galeria">' + "".join(
            f'<div class="ph ph-4x3">{media_tag("img", u)}<span class="ph-ico"><i class="fa-regular fa-image"></i></span></div>' for u in imgs[:3]) + "</div>"
    else:   # infografía o video sin enlace: imagen relacionada
        cont = " contain" if kind == "infografia" and m.get("contain") else ""
        body = f'<div class="ph ph-16x9{cont}">{media_tag("img", imgs[0])}<span class="ph-ico"><i class="fa-regular fa-image"></i></span></div>'
    return f'<figure>{body}<figcaption data-en="{esc(cap[1])}">{cap[0]}</figcaption></figure>'

def build_article(a):
    s = a["slug"]; f = fecha_larga(a["fecha"]); m = mins(a)
    others = [x for x in ARTICULOS if x is not a]
    i = ARTICULOS.index(a)
    rel = [ARTICULOS[(i + k) % len(ARTICULOS)] for k in (1, 2, 3)]
    wa_text = (f"Hola Gabriela, leí tu artículo «{a['titulo'][0]}» y me gustaría asesoría.",
               f"Hello Gabriela, I read your article “{a['titulo'][1]}” and I would like some advice.")
    from urllib.parse import quote
    wa_es, wa_en = WA + quote(wa_text[0]), WA + quote(wa_text[1])
    ld = (f'\n    <script type="application/ld+json">{{"@context":"https://schema.org","@type":"Article","headline":"{a["titulo"][0]}",'
          f'"datePublished":"{a["fecha"][0]}-{a["fecha"][1]:02d}-{a["fecha"][2]:02d}","author":{{"@type":"Person","name":"{AUTORA["nombre"]}"}},'
          f'"inLanguage":"es","mainEntityOfPage":"{DOMINIO}/articulo-{s}.html"}}</script>')
    out = head(a["titulo"], a["deck"], f"articulo-{s}.html", ld)
    out += f'''    <div class="progreso" id="progreso"></div>
    <nav class="navbar">
        <a href="index.html">{T("Inicio", "Home")}</a>
        <a href="blog.html">{T("Perspectivas", "Insights")}</a>
        <a href="index.html#contacto">{T("Contacto", "Contact")}</a>
        {NAV_LANG}
    </nav>

    <main class="art-wrap">
        <header class="art-head">
            <a href="blog.html" class="volver"><i class="fa-solid fa-arrow-left"></i> {T("Volver a Perspectivas", "Back to Insights")}</a>
            <div class="art-kicker">{cat_html(a)}<span class="borrador" data-en="Draft">Borrador</span></div>
            <h1 data-en="{esc(a["titulo"][1])}">{a["titulo"][0]}</h1>
            <p class="deck" data-en="{esc(a["deck"][1])}">{a["deck"][0]}</p>
            <div class="art-by">
                <div class="who">
                    {autor_img()}
                    <div>
                        <strong>{AUTORA["nombre"]}</strong>
                        <span>{T(AUTORA["rol"][0], AUTORA["rol"][1])} · {T(f[0], f[1])} · {T(m[0], m[1])}</span>
                    </div>
                </div>
                <div class="share" aria-label="Compartir" data-en-aria-label="Share">
                    <a id="sh-li" href="#" target="_blank" rel="noopener" aria-label="LinkedIn"><i class="fa-brands fa-linkedin-in"></i></a>
                    <a id="sh-wa" href="#" target="_blank" rel="noopener" aria-label="WhatsApp"><i class="fa-brands fa-whatsapp"></i></a>
                    <button id="sh-copy" type="button" aria-label="Copiar enlace" data-en-aria-label="Copy link"><i class="fa-solid fa-link"></i></button>
                </div>
            </div>
        </header>

        <div class="art-audio">
            <div class="ph ph-audio">{media_tag("audio", f"assets/articulos/{s}.mp3")}
                <span class="ph-ico"><i class="fa-solid fa-play"></i></span>
                <span><span class="t" data-en="Listen to this article">Escucha este artículo</span><br><span class="d">{a["mins"]} min · <span data-en="Audio placeholder">Audio (placeholder)</span></span></span>
                <span class="bars" aria-hidden="true">{"".join("<span></span>" for _ in range(28))}</span>
            </div>
        </div>

        <figure class="art-hero">
            <div class="ph ph-16x9{" contain" if MEDIA[s].get("contain") else ""}">{media_tag("img", MEDIA[s]["hero"])}<span class="ph-ico"><i class="fa-regular fa-image"></i></span></div>
            <figcaption data-en="{esc(MEDIA[s]["hero_cap"][1])}">{MEDIA[s]["hero_cap"][0]}</figcaption>
        </figure>

        <div class="art-body">
            <aside class="esencial">
                <h3 data-en="Key takeaways">Lo esencial</h3>
                <ul>{"".join(f'<li data-en="{esc(y)}">{x}</li>' for x, y in zip(a["esencial"][0], a["esencial"][1]))}</ul>
            </aside>
            {render_blocks(a, 0)}
        </div>

        <section class="autora-card">
            {autor_img()}
            <div>
                <small data-en="About the author">Sobre la autora</small>
                <h3>{AUTORA["nombre"]}</h3>
                <p data-en="{esc(AUTORA["bio"][1])}">{AUTORA["bio"][0]}</p>
            </div>
        </section>

        <section class="art-cta">
            <h3 data-en="Need advice on this topic?">¿Necesitas asesoría en este tema?</h3>
            <p data-en="Let’s schedule an initial consultation to assess where your organization stands.">Agendemos una consulta inicial para evaluar el estado actual de tu organización.</p>
            <a href="{wa_es}" data-en-href="{wa_en}" target="_blank" rel="noopener" class="btn-whatsapp"><i class="fa-brands fa-whatsapp"></i> {T("Contactar por WhatsApp", "Contact via WhatsApp")}</a>
        </section>

        <section class="relacionados">
            <h3 data-en="You may also like">También te puede interesar</h3>
            <div class="blog-grid">
                {"".join(card(r) for r in rel)}
            </div>
        </section>
    </main>
'''
    out += footer(FOOT_LINKS)
    open(os.path.join(ROOT, f"articulo-{s}.html"), "w", encoding="utf-8").write(out)

# ------------------------------------------------------------------ BLOG
def build_blog():
    lead = ARTICULOS[0]; rest = ARTICULOS[1:]
    f = fecha_larga(lead["fecha"]); m = mins(lead)
    cats = []
    for a in ARTICULOS:
        if a["cat"] not in cats: cats.append(a["cat"])
    chips = f'<button class="on" data-f="*" type="button">{T("Todos", "All")}</button>' + "".join(
        f'<button data-f="{esc(c[0])}" type="button">{T(c[0], c[1])}</button>' for c in cats)
    out = head(("Perspectivas — Gabriela L. González Vázquez", "Insights — Gabriela L. González Vázquez"),
               ("Análisis, guías y reflexiones sobre gobernanza corporativa, AI Governance, compliance y protección de datos.",
                "Analysis, guides and reflections on corporate governance, AI governance, compliance and data protection."), "blog.html")
    out = out.replace('og:type" content="article"', 'og:type" content="website"')
    out += f'''    <nav class="navbar">
        <a href="index.html">{T("Inicio", "Home")}</a>
        <a href="index.html#sobre-mi">{T("Sobre mí", "About me")}</a>
        <a href="index.html#experiencia">{T("Experiencia", "Experience")}</a>
        <a href="blog.html">{T("Perspectivas", "Insights")}</a>
        <a href="index.html#contacto">{T("Contacto", "Contact")}</a>
        {NAV_LANG}
    </nav>

    <header class="masthead">
        <div class="mast-top">{T("Blog Legal", "Legal Blog")}</div>
        <h1>{T("Perspectivas", "Insights")}</h1>
        <p>{T("Análisis, guías y reflexiones sobre gobernanza corporativa, AI Governance, compliance y protección de datos.",
              "Analysis, guides and reflections on corporate governance, AI governance, compliance and data protection.")}</p>
        <div class="mast-rule"></div>
    </header>

    <section class="blog-lista">
        <div class="filtros" id="filtros">{chips}</div>

        <article class="lead-story" id="lead" data-catname="{esc(lead["cat"][0])}">
            <a class="ph ph-16x9" href="articulo-{lead["slug"]}.html" aria-label="{esc(lead["titulo"][0])}" data-en-aria-label="{esc(lead["titulo"][1])}">
                {media_tag("img", MEDIA[lead["slug"]]["thumb"])}
                <span class="ph-ico"><i class="fa-regular fa-image"></i></span>
                <span class="ph-label" data-en="Featured image">Imagen destacada</span>
            </a>
            <div>
                {cat_html(lead)}
                <h2><a href="articulo-{lead["slug"]}.html" style="color:inherit;text-decoration:none">{T(lead["titulo"][0], lead["titulo"][1])}</a></h2>
                <p class="deck">{T(lead["deck"][0], lead["deck"][1])}</p>
                <div class="byline">{autor_img()} <b>{AUTORA["nombre"]}</b><span class="dot">•</span>{T(f[0], f[1])}<span class="dot">•</span>{T(m[0], m[1])}</div>
            </div>
        </article>

        <div class="blog-grid" id="grid">
            {"".join(card(a) for a in rest)}
        </div>
    </section>
'''
    out += footer(f'<a href="privacidad.html">{T("Aviso de Privacidad", "Privacy Notice")}</a> | <a href="index.html">{T("Inicio", "Home")}</a>')
    open(os.path.join(ROOT, "blog.html"), "w", encoding="utf-8").write(out)

if __name__ == "__main__":
    for a in ARTICULOS: build_article(a)
    build_blog()
    # el antiguo articulo.html pasa a redirigir al primer artículo (no rompe enlaces viejos)
    open(os.path.join(ROOT, "articulo.html"), "w", encoding="utf-8").write(
        f'<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><meta http-equiv="refresh" content="0; url=articulo-{ARTICULOS[0]["slug"]}.html">'
        f'<link rel="canonical" href="{DOMINIO}/articulo-{ARTICULOS[0]["slug"]}.html"><title>Perspectivas</title></head>'
        f'<body><a href="articulo-{ARTICULOS[0]["slug"]}.html">Ir al artículo</a></body></html>')
    print("OK:", len(ARTICULOS), "artículos + blog.html")

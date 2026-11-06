# -*- coding: utf-8 -*-
"""
Genera: articulo-<slug>.html (x6), blog.html y articulo.html (redirección)
a partir de tools/articulos_data.py.

Uso (desde la raíz del sitio):   python3 tools/generar_articulos.py

Cada texto lleva data-en="..." con su traducción; js/sitio.js hace el cambio ES/EN.
Estilos: css/site.css (el mismo sistema de diseño que index.html).

Multimedia:
  · Video de YouTube: se define en VIDEOS (slug → id y pie de foto).
  · Audio: si existe assets/articulos/<slug>.mp3, se muestra un reproductor; si no, no aparece nada.
  · Los bloques ('media', 'infografia'|'galeria') no se publican.
"""
import os, sys, html as H
from urllib.parse import quote
sys.path.insert(0, os.path.dirname(__file__))
from articulos_data import ARTICULOS, AUTORA, MESES_ES, MESES_EN

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DOMINIO = "https://gabrielagonzalezvazquez.github.io"
WA = "https://wa.me/525537179626?text="
esc = lambda s: H.escape(s, quote=True)

VIDEOS = {
    "ai-governance-mexico": dict(
        youtube="OaND_omLEng",
        cap=("Video: guía del AI Act de la Unión Europea y su enfoque basado en riesgo.",
             "Video: guide to the EU AI Act and its risk-based approach.")),
}

SVG_WA = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/></svg>')
SVG_LI = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>')
SVG_LINK = ('<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" style="fill:none">'
            '<path d="M10 13a5 5 0 0 0 7.07 0l3-3a5 5 0 0 0-7.07-7.07l-1 1"/><path d="M14 11a5 5 0 0 0-7.07 0l-3 3a5 5 0 0 0 7.07 7.07l1-1"/></svg>')


def T(es, en, tag="span", cls="", extra=""):
    c = f' class="{cls}"' if cls else ""
    x = f" {extra}" if extra else ""
    return f'<{tag}{c}{x} data-en="{esc(en)}">{es}</{tag}>'

def fecha_corta(f):  # 13 ene 2026
    y, m, d = f
    return (f"{d} {MESES_ES[m][:3]} {y}", f"{MESES_EN[m][:3]} {d}, {y}")
def fecha_larga(f):
    y, m, d = f
    return (f"{d} de {MESES_ES[m]} de {y}", f"{MESES_EN[m]} {d}, {y}")
def iso(f): return f"{f[0]}-{f[1]:02d}-{f[2]:02d}"

def autor_img(size=40):
    return f'<img src="{AUTORA["foto"]}" width="{size}" height="{size}" alt="" loading="lazy">'

# ------------------------------------------------------------------ PIEZAS COMUNES
def head(titulo, desc, path, og_type="article", extra=""):
    t_es, t_en = titulo; d_es, d_en = desc
    return f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title data-en="{esc(t_en)}">{t_es}</title>
<meta name="description" content="{esc(d_es)}" data-en-content="{esc(d_en)}">
<meta name="author" content="{AUTORA["nombre"]}">
<meta name="theme-color" content="#F5F2EC">
<link rel="canonical" href="{DOMINIO}/{path}">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<meta property="og:type" content="{og_type}">
<meta property="og:url" content="{DOMINIO}/{path}">
<meta property="og:title" content="{esc(t_es)}">
<meta property="og:description" content="{esc(d_es)}">
<meta property="og:image" content="{DOMINIO}/assets/foto-sobre-mi.jpg">
<meta property="og:locale" content="es_MX">
<meta name="twitter:card" content="summary_large_image">
<link rel="preload" href="assets/fonts/newsreader-normal-latin-9.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/ibm-plex-sans-normal-latin-5.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="css/site.css">{extra}
</head>
<body>
<a class="skip" href="#main" data-en="Skip to content">Saltar al contenido</a>
'''

def header(actual=""):
    links = [("index.html#sobre-mi", "Perfil", "About"), ("index.html#servicios", "Áreas", "Practice"),
             ("index.html#experiencia", "Experiencia", "Experience"), ("blog.html", "Perspectivas", "Insights"),
             ("index.html#contacto", "Contacto", "Contact")]
    nav = "\n      ".join(
        f'<a href="{h}"{" aria-current=" + chr(34) + "page" + chr(34) if h == actual else ""} data-en="{esc(en)}">{es}</a>'
        for h, es, en in links)
    lang = '<button class="lang-btn" type="button" aria-label="Switch to English" lang="en">EN</button>'
    return f'''
<header class="top">
  <div class="wrap">
    <a class="brand" href="index.html" aria-label="Gabriela L. González Vázquez — inicio" data-en-aria-label="Gabriela L. González Vázquez — home">
      <b>G. González Vázquez</b><span data-en="Attorney">Abogada</span>
    </a>
    <div class="top-actions">
      {lang}
      <button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav" aria-label="Menú" data-en-aria-label="Menu"><span></span></button>
    </div>
    <nav class="nav" id="nav" aria-label="Principal" data-en-aria-label="Main">
      {nav}
      {lang}
    </nav>
  </div>
</header>
'''

def footer():
    return f'''
<footer class="foot">
  <div class="wrap">
    <p data-en="© 2026 Gabriela L. González Vázquez">© 2026 Gabriela L. González Vázquez</p>
    <nav aria-label="Pie de página" data-en-aria-label="Footer">
      <a href="index.html" data-en="Home">Inicio</a>
      <a href="blog.html" data-en="Insights">Perspectivas</a>
      <a href="privacidad.html" data-en="Privacy notice">Aviso de privacidad</a>
      <a href="aviso-legal.html" data-en="Legal notice">Aviso legal</a>
    </nav>
  </div>
</footer>

<script src="js/sitio.js"></script>
</body>
</html>
'''

def portada(a, eager=False):
    """Portada de la tarjeta: usa assets/articulos/<slug>.jpg si existe; si no, una portada tipográfica."""
    foto = f"assets/articulos/{a['slug']}.jpg"
    if os.path.exists(os.path.join(ROOT, foto)):
        return f'<div class="cover"><img src="{foto}" alt="" {"" if eager else "loading=\"lazy\""}></div>'
    w_es, w_en = a["cat"][0].split()[0], a["cat"][1].split()[0]
    return (f'<div class="cover" aria-hidden="true"><div class="cover-art">'
            f'<small data-en="{esc(a["cat"][1])}">{a["cat"][0]}</small><b data-en="{esc(w_en)}">{w_es}</b></div></div>')

def card(a, reveal=True):
    f = fecha_corta(a["fecha"])
    meta = (f'{f[0]} · {a["mins"]} min', f'{f[1]} · {a["mins"]} min')
    return f'''
      <article class="card{" reveal" if reveal else ""}" data-catname="{esc(a["cat"][0])}">
        {portada(a)}
        <div class="card-body">
          <p class="card-cat" data-en="{esc(a["cat"][1])}">{a["cat"][0]}</p>
          <h3><a href="articulo-{a["slug"]}.html" data-en="{esc(a["titulo"][1])}">{a["titulo"][0]}</a></h3>
          <p data-en="{esc(a["deck"][1])}">{a["deck"][0]}</p>
          <div class="card-meta"><span data-en="{esc(meta[1])}">{meta[0]}</span><span class="go" aria-hidden="true" data-en="Read →">Leer →</span></div>
        </div>
      </article>'''

# ------------------------------------------------------------------ ARTÍCULO
def media_block(a):
    """Video de YouTube con fachada: no se conecta a YouTube hasta que la persona hace clic."""
    v = VIDEOS.get(a["slug"])
    if not v:
        return ""
    cap = v["cap"]
    aviso = ("Al reproducir, el video se carga desde YouTube (Google), que puede guardar cookies. "
             "Consulte el <a href=\"privacidad.html#cookies\">Aviso de Privacidad</a>.",
             "Playing loads the video from YouTube (Google), which may set cookies. "
             "See the <a href=\"privacidad.html#cookies\">Privacy Notice</a>.")
    return (f'<figure><div class="video-embed yt" data-yt="{v["youtube"]}" data-title="{esc(cap[0])}">'
            f'<button type="button" class="yt-play" data-en="&lt;span&gt;Play video&lt;/span&gt;"><span>Reproducir video</span></button>'
            f'<p class="yt-note" data-en="{esc(aviso[1])}">{aviso[0]}</p></div>'
            f'<figcaption data-en="{esc(cap[1])}">{cap[0]}</figcaption></figure>')

def render_blocks(a):
    es, en = a["es"], a["en"]
    assert [b[0] for b in es] == [b[0] for b in en], a["slug"]
    out = []
    for (t, ves), (_, ven) in zip(es, en):
        if t == "h2":      out.append(f'<h2 data-en="{esc(ven)}">{ves}</h2>')
        elif t == "p":     out.append(f'<p data-en="{esc(ven)}">{ves}</p>')
        elif t == "ul":    out.append("<ul>" + "".join(f'<li data-en="{esc(y)}">{x}</li>' for x, y in zip(ves, ven)) + "</ul>")
        elif t == "quote": out.append(f'<blockquote><p data-en="{esc(ven)}">{ves}</p></blockquote>')
        elif t == "media" and ves == "video":
            m = media_block(a)
            if m: out.append(m)
    return "\n        ".join(out)

def audio_block(a):
    src = f"assets/articulos/{a['slug']}.mp3"
    if not os.path.exists(os.path.join(ROOT, src)):
        return ""
    return (f'\n      <figure style="margin-top:24px"><figcaption class="eyebrow" style="margin-bottom:8px" data-en="Listen to this article">Escucha este artículo</figcaption>'
            f'<audio controls preload="none" src="{src}" style="width:100%"></audio></figure>')

def build_article(a):
    s = a["slug"]; f = fecha_larga(a["fecha"])
    i = ARTICULOS.index(a)
    rel = [ARTICULOS[(i + k) % len(ARTICULOS)] for k in (1, 2, 3)]
    wa_text = (f"Hola Gabriela, leí tu artículo «{a['titulo'][0]}» y me gustaría asesoría.",
               f"Hello Gabriela, I read your article “{a['titulo'][1]}” and I would like some advice.")
    wa_es, wa_en = WA + quote(wa_text[0]), WA + quote(wa_text[1])
    ld = ('\n<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article",'
          f'"headline":"{a["titulo"][0]}","description":"{a["deck"][0]}","datePublished":"{iso(a["fecha"])}",'
          f'"author":{{"@type":"Person","name":"{AUTORA["nombre"]}","url":"{DOMINIO}/"}},'
          f'"inLanguage":"es","mainEntityOfPage":"{DOMINIO}/articulo-{s}.html"}}</script>')
    meta = (f'{f[0]} · {a["mins"]} min de lectura', f'{f[1]} · {a["mins"]} min read')

    out = head(a["titulo"], a["deck"], f"articulo-{s}.html", "article", ld)
    out += '<div class="progreso" id="progreso" aria-hidden="true"></div>'
    out += header("blog.html")
    out += f'''
<main id="main">
  <article>
    <div class="wrap">
      <header class="art-head reveal">
        <a href="blog.html" class="volver" data-en="← Back to Insights">← Volver a Perspectivas</a>
        <p class="eyebrow">{T(a["cat"][0], a["cat"][1], "b")}</p>
        <h1 data-en="{esc(a["titulo"][1])}">{a["titulo"][0]}</h1>
        <p class="deck" data-en="{esc(a["deck"][1])}">{a["deck"][0]}</p>
        <div class="art-by">
          <div class="byline">{autor_img()}<div>{AUTORA["nombre"]}<span><time datetime="{iso(a["fecha"])}" data-en="{esc(meta[1])}">{meta[0]}</time></span></div></div>
          <div class="share" role="group" aria-label="Compartir" data-en-aria-label="Share">
            <a id="sh-li" href="https://www.linkedin.com/sharing/share-offsite/?url={quote(DOMINIO + "/articulo-" + s + ".html", safe="")}" target="_blank" rel="noopener" aria-label="Compartir en LinkedIn" data-en-aria-label="Share on LinkedIn">{SVG_LI}</a>
            <a id="sh-wa" href="https://wa.me/?text={quote(DOMINIO + "/articulo-" + s + ".html", safe="")}" target="_blank" rel="noopener" aria-label="Compartir por WhatsApp" data-en-aria-label="Share on WhatsApp">{SVG_WA}</a>
            <button id="sh-copy" type="button" aria-label="Copiar enlace" data-en-aria-label="Copy link">{SVG_LINK}</button>
            <span id="sh-status" class="sr-only" aria-live="polite"></span>
          </div>
        </div>{audio_block(a)}
      </header>

      <div class="art-grid">
        <div class="prose">
        {render_blocks(a)}
        </div>
        <aside class="esencial" aria-labelledby="esencial-t">
          <h2 id="esencial-t" data-en="Key takeaways">Lo esencial</h2>
          <ul>{"".join(f'<li data-en="{esc(y)}">{x}</li>' for x, y in zip(a["esencial"][0], a["esencial"][1]))}</ul>
        </aside>
      </div>

      <section class="autora" aria-label="Sobre la autora" data-en-aria-label="About the author">
        {autor_img(88)}
        <div>
          <p class="eyebrow" data-en="About the author">Sobre la autora</p>
          <h2>{AUTORA["nombre"]}</h2>
          <p data-en="{esc(AUTORA["bio"][1])}">{AUTORA["bio"][0]}</p>
        </div>
      </section>
    </div>
  </article>

  <section class="art-cta band-blue" aria-labelledby="cta-t">
    <div class="wrap">
      <div>
        <h2 id="cta-t" data-en="Need advice on this topic?">¿Necesita asesoría en este tema?</h2>
        <p data-en="Let’s schedule an initial consultation to assess where your organization stands.">Agendemos una consulta inicial para evaluar el estado actual de su organización.</p>
      </div>
      <a href="{wa_es}" data-en-href="{wa_en}" target="_blank" rel="noopener" class="btn btn-white">{SVG_WA}<span data-en="Message on WhatsApp">Escribir por WhatsApp</span></a>
    </div>
  </section>

  <section class="relacionados" aria-labelledby="rel-t">
    <div class="wrap">
      <h2 id="rel-t" data-en="Keep reading">Siga leyendo</h2>
      <div class="cards stagger">{"".join(card(r) for r in rel)}
      </div>
    </div>
  </section>
</main>
'''
    out += footer()
    open(os.path.join(ROOT, f"articulo-{s}.html"), "w", encoding="utf-8").write(out)

# ------------------------------------------------------------------ BLOG
def build_index():
    """Inserta las tres publicaciones más recientes en index.html y el ícono de WhatsApp."""
    p = os.path.join(ROOT, "index.html")
    h = open(p, encoding="utf-8").read()
    ini, fin = "<!--CARDS-->", "<!--/CARDS-->"
    if ini in h:
        a, b = h.index(ini), (h.index(fin) + len(fin) if fin in h else h.index(ini) + len(ini))
        h = h[:a] + ini + "".join(card(x) for x in ARTICULOS[:3]) + "\n" + fin + h[b:]
    h = h.replace('<path d="__WA__"/>', SVG_WA[SVG_WA.index("<path"):SVG_WA.index("</svg>")])
    open(p, "w", encoding="utf-8").write(h)

def build_blog():
    lead, rest = ARTICULOS[0], ARTICULOS[1:]
    f = fecha_larga(lead["fecha"])
    meta = (f'{f[0]} · {lead["mins"]} min de lectura', f'{f[1]} · {lead["mins"]} min read')
    cats = []
    for a in ARTICULOS:
        if a["cat"] not in cats: cats.append(a["cat"])
    chips = f'<button type="button" data-f="*" aria-pressed="true" data-en="All">Todos</button>' + "".join(
        f'<button type="button" data-f="{esc(c[0])}" aria-pressed="false" data-en="{esc(c[1])}">{c[0]}</button>' for c in cats)

    out = head(("Perspectivas — Gabriela L. González Vázquez", "Insights — Gabriela L. González Vázquez"),
               ("Análisis sobre gobernanza corporativa, AI Governance, compliance y protección de datos.",
                "Analysis on corporate governance, AI governance, compliance and data protection."), "blog.html", "website")
    out += header("blog.html")
    out += f'''
<main id="main">
  <div class="wrap blog-wrap">
    <header class="masthead reveal">
      <span class="pill" data-en="Legal analysis">Análisis legal</span>
      <h1 data-en="Insights">Perspectivas</h1>
      <p data-en="Practical analysis on corporate governance, AI governance, compliance and data protection, written for companies that need to decide.">Análisis práctico sobre gobernanza corporativa, AI Governance, compliance y protección de datos, escrito para empresas que necesitan decidir.</p>
    </header>

    <div class="filtros" id="filtros" role="group" aria-label="Filtrar por tema" data-en-aria-label="Filter by topic">{chips}</div>

    <article class="card lead-card reveal" data-catname="{esc(lead["cat"][0])}">
      {portada(lead, True)}
      <div class="card-body">
        <p class="card-cat" data-en="{esc(lead["cat"][1])}">{lead["cat"][0]}</p>
        <h2><a href="articulo-{lead["slug"]}.html" data-en="{esc(lead["titulo"][1])}">{lead["titulo"][0]}</a></h2>
        <p data-en="{esc(lead["deck"][1])}">{lead["deck"][0]}</p>
        <div class="card-meta"><div class="byline">{autor_img()}<div>{AUTORA["nombre"]}<span data-en="{esc(meta[1])}">{meta[0]}</span></div></div><span class="go" aria-hidden="true" data-en="Read →">Leer →</span></div>
      </div>
    </article>

    <div class="cards stagger">{"".join(card(a) for a in rest)}
    </div>
  </div>
</main>
'''
    out += footer()
    open(os.path.join(ROOT, "blog.html"), "w", encoding="utf-8").write(out)

if __name__ == "__main__":
    for a in ARTICULOS: build_article(a)
    build_blog()
    build_index()
    first = ARTICULOS[0]["slug"]
    open(os.path.join(ROOT, "articulo.html"), "w", encoding="utf-8").write(
        f'<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><meta http-equiv="refresh" content="0; url=articulo-{first}.html">'
        f'<link rel="canonical" href="{DOMINIO}/articulo-{first}.html"><title>Perspectivas</title></head>'
        f'<body><a href="articulo-{first}.html">Ir al artículo</a></body></html>')
    print("OK:", len(ARTICULOS), "artículos + blog.html")

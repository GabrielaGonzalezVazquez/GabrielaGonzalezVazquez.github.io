# -*- coding: utf-8 -*-
"""
Genera: areas.html, area-<slug>.html (x6), recursos.html, glosario.html,
el contacto guiado de index.html, sitemap.xml y robots.txt.
Uso (desde la raíz del sitio):   python3 tools/generar_secciones.py
Contenido en tools/secciones_data.py. Estilos en css/site.css. Comportamiento en js/sitio.js.
"""
import os, sys, json, html as H, unicodedata
sys.path.insert(0, os.path.dirname(__file__))
from generar_articulos import head, header, footer, card, ROOT, DOMINIO, SVG_WA
from articulos_data import ARTICULOS, AUTORA
from secciones_data import AREAS, TIPOS, URGENCIAS, GUIAS, QUIZ, GLOSARIO

esc = lambda s: H.escape(s, quote=True)
ART = {a["slug"]: a for a in ARTICULOS}

def T(tag, par, attrs=""):
    a = f" {attrs}" if attrs else ""
    return f'<{tag}{a} data-en="{esc(par[1])}">{par[0]}</{tag}>'

def lista(items, cls="tick-list"):
    return f'<ul class="{cls}">' + "".join(T("li", x) for x in items) + "</ul>"

def guardar(nombre, html):
    open(os.path.join(ROOT, nombre), "w", encoding="utf-8").write(html)

def cta_banda(area_slug=""):
    destino = f"index.html?area={area_slug}#contacto" if area_slug else "index.html#contacto"
    return f'''
  <section class="art-cta band-blue" aria-labelledby="cta-t">
    <div class="wrap">
      <div>
        <h2 id="cta-t" data-en="Shall we review your case?">¿Revisamos su caso?</h2>
        <p data-en="Tell me in three clicks what you need and send the message by WhatsApp or email.">Cuénteme en tres clics qué necesita y envíe el mensaje por WhatsApp o correo.</p>
      </div>
      <a class="btn btn-white" href="{destino}" data-en="Start a consultation">Iniciar una consulta</a>
    </div>
  </section>
'''

# ====================================================================== ÁREAS
def build_areas_index():
    out = head(("Áreas de práctica — Gabriela L. González Vázquez", "Practice areas — Gabriela L. González Vázquez"),
               ("Gobernanza corporativa, AI Governance, compliance, contratos, protección de datos y propiedad intelectual.",
                "Corporate governance, AI governance, compliance, contracts, data protection and intellectual property."), "areas.html", "website")
    out += header("areas.html")
    cards = "".join(f'''
      <article class="area-card reveal">
        <span class="area-n">{a["n"]}</span>
        <h2><a href="area-{a["slug"]}.html" data-en="{esc(a["nombre"][1])}">{a["nombre"][0]}</a></h2>
        {T("p", a["lede"])}
        <span class="go" aria-hidden="true" data-en="View area →">Ver área →</span>
      </article>''' for a in AREAS)
    out += f'''
<main id="main">
  <div class="wrap blog-wrap">
    <header class="masthead reveal">
      <span class="pill" data-en="Practice areas">Áreas de práctica</span>
      <h1 data-en="How I can help">Cómo puedo ayudarle</h1>
      <p data-en="Six specialties for companies that grow, innovate and need certainty: from corporate structure to artificial intelligence.">Seis especialidades para empresas que crecen, innovan y necesitan certeza: desde la estructura corporativa hasta la inteligencia artificial.</p>
    </header>
    <div class="area-grid stagger">{cards}
    </div>
  </div>
{cta_banda()}
</main>
'''
    out += footer()
    guardar("areas.html", out)

def build_area(a):
    i = AREAS.index(a)
    otros = [x for x in AREAS if x is not a]
    art = ART.get(a["art"])
    ld = json.dumps({"@context": "https://schema.org", "@type": "Service", "name": a["nombre"][0], "description": a["lede"][0],
                     "provider": {"@type": "Person", "name": AUTORA["nombre"], "url": DOMINIO + "/"},
                     "areaServed": ["México", "Estados Unidos", "Latinoamérica"], "url": f"{DOMINIO}/area-{a['slug']}.html"}, ensure_ascii=False)
    faq_ld = json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q[0], "acceptedAnswer": {"@type": "Answer", "text": r[0]}} for q, r in a["faq"]]}, ensure_ascii=False)
    out = head((f'{a["nombre"][0]} — Gabriela L. González Vázquez', f'{a["nombre"][1]} — Gabriela L. González Vázquez'),
               a["lede"], f"area-{a['slug']}.html", "website",
               f'\n<script type="application/ld+json">{ld}</script>\n<script type="application/ld+json">{faq_ld}</script>')
    out += header("areas.html")
    entregables = "".join(f'<li class="reveal"><span>{k + 1:02d}</span>{T("p", e)}</li>' for k, e in enumerate(a["entregables"]))
    marco = "".join(T("li", m) for m in a["marco"])
    faq = "".join(f'<details class="reveal"><summary data-en="{esc(q[1])}">{q[0]}</summary><div class="a">{T("p", r)}</div></details>' for q, r in a["faq"])
    otras = "".join(f'<li><a href="area-{x["slug"]}.html"><span>{x["n"]}</span><b data-en="{esc(x["nombre"][1])}">{x["nombre"][0]}</b></a></li>' for x in otros)
    relacionado = f'''
    <section class="section light" aria-labelledby="rel-t">
      <div class="wrap">
        <div class="section-head reveal"><span class="pill" data-en="Further reading">Para profundizar</span><h2 id="rel-t" data-en="Related article">Artículo relacionado</h2></div>
        <div class="cards cards-one">{card(art)}</div>
      </div>
    </section>''' if art else ""
    out += f'''
<main id="main">
  <section class="area-hero band-blue">
    <div class="wrap reveal">
      <a href="areas.html" class="volver" data-en="← All practice areas">← Todas las áreas</a>
      <span class="pill pill-white" data-en="Area {a["n"]}">Área {a["n"]}</span>
      <h1 data-en="{esc(a["nombre"][1])}">{a["nombre"][0]}</h1>
      {T("p", a["lede"], 'class="lede"')}
      <div class="contact-actions" style="justify-content:flex-start">
        <a class="btn btn-white" href="index.html?area={a["slug"]}#contacto" data-en="Ask about this area">Consultar sobre esta área</a>
        <a class="btn btn-line" href="#entregables" data-en="What I deliver">Qué entrego</a>
      </div>
    </div>
  </section>

  <section class="section" aria-labelledby="intro-t">
    <div class="wrap">
      <div class="area-intro reveal">
        <h2 id="intro-t" class="sr-only" data-en="Overview">Resumen</h2>
        {T("p", a["intro"])}
      </div>
      <div class="two-col stagger">
        <div class="reveal"><h3 data-en="Common problems">Problemas frecuentes</h3>{lista(a["problemas"])}</div>
        <div class="reveal"><h3 data-en="Who it is for">Para quién es</h3>{lista(a["para"])}</div>
      </div>
    </div>
  </section>

  <section class="section light" id="entregables" aria-labelledby="ent-t">
    <div class="wrap">
      <div class="section-head reveal"><span class="pill" data-en="Deliverables">Entregables</span><h2 id="ent-t" data-en="What I deliver">Qué entrego</h2></div>
      <ol class="deliverables stagger">{entregables}</ol>
      <div class="marco reveal">
        <h3 data-en="Legal framework">Marco legal de referencia</h3>
        <ul>{marco}</ul>
      </div>
    </div>
  </section>

  <section class="section" aria-labelledby="afaq-t">
    <div class="wrap">
      <div class="section-head reveal"><span class="pill" data-en="Questions">Preguntas</span><h2 id="afaq-t" data-en="Frequently asked questions">Preguntas frecuentes</h2></div>
      <div class="faq stagger">{faq}</div>
    </div>
  </section>
{relacionado}
  <nav class="section other-areas" aria-labelledby="otras-t">
    <div class="wrap">
      <h2 id="otras-t" class="reveal" data-en="Other practice areas">Otras áreas de práctica</h2>
      <ul class="stagger">{otras}</ul>
    </div>
  </nav>
{cta_banda(a["slug"])}
</main>
'''
    out += footer()
    guardar(f"area-{a['slug']}.html", out)

# ====================================================================== CONTACTO GUIADO (index.html)
def radios(nombre, opciones, valores=None):
    out = []
    for k, op in enumerate(opciones):
        v = valores[k] if valores else op[0]
        out.append(f'<label class="opt"><input type="radio" name="{nombre}" value="{esc(v)}"><span data-en="{esc(op[1])}">{op[0]}</span></label>')
    return "".join(out)

def contacto_guiado():
    areas = [a["nombre"] for a in AREAS] + [("Otro tema", "Other topic")]
    slugs = [a["slug"] for a in AREAS] + ["otro"]
    return f'''
    <form class="guided" id="guiado" novalidate>
      <fieldset>
        <legend data-en="1. What do you need help with?">1. ¿En qué necesita apoyo?</legend>
        <div class="opts">{radios("area", areas, slugs)}</div>
      </fieldset>
      <fieldset>
        <legend data-en="2. Your organization is…">2. Su organización es…</legend>
        <div class="opts">{radios("tipo", TIPOS)}</div>
      </fieldset>
      <fieldset>
        <legend data-en="3. When do you need it?">3. ¿Para cuándo lo necesita?</legend>
        <div class="opts">{radios("urgencia", URGENCIAS)}</div>
      </fieldset>
      <div class="fields">
        <label><span data-en="Your name (optional)">Su nombre (opcional)</span><input type="text" name="nombre" autocomplete="name" maxlength="80" spellcheck="false"></label>
        <label><span data-en="Briefly describe your case (optional)">Describa brevemente su caso (opcional)</span><textarea name="detalle" rows="3" maxlength="500" data-en-placeholder="E.g. we are about to close our first round…" placeholder="Ej. estamos por cerrar nuestra primera ronda…"></textarea></label>
      </div>
      <div class="preview">
        <p class="eyebrow" data-en="Your message">Su mensaje</p>
        <p id="guiado-msg" aria-live="polite" data-en="Choose the options above and your message will appear here.">Elija las opciones de arriba y aquí aparecerá su mensaje.</p>
      </div>
      <div class="guided-actions">
        <a class="btn btn-solid" id="guiado-wa" href="https://wa.me/525537179626" target="_blank" rel="noopener">{SVG_WA}<span data-en="Send via WhatsApp">Enviar por WhatsApp</span></a>
        <a class="btn btn-line" id="guiado-mail" href="mailto:ggv@blic.com.mx" data-en="Send via email">Enviar por correo</a>
      </div>
      <p class="guided-note" data-en="Nothing is stored on this site: the message opens in your WhatsApp or email so you can review and send it.">Este sitio no guarda nada: el mensaje se abre en su WhatsApp o correo para que usted lo revise y lo envíe.</p>
    </form>
'''

def inyectar_contacto():
    p = os.path.join(ROOT, "index.html")
    h = open(p, encoding="utf-8").read()
    ini, fin = "<!--GUIADO-->", "<!--/GUIADO-->"
    if ini in h:
        a, b = h.index(ini), h.index(fin) + len(fin)
        h = h[:a] + ini + contacto_guiado() + "    " + fin + h[b:]
        open(p, "w", encoding="utf-8").write(h)

# ====================================================================== RECURSOS
def build_recursos():
    out = head(("Recursos — Gabriela L. González Vázquez", "Resources — Gabriela L. González Vázquez"),
               ("Guías prácticas y una autoevaluación para startups y empresas: AI Governance, protección de datos y rondas de inversión.",
                "Practical guides and a self-assessment for startups and companies: AI governance, data protection and funding rounds."), "recursos.html", "website")
    out += header("recursos.html")
    preguntas = "".join(f'''
          <fieldset class="q">
            <legend><span>{k + 1:02d}</span><span data-en="{esc(q[1])}">{q[0]}</span></legend>
            <div class="opts">
              <label class="opt"><input type="radio" name="q{k}" value="1"><span data-en="Yes">Sí</span></label>
              <label class="opt"><input type="radio" name="q{k}" value="0"><span data-en="No">No</span></label>
              <label class="opt"><input type="radio" name="q{k}" value="0"><span data-en="Not sure">No sé</span></label>
            </div>
          </fieldset>''' for k, q in enumerate(QUIZ["preguntas"]))
    res = "".join(f'<div class="quiz-res" data-min="{m}" hidden><h3 data-en="{esc(t[1])}">{t[0]}</h3>{T("p", d)}</div>' for m, t, d in QUIZ["resultados"])
    guias = "".join(f'''
      <article class="guide-block reveal" id="{g["id"]}">
        <header>
          <div>
            <h3 data-en="{esc(g["titulo"][1])}">{g["titulo"][0]}</h3>
            {T("p", g["desc"])}
          </div>
          <div class="guide-tools">
            <span class="guide-count" aria-live="polite"><b>0</b>/{len(g["items"])}</span>
            <button class="btn btn-line btn-print" type="button" data-guide="{g["id"]}" data-en="Print / save PDF">Imprimir / guardar PDF</button>
          </div>
        </header>
        <ul class="checklist">{"".join(f'<li><label><input type="checkbox"><span data-en="{esc(it[1])}">{it[0]}</span></label></li>' for it in g["items"])}</ul>
      </article>''' for g in GUIAS)
    out += f'''
<main id="main">
  <div class="wrap">
    <header class="masthead reveal">
      <span class="pill" data-en="Resources">Recursos</span>
      <h1 data-en="Practical tools">Herramientas prácticas</h1>
      <p data-en="Guides and a self-assessment to see where your company stands. Everything works in your browser and nothing is sent or stored.">Guías y una autoevaluación para saber dónde está su empresa. Todo funciona en su navegador y no se envía ni se guarda nada.</p>
    </header>
  </div>

  <section class="section light" id="autoevaluacion" aria-labelledby="quiz-t">
    <div class="wrap">
      <form class="quiz reveal" id="quiz" novalidate>
        <div class="quiz-head">
          <span class="pill" data-en="Self-assessment">Autoevaluación</span>
          <h2 id="quiz-t" data-en="{esc(QUIZ["titulo"][1])}">{QUIZ["titulo"][0]}</h2>
          {T("p", QUIZ["desc"])}
          <div class="quiz-bar" aria-hidden="true"><i></i></div>
        </div>
        {preguntas}
        <div class="quiz-out" aria-live="polite">
          <p class="quiz-score" hidden><b>0</b>/8</p>
          {res}
          <p class="quiz-hint" data-en="Answer all eight questions to see your result.">Responda las ocho preguntas para ver su resultado.</p>
          <a class="btn btn-solid quiz-cta" href="index.html?area=gobernanza-corporativa#contacto" hidden data-en="Talk about my case">Hablar sobre mi caso</a>
        </div>
      </form>
    </div>
  </section>

  <section class="section" id="guias" aria-labelledby="guias-t">
    <div class="wrap">
      <div class="section-head reveal">
        <span class="pill" data-en="Guides">Guías</span>
        <h2 id="guias-t" data-en="Checklists you can print">Listas de verificación para imprimir</h2>
        <p data-en="Tick what you already have; print or save as PDF to share with your team.">Marque lo que ya tiene; imprímalas o guárdelas en PDF para compartirlas con su equipo.</p>
      </div>
      <div class="guides">{guias}
      </div>
      <p class="cards-more reveal"><a class="link" href="glosario.html"><span data-en="Need a term explained? Visit the glossary">¿Algún término no le es claro? Consulte el glosario</span> <span class="arr" aria-hidden="true">→</span></a></p>
    </div>
  </section>
{cta_banda()}
</main>
'''
    out += footer()
    guardar("recursos.html", out)

# ====================================================================== GLOSARIO
def ancla(t):
    s = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode().lower()
    return "".join(c if c.isalnum() else "-" for c in s).strip("-").replace("--", "-")

def build_glosario():
    items = sorted(GLOSARIO, key=lambda x: unicodedata.normalize("NFKD", x[0][0]).lower())
    letras = sorted({unicodedata.normalize("NFKD", t[0][0])[0].upper() for t in items})
    ld = json.dumps({"@context": "https://schema.org", "@type": "DefinedTermSet", "name": "Glosario legal",
                     "hasDefinedTerm": [{"@type": "DefinedTerm", "name": t[0], "description": d[0]} for t, d in items]}, ensure_ascii=False)
    out = head(("Glosario legal — Gabriela L. González Vázquez", "Legal glossary — Gabriela L. González Vázquez"),
               ("Términos clave de gobernanza corporativa, compliance, protección de datos, propiedad intelectual e inteligencia artificial.",
                "Key terms in corporate governance, compliance, data protection, intellectual property and artificial intelligence."), "glosario.html", "website",
               f'\n<script type="application/ld+json">{ld}</script>')
    out += header("")
    entradas = "".join(f'''
        <div class="term" id="{ancla(t[0])}" data-letra="{unicodedata.normalize("NFKD", t[0])[0].upper()}">
          <dt data-en="{esc(t[1])}">{t[0]}</dt>
          <dd data-en="{esc(d[1])}">{d[0]}</dd>
        </div>''' for t, d in items)
    out += f'''
<main id="main">
  <div class="wrap blog-wrap">
    <header class="masthead reveal">
      <span class="pill" data-en="Glossary">Glosario</span>
      <h1 data-en="Legal glossary">Glosario legal</h1>
      <p data-en="Plain-language definitions of the terms that come up most in governance, compliance, data and technology.">Definiciones en lenguaje claro de los términos que más aparecen en gobernanza, compliance, datos y tecnología.</p>
    </header>
    <div class="gl-tools reveal">
      <label class="gl-search"><span class="sr-only" data-en="Search the glossary">Buscar en el glosario</span>
        <input type="search" id="gl-q" autocomplete="off" spellcheck="false" data-en-placeholder="Search a term…" placeholder="Buscar un término…"></label>
      <nav class="gl-letters" aria-label="Letras" data-en-aria-label="Letters">{"".join(f'<a href="#letra-{l}">{l}</a>' for l in letras)}</nav>
    </div>
    <p class="gl-empty" id="gl-empty" hidden data-en="No terms match your search.">No hay términos que coincidan con su búsqueda.</p>
    <p class="sr-only" id="gl-status" aria-live="polite"></p>
    <dl class="glossary">{"".join(f'<span id="letra-{l}" class="gl-anchor" aria-hidden="true"></span>' for l in [])}{entradas}
    </dl>
  </div>
{cta_banda()}
</main>
'''
    # anclas de letra: primer término de cada letra
    for l in letras:
        out = out.replace(f'data-letra="{l}">', f'data-letra="{l}"><span id="letra-{l}" class="gl-anchor"></span>', 1)
    out += footer()
    guardar("glosario.html", out)

# ====================================================================== SITEMAP
def build_sitemap():
    paginas = ["", "areas.html"] + [f"area-{a['slug']}.html" for a in AREAS] + ["blog.html"] + \
              [f"articulo-{a['slug']}.html" for a in ARTICULOS] + ["recursos.html", "glosario.html", "privacidad.html", "aviso-legal.html"]
    urls = "".join(f"  <url><loc>{DOMINIO}/{p}</loc></url>\n" for p in paginas)
    guardar("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
    guardar("robots.txt", f"User-agent: *\nAllow: /\nDisallow: /tools/\n\nSitemap: {DOMINIO}/sitemap.xml\n")

if __name__ == "__main__":
    build_areas_index()
    for a in AREAS: build_area(a)
    build_recursos()
    build_glosario()
    inyectar_contacto()
    build_sitemap()
    print("OK: áreas (7), recursos, glosario, contacto guiado, sitemap.xml, robots.txt")

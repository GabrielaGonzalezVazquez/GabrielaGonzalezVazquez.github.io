/* ============================================================
   SITIO.JS — comportamientos nuevos (se carga en todas las páginas)
   1) Cambio de idioma ES / EN   2) Medios que reemplazan placeholders
   3) Slot de video en Áreas     4) Progreso de lectura y compartir
   5) Filtros del blog
   ============================================================ */
(function () {
    'use strict';

    /* ---------- 1. IDIOMA ---------- */
    const KEY = 'idioma-sitio';
    const guardado = () => { try { return localStorage.getItem(KEY); } catch (e) { return null; } };
    const guardar = v => { try { localStorage.setItem(KEY, v); } catch (e) {} };

    function aplicarIdioma(lang) {
        const root = document.documentElement;
        root.lang = lang;

        // Contenido (innerHTML). El original en español se guarda la primera vez.
        document.querySelectorAll('[data-en]').forEach(el => {
            if (el.dataset.es === undefined) el.dataset.es = el.innerHTML;
            el.innerHTML = lang === 'en' ? el.dataset.en : el.dataset.es;
        });

        // Atributos: data-en-alt, data-en-href, data-en-aria-label, data-en-content...
        document.querySelectorAll('*').forEach(el => {
            for (const a of el.attributes) {
                if (!a.name.startsWith('data-en-')) continue;
                const attr = a.name.slice(8);
                const bak = 'data-es-' + attr;
                if (!el.hasAttribute(bak)) el.setAttribute(bak, el.getAttribute(attr) || '');
                el.setAttribute(attr, lang === 'en' ? a.value : el.getAttribute(bak));
            }
        });

        // Frase rotativa del hero: se actualiza al instante
        const rot = document.querySelector('.rotativo-texto');
        if (rot) rot.textContent = lang === 'en' ? 'Corporate Governance' : 'Gobernanza Corporativa';

        document.querySelectorAll('#lang-toggle span').forEach(s => { s.textContent = lang === 'en' ? 'ES' : 'EN'; });
        document.querySelectorAll('#lang-toggle').forEach(b => {
            b.setAttribute('aria-label', lang === 'en' ? 'Cambiar a español' : 'Switch to English');
        });
        guardar(lang);
    }

    const inicial = guardado() === 'en' ? 'en' : 'es';
    if (inicial === 'en') aplicarIdioma('en');

    document.querySelectorAll('#lang-toggle').forEach(btn =>
        btn.addEventListener('click', () => aplicarIdioma(document.documentElement.lang === 'en' ? 'es' : 'en'))
    );

    /* ---------- 2. PLACEHOLDERS ↔ MEDIOS REALES ----------
       Si existe el archivo (imagen / video / audio) se muestra solo, sin tocar el código. */
    document.querySelectorAll('.ph').forEach(box => {
        box.querySelectorAll('.ph-media').forEach(m => {
            const ok = () => box.classList.add('has-media');
            if (m.tagName === 'IMG') {
                if (m.complete && m.naturalWidth) ok();
                m.addEventListener('load', ok);
                m.addEventListener('error', () => m.remove());
            } else {
                m.addEventListener('loadedmetadata', ok);
                if (m.readyState >= 1) ok();
            }
        });
    });

    /* ---------- 3. SLOT DE VIDEO (Áreas de Práctica) ---------- */
    document.querySelectorAll('.video-slot').forEach(slot => {
        const v = slot.querySelector('video');
        if (!v) return;
        const ok = () => { slot.classList.add('has-video'); const p = v.play(); if (p && p.catch) p.catch(() => {}); };
        v.addEventListener('loadeddata', ok);
        if (v.readyState >= 2) ok();
    });

    /* ---------- 4. PROGRESO DE LECTURA + COMPARTIR ---------- */
    const barra = document.getElementById('progreso');
    if (barra) {
        const upd = () => {
            const h = document.documentElement.scrollHeight - window.innerHeight;
            barra.style.width = (h > 0 ? Math.min(100, (window.scrollY / h) * 100) : 0) + '%';
        };
        window.addEventListener('scroll', upd, { passive: true }); upd();
    }
    const url = encodeURIComponent(location.href), titulo = encodeURIComponent(document.title);
    const li = document.getElementById('sh-li'), wa = document.getElementById('sh-wa'), cp = document.getElementById('sh-copy');
    if (li) li.href = 'https://www.linkedin.com/sharing/share-offsite/?url=' + url;
    if (wa) wa.href = 'https://wa.me/?text=' + titulo + '%20' + url;
    if (cp) cp.addEventListener('click', () => {
        const done = () => { const i = cp.querySelector('i'); i.className = 'fa-solid fa-check'; setTimeout(() => (i.className = 'fa-solid fa-link'), 1600); };
        if (navigator.clipboard) navigator.clipboard.writeText(location.href).then(done).catch(() => {}); else done();
    });

    /* ---------- 5. FILTROS DEL BLOG ---------- */
    const filtros = document.getElementById('filtros');
    if (filtros) {
        const items = [...document.querySelectorAll('#lead, #grid .blog-card')];
        filtros.addEventListener('click', e => {
            const b = e.target.closest('button'); if (!b) return;
            filtros.querySelectorAll('button').forEach(x => x.classList.toggle('on', x === b));
            const f = b.dataset.f;
            items.forEach(it => it.classList.toggle('oculto', f !== '*' && it.dataset.catname !== f));
        });
    }
})();

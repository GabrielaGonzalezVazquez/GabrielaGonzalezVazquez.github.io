/* ============================================================
   SITIO.JS — se carga en todas las páginas. Sin dependencias.
   1) Idioma ES / EN        2) Menú móvil y encabezado
   3) Animaciones            4) Lectura y compartir
   5) Filtros de Perspectivas
   Todo el contenido es visible aunque este archivo no cargue,
   y las animaciones se desactivan con "reducir movimiento".
   ============================================================ */
(function () {
    'use strict';
    var doc = document.documentElement;
    var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var animar = !reduce && 'IntersectionObserver' in window && 'requestAnimationFrame' in window;
    if (animar) doc.classList.add('js');

    /* ---------- 1. IDIOMA ---------- */
    var KEY = 'idioma-sitio';
    function leer() { try { return localStorage.getItem(KEY); } catch (e) { return null; } }
    function guardar(v) { try { localStorage.setItem(KEY, v); } catch (e) {} }

    function aplicarIdioma(lang) {
        doc.lang = lang;
        document.querySelectorAll('[data-en]').forEach(function (el) {
            if (el.dataset.es === undefined) el.dataset.es = el.innerHTML;
            el.innerHTML = lang === 'en' ? el.dataset.en : el.dataset.es;
        });
        document.querySelectorAll('*').forEach(function (el) {
            for (var i = 0; i < el.attributes.length; i++) {
                var a = el.attributes[i];
                if (a.name.indexOf('data-en-') !== 0) continue;
                var attr = a.name.slice(8), bak = 'data-es-' + attr;
                if (!el.hasAttribute(bak)) el.setAttribute(bak, el.getAttribute(attr) || '');
                el.setAttribute(attr, lang === 'en' ? a.value : el.getAttribute(bak));
            }
        });
        document.querySelectorAll('.lang-btn').forEach(function (b) {
            b.textContent = lang === 'en' ? 'ES' : 'EN';
            b.setAttribute('aria-label', lang === 'en' ? 'Cambiar a español' : 'Switch to English');
            b.setAttribute('lang', lang === 'en' ? 'es' : 'en');
        });
        guardar(lang);
        document.dispatchEvent(new CustomEvent('idioma'));
    }

    if (leer() === 'en') aplicarIdioma('en');
    document.querySelectorAll('.lang-btn').forEach(function (btn) {
        btn.addEventListener('click', function () { aplicarIdioma(doc.lang === 'en' ? 'es' : 'en'); });
    });

    /* ---------- 2. MENÚ MÓVIL ---------- */
    var top = document.querySelector('.top');
    var menuBtn = document.querySelector('.menu-btn');
    var nav = document.getElementById('nav');
    function cerrarMenu() {
        if (!nav || !menuBtn) return;
        nav.classList.remove('open');
        menuBtn.setAttribute('aria-expanded', 'false');
    }
    if (menuBtn && nav) {
        menuBtn.addEventListener('click', function () {
            var abierto = nav.classList.toggle('open');
            menuBtn.setAttribute('aria-expanded', abierto ? 'true' : 'false');
            if (top) top.classList.remove('hide');
        });
        nav.addEventListener('click', function (e) { if (e.target.closest('a')) cerrarMenu(); });
        document.addEventListener('keydown', function (e) {
            if (e.key === 'Escape' && nav.classList.contains('open')) { cerrarMenu(); menuBtn.focus(); }
        });
    }
    // El encabezado nunca debe tapar un elemento enfocado con el teclado
    document.addEventListener('focusin', function () { if (top) top.classList.remove('hide'); });

    /* ---------- 3. ANIMACIONES ---------- */

    // 3a. Entrada de la portada
    requestAnimationFrame(function () { requestAnimationFrame(function () { doc.classList.add('loaded'); }); });
    var heroFig = document.querySelector('.hero-figure');
    if (heroFig) setTimeout(function () { heroFig.classList.add('settled'); }, 2100);

    // 3b. Aparición al entrar en pantalla
    if (animar) {
        var io = new IntersectionObserver(function (entries) {
            entries.forEach(function (en) {
                if (!en.isIntersecting) return;
                en.target.classList.add('in');
                if (en.target.hasAttribute('data-count')) contar(en.target);
                io.unobserve(en.target);
            });
        }, { rootMargin: '0px 0px -10% 0px', threshold: 0.08 });
        document.querySelectorAll('.reveal, .reveal-img, .draw, [data-count]').forEach(function (el) { io.observe(el); });
    }

    // 3c. Contadores (12+, 20+…)
    function contar(el) {
        var fin = parseInt(el.getAttribute('data-count'), 10), suf = el.getAttribute('data-suffix') || '';
        var t0 = null, dur = 1400;
        function paso(t) {
            if (!t0) t0 = t;
            var k = Math.min(1, (t - t0) / dur), e = 1 - Math.pow(1 - k, 4);
            el.textContent = Math.round(fin * e) + suf;
            if (k < 1) requestAnimationFrame(paso);
        }
        requestAnimationFrame(paso);
    }

    // 3d. Texto que se ilumina palabra por palabra al hacer scroll
    function partir() {
        document.querySelectorAll('[data-words]').forEach(function (el) {
            if (el.querySelector('.w')) return;
            var txt = el.textContent.trim().split(/\s+/);
            el.innerHTML = txt.map(function (w) { return '<span class="w">' + w + '</span>'; }).join(' ');
            el.setAttribute('aria-label', txt.join(' '));
        });
    }
    if (animar) { partir(); document.addEventListener('idioma', function () { partir(); progreso(); }); }

    // 3e. Motor de scroll: escribe --p (0→1) en elementos [data-progress] visibles
    var visibles = new Set();
    var pasos = document.querySelectorAll('.steps li');
    if (animar) {
        var vis = new IntersectionObserver(function (entries) {
            entries.forEach(function (en) {
                if (en.isIntersecting) { visibles.add(en.target); return; }
                visibles.delete(en.target);
                var arriba = en.boundingClientRect.top < 0;
                en.target.style.setProperty('--p', arriba ? '1' : '0');
                en.target.querySelectorAll('.w').forEach(function (w) { w.classList.toggle('lit', arriba); });
            });
            progreso();
        });
        document.querySelectorAll('[data-progress]').forEach(function (el) { vis.observe(el); });
    }

    function progreso() {
        var vh = window.innerHeight;
        visibles.forEach(function (el) {
            var r = el.getBoundingClientRect();
            var modo = el.getAttribute('data-progress');
            var p = modo === 'center'
                ? (vh * 0.85 - r.top) / (r.height * 0.9 + vh * 0.35)
                : (vh - r.top) / (vh + r.height);
            p = Math.max(0, Math.min(1, p));
            el.style.setProperty('--p', p.toFixed(4));
            var ws = el.querySelectorAll('.w');
            if (ws.length) {
                var n = Math.round(p * 1.25 * ws.length);
                ws.forEach(function (w, i) { w.classList.toggle('lit', i < n); });
            }
        });
        if (pasos.length && window.innerWidth > 960) {
            var mejor = 0, dist = Infinity;
            pasos.forEach(function (li, i) {
                var r = li.getBoundingClientRect(), d = Math.abs(r.top + r.height / 2 - vh / 2);
                if (d < dist) { dist = d; mejor = i; }
            });
            pasos.forEach(function (li, i) { li.classList.toggle('active', i === mejor); });
        }
    }

    // 3f. Encabezado: se oculta al bajar y reaparece al subir
    var barra = document.getElementById('progreso');
    var ultimoY = window.scrollY, pendiente = false;
    function alScroll() {
        if (pendiente) return;
        pendiente = true;
        requestAnimationFrame(function () {
            pendiente = false;
            var y = window.scrollY;
            if (top) {
                top.classList.toggle('scrolled', y > 8);
                var abierto = nav && nav.classList.contains('open');
                if (animar && !abierto) top.classList.toggle('hide', y > ultimoY && y > 400);
            }
            ultimoY = y;
            if (barra) {
                var h = doc.scrollHeight - window.innerHeight;
                barra.style.transform = 'scaleX(' + (h > 0 ? Math.min(1, y / h) : 0) + ')';
            }
            if (animar) progreso();
        });
    }
    window.addEventListener('scroll', alScroll, { passive: true });
    window.addEventListener('resize', alScroll, { passive: true });
    alScroll();

    /* ---------- 4. COMPARTIR ---------- */
    var url = encodeURIComponent(location.href), titulo = encodeURIComponent(document.title);
    var li = document.getElementById('sh-li'), wa = document.getElementById('sh-wa'), cp = document.getElementById('sh-copy');
    if (li) li.href = 'https://www.linkedin.com/sharing/share-offsite/?url=' + url;
    if (wa) wa.href = 'https://wa.me/?text=' + titulo + '%20' + url;
    if (cp) cp.addEventListener('click', function () {
        var estado = document.getElementById('sh-status');
        function hecho() {
            cp.classList.add('ok');
            if (estado) estado.textContent = doc.lang === 'en' ? 'Link copied' : 'Enlace copiado';
            setTimeout(function () { cp.classList.remove('ok'); if (estado) estado.textContent = ''; }, 2000);
        }
        if (navigator.clipboard) navigator.clipboard.writeText(location.href).then(hecho).catch(function () {});
    });

    /* ---------- 4b. VIDEO: solo se conecta a YouTube tras un clic ---------- */
    document.querySelectorAll('.yt').forEach(function (box) {
        var btn = box.querySelector('.yt-play'); if (!btn) return;
        btn.addEventListener('click', function () {
            var f = document.createElement('iframe');
            f.src = 'https://www.youtube-nocookie.com/embed/' + box.dataset.yt + '?autoplay=1&rel=0';
            f.title = box.dataset.title || 'Video';
            f.allow = 'accelerometer; autoplay; encrypted-media; picture-in-picture; fullscreen';
            f.allowFullscreen = true;
            f.referrerPolicy = 'strict-origin-when-cross-origin';
            box.innerHTML = ''; box.appendChild(f); f.focus();
        });
    });

    /* ---------- 5. FILTROS DE PERSPECTIVAS ---------- */
    var filtros = document.getElementById('filtros');
    if (filtros) {
        var items = document.querySelectorAll('[data-catname]');
        filtros.addEventListener('click', function (e) {
            var b = e.target.closest('button'); if (!b) return;
            filtros.querySelectorAll('button').forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
            var f = b.dataset.f;
            items.forEach(function (it) {
                var ocultar = f !== '*' && it.dataset.catname !== f;
                it.classList.toggle('oculto', ocultar);
                if (!ocultar) { it.classList.remove('in'); void it.offsetWidth; it.classList.add('in'); }
            });
        });
    }
})();

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
    // tras la entrada, la portada responde al scroll sin retardo
    setTimeout(function () {
        document.querySelectorAll('.hero-card, .hero-media').forEach(function (el) { el.classList.add('settled'); });
    }, 2600);

    // 3b. Aparición al entrar en pantalla
    if (animar) {
        // Las animaciones se repiten al bajar y al subir: al salir por completo de la pantalla
        // el elemento vuelve a su estado inicial y se anima de nuevo cuando reaparece.
        var io = new IntersectionObserver(function (entries) {
            entries.forEach(function (en) {
                var el = en.target;
                if (en.isIntersecting) {
                    if (el.classList.contains('in')) return;
                    el.classList.add('in');
                    if (el.hasAttribute('data-count')) contar(el);
                } else if (!el.matches(':focus-within')) {
                    el.classList.remove('in');
                }
            });
        }, { rootMargin: '0px 0px -8% 0px', threshold: 0 });
        document.querySelectorAll('.reveal, .reveal-img, .t-item, [data-count]').forEach(function (el) { io.observe(el); });
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
            var p = modo === 'center' ? (vh * 0.85 - r.top) / (r.height * 0.9 + vh * 0.35)
                  : modo === 'exit' ? -r.top / r.height
                  : (vh - r.top) / (vh + r.height);
            p = Math.max(0, Math.min(1, p));
            el.style.setProperty('--p', p.toFixed(4));
            var ws = el.querySelectorAll('.w');
            if (ws.length) {
                var n = Math.round(p * 1.25 * ws.length);
                ws.forEach(function (w, i) { w.classList.toggle('lit', i < n); });
            }
        });
        if (pasos.length && window.innerWidth > 1000) {
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
            if (Math.abs(y - ultimoY) > 2) doc.classList.toggle('subiendo', y < ultimoY);
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

    /* ---------- 3g. FRASE ROTATIVA DE LA PORTADA ---------- */
    var rot = document.querySelector('.rotativo span');
    var FRASES = {
        es: ['Gobernanza Corporativa', 'AI Governance', 'Compliance Regulatorio', 'Contratos y Transacciones', 'Protección de Datos', 'Propiedad Intelectual'],
        en: ['Corporate Governance', 'AI Governance', 'Regulatory Compliance', 'Contracts & Transactions', 'Data Protection', 'Intellectual Property']
    };
    var iFrase = 0;
    function frases() { return FRASES[doc.lang === 'en' ? 'en' : 'es']; }
    if (rot) {
        document.addEventListener('idioma', function () { rot.textContent = frases()[iFrase % frases().length]; });
        if (!reduce) setInterval(function () {
            if (document.hidden) return;
            rot.classList.add('out');
            setTimeout(function () {
                iFrase = (iFrase + 1) % frases().length;
                rot.textContent = frases()[iFrase];
                rot.classList.remove('out'); rot.classList.add('pre');
                void rot.offsetWidth;
                rot.classList.remove('pre');
            }, 450);
        }, 2800);
    }

    /* ---------- 3h. VIDEOS: pausa accesible y "reducir movimiento" ---------- */
    document.querySelectorAll('video[data-auto]').forEach(function (v) {
        if (reduce) { v.removeAttribute('autoplay'); v.pause(); }
        else { var pr = v.play(); if (pr && pr.catch) pr.catch(function () {}); }
    });
    var vBtn = document.querySelector('.video-toggle');
    var vHero = document.querySelector('.hero-media video');
    if (vBtn && vHero) {
        function sync() {
            var pausado = vHero.paused;
            vBtn.setAttribute('aria-pressed', pausado ? 'true' : 'false');
            vBtn.setAttribute('aria-label', doc.lang === 'en' ? (pausado ? 'Play video' : 'Pause video') : (pausado ? 'Reproducir video' : 'Pausar video'));
        }
        vBtn.addEventListener('click', function () { if (vHero.paused) vHero.play(); else vHero.pause(); });
        vHero.addEventListener('play', sync); vHero.addEventListener('pause', sync);
        document.addEventListener('idioma', sync); sync();
    }

    /* ---------- 3i. CARRUSEL DE LA UNIVERSIDAD ---------- */
    document.querySelectorAll('.carousel').forEach(function (car) {
        var slides = car.querySelectorAll('.slide'), dots = car.querySelectorAll('.dots button'), cap = car.querySelector('.carousel-ui p');
        var i = 0, timer = null;
        function ir(n) {
            i = (n + slides.length) % slides.length;
            slides.forEach(function (s, k) { s.classList.toggle('active', k === i); s.setAttribute('aria-hidden', k === i ? 'false' : 'true'); });
            dots.forEach(function (d, k) { d.setAttribute('aria-current', k === i ? 'true' : 'false'); });
            if (cap) cap.textContent = slides[i].querySelector('img').alt;
        }
        function reiniciarPunto() { var d = dots[i]; if (!d) return; d.setAttribute('aria-current', 'false'); void d.offsetWidth; d.setAttribute('aria-current', 'true'); }
        function auto() { if (reduce) return; clearInterval(timer); reiniciarPunto(); timer = setInterval(function () { if (!document.hidden) ir(i + 1); }, 5200); }
        dots.forEach(function (d, k) { d.addEventListener('click', function () { ir(k); auto(); }); });
        car.addEventListener('mouseenter', function () { clearInterval(timer); });
        car.addEventListener('mouseleave', auto);
        car.addEventListener('focusin', function () { clearInterval(timer); });
        document.addEventListener('idioma', function () { ir(i); });
        ir(0); auto();
    });

    /* ---------- 3j. CONTACTO GUIADO: arma el mensaje; no envía ni guarda nada ---------- */
    var guiado = document.getElementById('guiado');
    if (guiado) {
        var WA_NUM = '525537179626', CORREO = 'ggv@blic.com.mx';
        var msgEl = document.getElementById('guiado-msg'), btnWa = document.getElementById('guiado-wa'), btnMail = document.getElementById('guiado-mail');
        var vacio = msgEl.innerHTML;
        function elegido(nombre) {
            var r = guiado.querySelector('input[name="' + nombre + '"]:checked');
            return r ? r.parentNode.querySelector('span').textContent.trim() : '';
        }
        function armar() {
            var en = doc.lang === 'en';
            var area = elegido('area'), tipo = elegido('tipo'), urg = elegido('urgencia');
            var nombre = guiado.nombre.value.trim(), detalle = guiado.detalle.value.trim();
            if (!area && !tipo && !urg && !detalle) {
                msgEl.innerHTML = en ? (msgEl.getAttribute('data-en') || vacio) : vacio;
                [btnWa, btnMail].forEach(function (b) { b.setAttribute('aria-disabled', 'true'); });
                return;
            }
            var l = [];
            l.push(en ? 'Hello Gabriela' + (nombre ? ', my name is ' + nombre : '') + '.' : 'Hola Gabriela' + (nombre ? ', soy ' + nombre : '') + '.');
            if (area) l.push(en ? 'I would like advice on: ' + area + '.' : 'Me gustaría asesoría en: ' + area + '.');
            if (tipo) l.push(en ? 'Organization: ' + tipo + '.' : 'Tipo de organización: ' + tipo + '.');
            if (urg) l.push(en ? 'Timing: ' + urg + '.' : 'Plazo: ' + urg + '.');
            if (detalle) l.push((en ? 'Details: ' : 'Detalle: ') + detalle);
            var texto = l.join('\n');
            msgEl.textContent = texto;
            btnWa.href = 'https://wa.me/' + WA_NUM + '?text=' + encodeURIComponent(texto);
            var asunto = (en ? 'Consultation' : 'Consulta') + (area ? ' — ' + area : '');
            btnMail.href = 'mailto:' + CORREO + '?subject=' + encodeURIComponent(asunto) + '&body=' + encodeURIComponent(texto);
            [btnWa, btnMail].forEach(function (b) { b.removeAttribute('aria-disabled'); });
        }
        guiado.addEventListener('input', armar);
        guiado.addEventListener('change', armar);
        guiado.addEventListener('submit', function (e) { e.preventDefault(); });
        document.addEventListener('idioma', armar);
        var pre = new URLSearchParams(location.search).get('area');
        if (pre) { var r = guiado.querySelector('input[name="area"][value="' + pre.replace(/[^a-z-]/g, '') + '"]'); if (r) r.checked = true; }
        armar();
    }

    /* ---------- 3k. AUTOEVALUACIÓN ---------- */
    var quiz = document.getElementById('quiz');
    if (quiz) {
        var nq = quiz.querySelectorAll('.q').length;
        quiz.addEventListener('change', function () {
            var resp = quiz.querySelectorAll('.q input:checked'), total = 0;
            resp.forEach(function (r) { total += +r.value; });
            quiz.querySelector('.quiz-bar').style.setProperty('--q', resp.length / nq);
            var listo = resp.length === nq;
            quiz.querySelector('.quiz-hint').hidden = listo;
            quiz.querySelector('.quiz-cta').hidden = !listo;
            var sc = quiz.querySelector('.quiz-score'); sc.hidden = !listo; sc.querySelector('b').textContent = total;
            var res = quiz.querySelectorAll('.quiz-res'), elegido = null;
            res.forEach(function (x) { if (total >= +x.dataset.min) elegido = x; });
            res.forEach(function (x) { x.hidden = !listo || x !== elegido; });
        });
    }

    /* ---------- 3l. GUÍAS: avance y opción de imprimir solo una ---------- */
    document.querySelectorAll('.guide-block').forEach(function (g) {
        var b = g.querySelector('.guide-count b');
        g.addEventListener('change', function () { b.textContent = g.querySelectorAll('.checklist input:checked').length; });
    });
    document.querySelectorAll('.btn-print').forEach(function (btn) {
        btn.addEventListener('click', function () {
            var g = document.getElementById(btn.dataset.guide);
            document.body.classList.add('print-guide'); g.classList.add('printing');
            window.print();
        });
    });
    window.addEventListener('afterprint', function () {
        document.body.classList.remove('print-guide');
        document.querySelectorAll('.printing').forEach(function (g) { g.classList.remove('printing'); });
    });

    /* ---------- 3m. GLOSARIO: búsqueda ---------- */
    var glq = document.getElementById('gl-q');
    if (glq) {
        var terms = document.querySelectorAll('.term'), vacioGl = document.getElementById('gl-empty'), est = document.getElementById('gl-status');
        var norm = function (t) { return t.normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase(); };
        glq.addEventListener('input', function () {
            var q = norm(glq.value.trim()), n = 0;
            terms.forEach(function (t) { var ok = !q || norm(t.textContent).indexOf(q) > -1; t.classList.toggle('oculto', !ok); if (ok) n++; });
            vacioGl.hidden = n > 0;
            est.textContent = q ? (doc.lang === 'en' ? n + ' terms found' : n + ' términos encontrados') : '';
        });
    }

    /* ---------- 3n. AVISOS LEGALES: índice activo, almacenamiento e impresión ---------- */
    var tocLinks = document.querySelectorAll('.legal-toc a');
    if (tocLinks.length && 'IntersectionObserver' in window) {
        var porId = {};
        tocLinks.forEach(function (a) { porId[a.getAttribute('href').slice(1)] = a; });
        var tocIO = new IntersectionObserver(function (entries) {
            entries.forEach(function (en) {
                if (!en.isIntersecting) return;
                tocLinks.forEach(function (a) { a.removeAttribute('aria-current'); });
                var a = porId[en.target.id]; if (a) a.setAttribute('aria-current', 'true');
            });
        }, { rootMargin: '-30% 0px -60% 0px' });
        document.querySelectorAll('.privacidad-section[id]').forEach(function (s) { tocIO.observe(s); });
    }
    var spEstado = document.getElementById('sp-estado'), spBorrar = document.getElementById('sp-borrar');
    function pintarEstado() {
        if (!spEstado) return;
        var v = leer(), en = doc.lang === 'en';
        spEstado.textContent = v ? (en ? 'Language: ' : 'Idioma: ') + v.toUpperCase() : (en ? 'Nothing' : 'Nada');
        if (spBorrar) spBorrar.disabled = !v;
    }
    if (spBorrar) spBorrar.addEventListener('click', function () {
        try { localStorage.removeItem(KEY); } catch (e) {}
        pintarEstado();
    });
    document.addEventListener('idioma', pintarEstado);
    pintarEstado();
    document.querySelectorAll('.btn-print-page').forEach(function (b) { b.addEventListener('click', function () { window.print(); }); });

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

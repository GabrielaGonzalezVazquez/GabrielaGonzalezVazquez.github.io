/* PORTADA "DE LA IDEA A LA LEY": la cámara avanza por cinco obras al hacer scroll.
   Con "reducir movimiento" se muestra una sola escena fija con el texto. */
(function () {
  'use strict';
  var root = document.documentElement;
  if (!document.querySelector('.story')) return;
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduce) { root.classList.add('story-static'); return; }
  root.classList.add('entra');
  setTimeout(function () { root.classList.remove('entra'); }, 1300);

  var story = document.querySelector('.story');
  if (!story) return;
  var scenes = [].slice.call(document.querySelectorAll('.scene'));
  var imgs = scenes.map(function (s) { return s.querySelector('img'); });
  var texts = [].slice.call(document.querySelectorAll('[data-ch]'));
  var dots = [].slice.call(document.querySelectorAll('.rail-dots span'));
  var cue = document.querySelector('.cue'), line = document.querySelector('.progress-line');
  var N = scenes.length, FADE = 0.2;

  var clamp = function (v, a, b) { return Math.max(a, Math.min(b, v)); };
  var ease = function (t) { return t < .5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2; };
  var smooth = function (a, b, v) { var t = clamp((v - a) / (b - a), 0, 1); return t * t * (3 - 2 * t); };

  function render() {
    var r = story.getBoundingClientRect();
    var total = story.offsetHeight - window.innerHeight;
    var p = clamp(-r.top / total, 0, 1);

    var x = 0.06 + p * (N - 0.06);   // posición en capítulos (0..N)
    scenes.forEach(function (s, i) {
      var t = x - i;                   // tiempo local de la escena
      var last = i === N - 1;
      var op = t < -FADE ? 0 : t < 0 ? (t + FADE) / FADE : (last ? 1 : (t > 1 ? 0 : 1));
      var sc, bl = 0;
      if (last) {                      // la última escena se aleja: plano general
        sc = 1.7 - 0.7 * ease(clamp(t + FADE, 0, 1.2) / 1.2);
      } else if (t < 0) {              // entra desde dentro del objeto anterior
        sc = 1.25 - 0.25 * ((t + FADE) / FADE); bl = 10 * (-t / FADE);
      } else {                         // la cámara avanza hacia el punto focal
        sc = 1 + 1.8 * ease(clamp(t, 0, 1)); bl = t > 0.8 ? (t - 0.8) / 0.2 * 6 : 0;
      }
      s.style.opacity = op.toFixed(3);
      s.style.zIndex = i + 1;
      imgs[i].style.transform = 'scale(' + sc.toFixed(4) + ')';
      imgs[i].style.filter = bl > 0.05 ? 'blur(' + bl.toFixed(2) + 'px)' : 'none';
    });

    texts.forEach(function (el, i) {
      var t = x - i;
      var vis = smooth(0.08, 0.28, t) * (1 - smooth(0.72, 0.92, t));
      if (i === N - 1) vis = smooth(0.08, 0.28, t);
      if (i === 0) vis = 1 - smooth(0.6, 0.85, t);
      var dy = (1 - vis) * 26 * (t < 0.5 ? 1 : -1);
      el.style.opacity = vis.toFixed(3);
      el.style.filter = vis < .98 ? 'blur(' + ((1 - vis) * 8).toFixed(1) + 'px)' : 'none';
      if (i === 0) el.style.transform = 'translate(-50%, calc(-50% + ' + dy.toFixed(1) + 'px)) scale(' + (0.96 + vis * 0.04).toFixed(3) + ')';
      else el.style.transform = 'translateY(' + dy.toFixed(1) + 'px)';
    });

    var activo = clamp(Math.floor(x), 0, N - 1);
    dots.forEach(function (d, i) { d.classList.toggle('on', i === activo); });
    cue.style.opacity = (1 - smooth(0.01, 0.05, p)).toFixed(2);
    line.style.transform = 'scaleX(' + p.toFixed(4) + ')';
  }

  var pend = false;
  function onScroll() { if (pend) return; pend = true; requestAnimationFrame(function () { pend = false; render(); }); }
  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', onScroll, { passive: true });
  render();
})();

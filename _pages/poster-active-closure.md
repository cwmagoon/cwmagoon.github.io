---
title: "Adaptive Closure for Polar Active Fluids — Poster"
excerpt: "Poster: Adaptive Closure for Polar Active Fluids. Connor W. Magoon, David B. Stein, and Scott Weady."
permalink: /posters/active-closure/
sitemap: false
---

<style>
  html, body { margin: 0; height: 100%; background: #f6f8fa; overflow: hidden; }
  .poster-stage {
    position: fixed;
    inset: 0;
    overflow: hidden;
    touch-action: manipulation;
  }
  .poster-stage img {
    position: absolute;
    left: 0;
    top: 0;
    transform-origin: 0 0;
    transition: transform 0.6s cubic-bezier(0.22, 0.61, 0.36, 1);
    box-shadow: 0 6px 30px rgba(0, 0, 0, 0.15);
  }
  .poster-nav {
    position: fixed;
    top: 50%;
    transform: translateY(-50%);
    width: 3rem;
    height: 3rem;
    border: 0;
    border-radius: 50%;
    background: rgba(30, 30, 40, 0.62);
    color: #fff;
    font-size: 2rem;
    line-height: 1;
    padding: 0 0 0.25rem;
    cursor: pointer;
    opacity: 0.85;
    transition: opacity 0.15s, background 0.15s;
    z-index: 2;
  }
  .poster-nav::after { content: ""; position: absolute; inset: -0.8rem; }
  .poster-nav:hover { opacity: 1; background: rgba(30, 30, 40, 0.85); }
  .poster-nav[hidden] { display: none; }
  .poster-prev { left: 0.75rem; }
  .poster-next { right: 0.75rem; }
{% include poster_pan.css %}
  .poster-pan { position: fixed; bottom: 2.4rem; }
  .poster-links {
    position: fixed;
    right: 0.75rem;
    bottom: 0.6rem;
    font: 0.85rem sans-serif;
    z-index: 2;
  }
  .poster-links a {
    color: #333;
    background: rgba(255, 255, 255, 0.85);
    padding: 0.3rem 0.6rem;
    border-radius: 999px;
    text-decoration: none;
    margin-left: 0.3rem;
  }
</style>

<div class="poster-stage" id="poster-stage">
  <img id="poster-img" src="/images/connor_flatiron_2026_poster_preview.jpg" alt="Poster: Adaptive Closure for Polar Active Fluids">
</div>
<button type="button" class="poster-nav poster-prev" id="poster-prev" aria-label="Previous panel" hidden>&#8249;</button>
<button type="button" class="poster-nav poster-next" id="poster-next" aria-label="Next panel">&#8250;</button>
<input type="range" class="poster-pan" id="poster-pan" min="0" max="1000" value="0" aria-label="Pan across panel" hidden>
<div class="poster-links">
  <a href="/images/connor_flatiron_2026_poster.png">Full resolution</a>
  <a href="/">Home</a>
</div>

<script>
{% include poster_panels.js %}

(function () {
  var panels = posterPanels["Confined Polar Active Suspensions"];
  var img = document.getElementById('poster-img');
  var prev = document.getElementById('poster-prev');
  var bar = document.getElementById('poster-pan');
  var stage = document.getElementById('poster-stage');
  var step = -1;
  posterPanSetup(stage, img, bar);

  /* Step -1 fits the whole poster; step i fits panel i, centred in the window */
  function show(next, animate) {
    if (next >= panels.length) next = -1;
    if (next < -1) next = -1;
    step = next;
    prev.hidden = step < 0;
    var VW = window.innerWidth, VH = window.innerHeight;
    var aspect = img.naturalHeight / img.naturalWidth;
    var W = Math.min(VW, VH / aspect), H = W * aspect;
    var p = step < 0 ? [0, 0, 1, 1] : panels[step];
    var fill = step < 0 ? 0.96 : 0.94;
    var sw = fill * VW / (p[2] * W), sh = fill * VH / (p[3] * H);
    var s = Math.min(sw, sh);
    var tx = VW / 2 - (p[0] + p[2] / 2) * s * W;
    stage._pan = null;
    bar.hidden = true;
    if (step >= 0 && posterIsWide(p, aspect)) {
      s = Math.min(sh, 2 * sw);
      stage._pan = posterPanRange(p, s, VW, W);
      tx = stage._pan.left;
    }
    var ty = VH / 2 - (p[1] + p[3] / 2) * s * H;
    if (stage._pan) {
      stage._pan.ty = ty; stage._pan.s = s; stage._pan.f = 0;
      bar.value = 0; bar.hidden = false;
    }
    img.style.transition = animate ? '' : 'none';
    img.style.width = W + 'px';
    img.style.transform = 'translate(' + tx + 'px,' + ty + 'px) scale(' + s + ')';
  }

  function ready() { show(step, false); }
  if (img.complete && img.naturalWidth) ready(); else img.addEventListener('load', ready);
  window.addEventListener('resize', ready);
  prev.addEventListener('click', function () { show(step - 1, true); });
  document.getElementById('poster-next').addEventListener('click', function () { show(step + 1, true); });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'ArrowRight' || e.key === ' ') { e.preventDefault(); show(step + 1, true); }
    if (e.key === 'ArrowLeft') { e.preventDefault(); show(step - 1, true); }
    if (e.key === 'Escape') show(-1, true);
  });
})();
</script>

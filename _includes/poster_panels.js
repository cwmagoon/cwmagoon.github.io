/* Poster panels as fractions of the image [x, y, w, h], in reading order.
   Arrows on the poster zoom to each panel in turn. */
const posterPanels = {
  "dQP: Differentiating Quadratic Programs": [
    [0.013, 0.156, 0.267, 0.296],
    [0.296, 0.156, 0.184, 0.296],
    [0.486, 0.156, 0.498, 0.296],
    [0.013, 0.463, 0.267, 0.294],
    [0.296, 0.463, 0.688, 0.294],
    [0.013, 0.770, 0.971, 0.210]
  ],
  "Confined Polar Active Suspensions": [
    [0.017, 0.136, 0.306, 0.245],
    [0.017, 0.431, 0.306, 0.243],
    [0.017, 0.723, 0.306, 0.245],
    [0.347, 0.136, 0.306, 0.245],
    [0.347, 0.431, 0.306, 0.243],
    [0.347, 0.723, 0.306, 0.245],
    [0.675, 0.136, 0.306, 0.408],
    [0.675, 0.561, 0.306, 0.410]
  ]
};

/* Wide panels on touch screens stay zoomed in instead of shrinking to fit;
   a bar and a sideways finger drag pan across them */
function posterIsWide(p, aspect) {
  var touch = window.matchMedia('(pointer: coarse)').matches || window.innerWidth <= 700;
  return touch && p[2] > 2 * p[3] * aspect;
}

function posterPanSetup(area, img, bar) {
  function apply(f) {
    var q = area._pan;
    if (!q) return;
    q.f = Math.max(0, Math.min(1, f));
    bar.value = q.f * 1000;
    img.style.transition = 'none';
    img.style.transform = 'translate(' + (q.left + (q.right - q.left) * q.f) + 'px,' + q.ty + 'px) scale(' + q.s + ')';
  }
  bar.addEventListener('input', function () { apply(bar.value / 1000); });
  var x0 = null, y0, f0;
  area.addEventListener('touchstart', function (e) {
    if (!area._pan || e.target === bar) return;
    x0 = e.touches[0].clientX; y0 = e.touches[0].clientY; f0 = area._pan.f;
  }, { passive: true });
  area.addEventListener('touchmove', function (e) {
    if (!area._pan || x0 === null) return;
    var dx = e.touches[0].clientX - x0, dy = e.touches[0].clientY - y0;
    if (Math.abs(dx) < Math.abs(dy)) return;
    e.preventDefault();
    apply(f0 + dx / (area._pan.right - area._pan.left));
  }, { passive: false });
  area.addEventListener('touchend', function () { x0 = null; });
}

/* Pan limits for a panel zoomed at scale s in an area of width W (image width W0) */
function posterPanRange(p, s, W, W0) {
  return { left: 0.03 * W - p[0] * s * W0, right: 0.97 * W - (p[0] + p[2]) * s * W0 };
}

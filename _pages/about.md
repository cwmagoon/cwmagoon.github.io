---
permalink: /
excerpt: "Connor Magoon is an Applied Mathematics PhD student at UNC Chapel Hill."
author_profile: false
redirect_from: 
  - /about/
  - /about.html
layout: default
hide_header: true
hide_footer: true
---

<meta name="viewport" content="width=device-width, initial-scale=1">

<!-- Favicon links -->
<link rel="apple-touch-icon" sizes="180x180" href="/images/apple-touch-icon.png">
<link rel="icon" type="image/png" sizes="32x32" href="/images/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/images/favicon-16x16.png">
<link rel="manifest" href="/images/site.webmanifest">

<style>
  * {
    font-family: "Times New Roman", Times, serif !important;
  }

  body {
    margin: 0;
    padding: 0;
  }

  a {
    text-decoration: none;
    color: inherit;
  }

  .main-wrap {
    max-width: 60%;
    margin: 0.25rem auto 1rem auto;
  }

  .section {
    padding: 0.75rem;
    margin: 1rem 0;
    border-radius: 14px;
    background: #f3f3f3;
  }

  .section-header {
    padding: 0.75rem;
    margin: 1rem 0 1.25rem 0;
    border-radius: 14px;
    background: #f0f6ff;
    border-left: 4px solid #004085;
  }

  .section-header a:not(.pill):not(.pill-blue) {
    color: #004085;
    text-decoration: underline;
    text-decoration-color: #99ccff;
    text-underline-offset: 2px;
  }

  .section-header a:not(.pill):not(.pill-blue):hover {
    text-decoration-color: #004085;
  }

  .section h2 {
    font-family: Helvetica, Arial, sans-serif !important;
    font-weight: bold;
    border-left: 4px solid #004085;
    padding-left: 0.6rem;
    margin-top: 0;
  }

  .section h3 {
    font-weight: bold;
    text-align: center;
    }
 

  /* Header */
  .header-grid {
    display: grid;
    grid-template-columns: 1fr auto;
    gap: 1.5rem;
    align-items: start;
  }

  .header-name {
    font-size: 2.1rem;
    margin: 0 0 0.5rem 0;
  }

  .header-photo {
    width: 140px;           /* smaller than the 160px before */
    height: auto;            /* keep aspect ratio */
    border-radius: 10px;     /* restores rounded corners */
    display: block;          /* ensures margin auto works */
    margin-left: auto;       /* horizontal centering in its column */
    margin-right: auto;
    }

  /* Pills */
  .pill-links {
    display: flex;
    flex-wrap: wrap;
    gap: 0.4rem;
    margin-bottom: 0.4rem;
  }

  .pill {
    padding: 0.25rem 0.65rem;
    font-size: 0.8rem;
    border-radius: 999px;
    background: #e6dbff;
    color: #4b2ca3;
    border: 1px solid #d1c2ff;
    display: inline-block;
    transition: background 0.15s, box-shadow 0.15s;
  }

  .pill:hover {
    background: #d4c4ff;
    box-shadow: 0 1px 4px rgba(75,44,163,0.15);
  }

  .pill-blue {
    padding: 0.25rem 0.65rem;
    font-size: 0.8rem;
    border-radius: 999px;
    background: #cce5ff;
    color: #004085;
    border: 1px solid #99ccff;
    display: inline-block;
    transition: background 0.15s, box-shadow 0.15s;
  }

  .pill-blue:hover {
    background: #b3d7ff;
    box-shadow: 0 1px 4px rgba(0,64,133,0.15);
  }

  .email-line {
    font-size: 0.85rem;
  }

  /* Grid */
  .projects-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1.5rem;
  }

  @media (max-width: 1400px) {
    .projects-grid { grid-template-columns: 1fr; }
    .main-wrap { max-width: 80%; }
  }

  @media (max-width: 600px) {
    .main-wrap { max-width: 95%; }
    .header-grid { grid-template-columns: 1fr; }
  }

  .project-card {
    background: #fff;
    border: 1px solid #e0e0e0;
    border-radius: 10px;
    padding: 1rem;
    transition: box-shadow 0.15s;
    container-type: inline-size;
    display: flex;
    flex-direction: column;
  }

  .project-card:hover {
    box-shadow: 0 2px 10px rgba(0,0,0,0.08);
  }

  .project-card h3 {
    font-family: Helvetica, Arial, sans-serif !important;
    font-size: 0.9rem; /* JS will override this dynamically */
    margin: 0 0 0.4rem 0;
    font-weight: bold;
    line-height: 1.3;
    white-space: normal;
    overflow-wrap: break-word;
    overflow: visible;
    text-overflow: clip;
  }

  /* Clickable figures */
  .figure-with-text {
    position: relative;
  }

  .clickable-figure {
    width: 100%;
    border-radius: 6px;
    cursor: pointer;
    transition: opacity 0.15s;
  }

  .clickable-figure:hover {
    opacity: 0.85;
  }

  .figure-text {
    display: none;
  }

  /* Status badges */
  .project-card {
    position: relative;
  }

  .figure-badge {
    position: absolute;
    top: 0;
    right: 0;
    padding: 0.25rem 0.65rem;
    font-size: 0.8rem;
    border-radius: 999px;
    background: #e6dbff;
    color: #4b2ca3;
    border: 1px solid #d1c2ff;
    display: inline-block;
    z-index: 50;
    transform: translate(50%, -50%);
  }

  /* Modal overlay */
  .modal-overlay {
    display: none;
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background: rgba(0,0,0,0.6);
    z-index: 10000;
    justify-content: center;
    align-items: center;
    padding: 2rem;
  }

  .modal-overlay.active {
    display: flex;
  }

  .modal-content {
    background: #fff;
    border-radius: 12px;
    max-width: 600px;
    width: 100%;
    padding: 1.5rem;
    position: relative;
    font-size: 0.9rem;
    line-height: 1.5;
    max-height: 80vh;
    overflow-y: auto;
  }

  .modal-content img {
    width: 100%;
    border-radius: 8px;
    margin-bottom: 1rem;
  }

  .modal-close {
    position: absolute;
    top: 0.5rem;
    right: 0.75rem;
    background: none;
    border: none;
    font-size: 1.4rem;
    cursor: pointer;
    color: #666;
    line-height: 1;
  }

  .modal-close:hover {
    color: #111;
  }

  .authors { font-size: 0.75rem; margin: 0.25rem 0 0 0; }
  .venue, .series-venue { font-size: 0.7rem; font-style: italic; margin: 0; }
  .links { margin-top: auto; padding-top: 0.5rem; }

  .project-card .links.pill-links {
    flex-wrap: nowrap;
    overflow: hidden;
  }

  /* Scale text only when a card is narrower than 260px (window squished) */
  @container (max-width: 260px) {
    .authors,
    .series-authors { font-size: clamp(0.45rem, 4.5cqi, 0.75rem); }
    .venue, .series-venue { font-size: clamp(0.4rem, 4.2cqi, 0.7rem); }
    .pill, .pill-blue {
      font-size: clamp(0.4rem, 4.8cqi, 0.8rem);
      padding: 0.25rem clamp(0.2rem, 3.8cqi, 0.65rem);
      white-space: nowrap;
    }
  }

  .modal-title { font-size: 1.1rem; font-weight: bold; margin: 0 0 0.4rem 0; }
  .modal-authors { font-size: 0.85rem; margin: 0 0 0.2rem 0; color: #444; }
  .modal-venue { font-size: 0.8rem; font-style: italic; margin: 0 0 0.6rem 0; color: #666; }
  .modal-desc { margin-bottom: 0.6rem; }
  .modal-equal { font-size: 0.75rem; font-style: italic; color: #888; margin-top: 0.5rem; }
  .modal-pills { display: flex; flex-wrap: wrap; gap: 0.4rem; margin-top: 0.6rem; }

  /* Series parts copied into the modal lose their flex parent, so lay
     them out as spaced inline blocks (name over its own "Submitted"). */
  .modal-authors .series-part {
    display: inline-block;
    vertical-align: top;
    margin-right: 1.4rem;
  }
  .modal-authors .series-part:last-child { margin-right: 0; }
  .modal-authors .series-part .series-venue { color: #666; }

  /* Three-part series authors grid */
  .series-authors {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 0.05rem 0;
    font-size: 0.75rem;
    margin: 0.25rem 0 0 0;
  }
  .series-authors .label { font-style: normal; }
  #research .series-authors .label { display: none; }

  /* Three-part series: each "Name + Submitted" is one non-breaking block
     that wraps as a whole unit, so names never split mid-phrase. */
  .series-parts {
    display: flex;
    flex-wrap: wrap;
    gap: 0.3rem 1rem;
  }
  .series-part {
    white-space: nowrap;
    line-height: 1.3;
  }
</style>

<div class="modal-overlay" id="desc-modal">
  <div class="modal-content">
    <button class="modal-close" aria-label="Close">&times;</button>
    <img id="modal-img" src="" alt="">
    <p class="modal-title" id="modal-title"></p>
    <p class="modal-authors" id="modal-authors"></p>
    <p class="modal-venue" id="modal-venue"></p>
    <div class="modal-desc" id="modal-text"></div>
    <p class="modal-equal" id="modal-equal" style="display:none;"><sup>*</sup>Equal contribution</p>
    <div class="modal-pills" id="modal-pills"></div>
  </div>
</div>

<script src="/assets/js/modal.js"></script>

<script>
/* Author homepage links — edit URLs here; leave "" to skip linking */
const authorLinks = {
  "Magoon":   "",
  "Liu":      "https://cn.linkedin.com/in/xinyun-liu-8b2632207",
  "Guan":     "https://www.hull.ac.uk/staff-directory/jian-hui-guan",
  "Tamim":    "https://sites.google.com/view/stamim/home",
  "Stone":    "https://stonelab.princeton.edu/index.php?id=people",
  "Sáenz":    "https://www.pml.unc.edu/about-me",
  "Yang":     "https://fengyuyang25.github.io/",
  "Aigerman": "https://noamaig.github.io/",
  "Kovalsky": "https://shaharkov.github.io/",
  "Durey":    "https://www.gla.ac.uk/schools/mathematicsstatistics/staff/matthewdurey/",
  "Camassa":  "https://math.unc.edu/faculty-member/camassa-roberto/"
};

document.addEventListener('DOMContentLoaded', function () {
  const research = document.getElementById('research');
  if (!research) return;

  const targets = research.querySelectorAll('.authors, .series-authors span:not(.label):not(.series-venue)');

  targets.forEach(function (el) {
    let html = el.innerHTML;
    /* Highlight own name in purple, except on ongoing projects */
    const card = el.closest('.project-card');
    const badge = card && card.querySelector('.figure-badge');
    const isOngoing = badge && badge.textContent.trim() === 'Ongoing';
    if (!isOngoing) {
      html = html.replace(/(?<![\wÀ-ɏ])(Magoon)(?![\wÀ-ɏ])/g, '<span style="color:#4b2ca3;font-weight:bold;">$1</span>');
    }
    /* Link other authors */
    Object.entries(authorLinks).forEach(function ([name, url]) {
      if (!url) return;
      const esc = name.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
      const re = new RegExp('(?<![\\wÀ-ɏ])(' + esc + ')(?![\\wÀ-ɏ])', 'g');
      html = html.replace(re, '<a href="' + url + '" target="_blank" style="color:inherit;text-decoration:none;cursor:pointer;">$1</a>');
    });
    el.innerHTML = html;
  });
});
</script>

<div class="main-wrap">







<!-- Header -->
<div class="section-header" style="display:flex; gap:1rem; flex-wrap:wrap;" id="about">

  <!-- Left column: Name + About + Pills -->
  <div style="flex:2; min-width:250px;" id="left-column-wrapper">
    <div style="display:flex; flex-direction:column; gap:1.2rem;" id="left-column">

      <div style="display: flex; align-items: center; flex-wrap: wrap; margin-bottom: 0.5rem;">
      <!-- Name -->
      <h1 style="margin:0; font-size:2rem; font-family: Helvetica, Arial, sans-serif !important;">Connor Magoon</h1>
      </div>

      <!-- About Box -->
      <div style="background:#cce5ff; color:#004085; border-radius:10px; padding:0.6rem 0.8rem; font-size:0.85rem; line-height:1.3; border: 1px solid #99ccff;">
        <p style="margin:0.3rem 0 0.3rem 0;"> I am a fourth-year Applied Mathematics PhD student at <a href="https://math.unc.edu/" target="_blank">UNC Chapel Hill</a>. Previously, I received my BS in physics and applied math. </p>
        I have broad interests, spanning understanding physical phenomena to developing mathematical tools for solving applied problems. One central thread sewn through all my work is geometry: leveraging simple geometry as a means for explanation, and tackling complex geometry which is prevalent in the non-ideal real world. 
        I work on simulations and modeling of fluids in the <a href="https://www.pml.unc.edu/" target="_blank">Physical Mathematics Lab</a> under the direction of <a href="https://www.pml.unc.edu/about-me" target="_blank">Prof. Pedro Sáenz</a>, and in the intersection of optimization, machine learning, and graphics with advisor <a href="https://shaharkov.github.io/" target="_blank">Prof. Shahar Kovalsky</a>.
        <p style="margin:0.3rem 0 0.3rem 0;"> <b>Summer 2026</b>: I am interning as a summer pre-doctoral researcher for the <a href="https://www.simonsfoundation.org/flatiron/" target="_blank">Flatiron Institute</a>, within the <a href="https://users.flatironinstitute.org/~bpm/index.html" target="_blank">biophysical modeling group</a> of the <a href="https://www.simonsfoundation.org/flatiron/center-for-computational-biology/" target="_blank">Center for Computational Biology</a>. </p>
      </div>

      


      <!-- Navigation pills -->
      <div class="pill-links" style="gap:0.5rem;">
        <a class="pill-blue" href="#about">About</a>
        <a class="pill-blue" href="#research">Research</a>
        <a class="pill-blue" href="#code">Code</a>
      </div>
      <!-- Profile & contact pills -->
      <div class="pill-links" style="gap:0.5rem;">
        <a class="pill" href="https://cwmagoon.github.io/files/cv.pdf" target="_blank">CV</a>
        <a class="pill" href="https://scholar.google.com/citations?user=18F4sZMAAAAJ&hl=en" target="_blank">Google Scholar</a>
        <a class="pill" href="https://orcid.org/0009-0009-1890-3279" target="_blank">ORCID</a>
        <a class="pill" href="https://github.com/cwmagoon" target="_blank">GitHub</a>
        <a class="pill" href="https://www.linkedin.com/in/connor-magoon-3189a9384" target="_blank">LinkedIn</a>
        <a class="pill" id="email-pill" style="cursor:pointer;" onclick="(function(el){navigator.clipboard.writeText('connorwm@live.unc.edu').then(function(){var orig=el.textContent;el.textContent='Copied!';setTimeout(function(){el.textContent=orig;},1500);});return false;})(this)">connorwm (at) live.unc.edu</a>
      </div>

    </div>
  </div>

  <!-- Right column: Photo -->
    <div style="flex:1; min-width:120px; display:flex; justify-content:center; align-items:center;">
    <img src="/images/profile.jpeg"
        style="height:280px; width:auto; border-radius:10px; object-fit:cover; box-shadow:0 6px 24px rgba(0,0,0,0.25), 0 2px 6px rgba(0,0,0,0.12);">
    </div>

</div>

















<!-- Research -->
<div class="section" id="research">
<div style="display:flex; align-items:center; gap:1rem; margin-bottom:0.5rem;">
<h2 style="margin-bottom:0;">Research</h2>
<span style="font-style:italic; font-size:0.85rem; white-space:nowrap;">Click figures for project descriptions.</span>
</div>

<div class="projects-grid">

<!-- Galloping Series -->
<div class="project-card">
<h3>Galloping Bubbles: Three-Part Series</h3>
<div class="figure-with-text">
<img src="/images/galloping_laws.png" class="clickable-figure" style="border-radius:0;">
<div class="figure-text">
A deep-dive experimental, numerical, and theoretical follow-up to our initial discovery of galloping bubbles, which are vertically vibrating millimetric-sized bubbles that spontaneously break symmetry and self-propel along a horizontal wall. At their heart is the parametric excitation of symmetrical and asymmetrical shape modes that together generate a non-reciprocal deformation, enabling the bubble to `swim'.
</div>
</div>
<div class="authors series-parts">
  <span class="series-part">Guan et al.<br><span class="series-venue">Submitted</span></span>
  <span class="series-part">Magoon et al.<br><span class="series-venue">Submitted</span></span>
  <span class="series-part">Tamim et al.<br><span class="series-venue">Submitted</span></span>
</div>
<div class="links pill-links">
<span class="pill">Coming soon</span>
</div>
</div>

<!-- dQP -->
<div class="project-card">
<h3>dQP: Differentiating Quadratic Programs</h3>
<div class="figure-with-text">
<img src="/images/dQP_schematic.png" class="clickable-figure" style="border-radius:0;">
<div class="figure-text">
dQP is a modular framework for differentiating the solution to a quadratic programming problem (QP) with respect to its parameters, enabling the seamless integration of QPs into machine learning architectures and bilevel optimization. dQP supports over 15 state-of-the-art QP solvers.
</div>
</div>
<p class="authors">Magoon<sup>*</sup>, Yang<sup>*</sup>, Aigerman, Kovalsky</p>
<p class="venue">NeurIPS (2025)</p>
<div class="links pill-links">
<a class="pill" href="https://papers.nips.cc/paper_files/paper/2025/file/9bd9aa8c2326b67321eb1f5f281ba618-Paper-Conference.pdf" target="_blank">Paper</a>
<a class="pill" href="https://github.com/cwmagoon/dQP" target="_blank">Code</a>
<a class="pill" href="https://neurips.cc/media/PosterPDFs/NeurIPS%202025/119180.png?t=1762316861" target="_blank">Poster</a>
<a class="pill" href="https://neurips.cc/virtual/2025/loc/san-diego/poster/119180" target="_blank">Video</a>
</div>
</div>

<!-- Galloping Bubbles -->
<div class="project-card">
<h3>Galloping Bubbles</h3>
<div class="figure-with-text">
<img src="/images/galloping_bubble.png" class="clickable-figure">
<div class="figure-text">
We discover, rationalize, and apply a fluid instability in which a vertically vibrating millimetric-sized bubble spontaneously breaks symmetry and self-propels along a horizontal wall. Applications include bubble removal, bubble sorting, surface cleaning, and even solving mazes! <br> <br> <b>Awarded an APS DFD Gallery of Fluid Motion Award.</b>
</div>
</div>
<p class="authors">Guan<sup>*</sup>, Tamim<sup>*</sup>, Magoon<sup>*</sup>, Stone, Sáenz</p>
<p class="venue">Nature Communications (2025)</p>
<div class="links pill-links">
<a class="pill" href="https://www.nature.com/articles/s41467-025-56611-5" target="_blank">Paper</a>
<a class="pill" href="https://doi.org/10.1103/fbdh-fnzv" target="_blank">Gallery Paper</a>
<a class="pill" href="https://www.youtube.com/watch?v=gLbRx5nBpEo" target="_blank">Video</a>
</div>
</div>

<!-- Traveling Faraday Waves -->
<div class="project-card">
<h3>Traveling Faraday Waves</h3>
<div class="figure-with-text">
<img src="/images/faraday_waves.png" class="clickable-figure">
<div class="figure-text">
We present a Faraday wave instability where a vertically vibrated annular bath spontaneously breaks symmetry from standing waves into fast traveling waves. <br> <br> <b>Awarded an APS DFD Gallery of Fluid Motion Award.</b>
</div>
</div>
<p class="authors">Guan, Magoon, Durey, Camassa, Sáenz</p>
<p class="venue">Physical Review Fluids (2023)</p>
<div class="links pill-links">
<a class="pill" href="https://journals.aps.org/prfluids/abstract/10.1103/PhysRevFluids.8.110501" target="_blank">Gallery Paper</a>
<a class="pill" href="https://www.youtube.com/watch?v=0d_D6yvXAFo" target="_blank">Video</a>
</div>
</div>

<!-- Collective -->
<div class="project-card">
<h3>Collective Galloping Bubbles</h3>
<div class="figure-with-text">
<img src="/images/collective_bubbles_flow.png" class="clickable-figure">
<div class="figure-text"></div>
</div>
<p class="authors">Magoon, Liu, Guan, Tamim, Stone, Sáenz</p>
<div class="links pill-links">
<span class="pill">Ongoing</span>
</div>
</div>

<!-- Neural Mappings -->
<div class="project-card">
<h3>Neural Mappings</h3>
<div class="figure-with-text">
<img src="/images/ant_mapping.png" class="clickable-figure">
<div class="figure-text"></div>
</div>
<p class="authors">Magoon, Yang, Aigerman, Kovalsky</p>
<div class="links pill-links">
<span class="pill">Ongoing</span>
</div>
</div>




</div>
</div>






<div class="section" id="code">
<div style="display:flex; align-items:center; gap:1rem; margin-bottom:0.5rem;">
<h2 style="margin-bottom:0;">Code</h2>
<span style="font-style:italic; font-size:0.85rem; white-space:nowrap;">Click figures for project repositories.</span>
</div>

<div class="projects-grid">

<!-- dQP -->
<div class="project-card">
<h3>dQP: Differentiating Quadratic Programs</h3>
<div class="figure-with-text">
  <a href="https://github.com/cwmagoon/dQP" target="_blank">
    <img src="/images/dQP_performance.png" class="clickable-figure">
  </a>
</div>

<div style="display: flex; flex-direction: column; gap: 0.4rem; margin-top: 0.5rem; align-items: center;">
  <pre style="
      display: block;
      background: #f6f8fa;
      border: 1px solid #ddd;
      padding: 0.3rem 0.6rem;
      border-radius: 6px;
      font-family: Menlo, Monaco, Consolas, 'Courier New', monospace;
      font-size: 0.85rem;
      margin: 0;
      line-height: 1.2;
      width: fit-content;
  "><code>pip install libdqp</code></pre>
  <div style="font-size:0.8rem; text-align: center;">
    Packaged by <a href="https://pypi.org/project/libdqp/" target="_blank" style="color:#004085; text-decoration:underline; text-decoration-color:#99ccff; text-underline-offset:2px;">PyPI</a>
  </div>
</div>

</div>





</div>
</div>











<script>
(function () {
  function fitCardHeaders() {
    var headers = Array.from(document.querySelectorAll('.project-card h3'));
    if (!headers.length) return;

    headers.forEach(function (h) {
      h.style.whiteSpace = 'nowrap';
      h.style.fontSize = '';
    });

    var sizes = headers.map(function (h) {
      var card = h.closest('.project-card');
      var cs = getComputedStyle(card);
      var available = card.clientWidth
        - parseFloat(cs.paddingLeft)
        - parseFloat(cs.paddingRight);

      /* hi is large so the search can grow the font to fill the card width
         (not just shrink to fit). In multi-column the title overflows well
         below this and shrinks as before; in single-column the wide card lets
         it scale up so the title still stretches the full width. */
      var lo = 6, hi = 200;
      h.style.fontSize = hi + 'px';
      if (h.scrollWidth <= available) return hi;

      while (hi - lo > 0.25) {
        var mid = (lo + hi) / 2;
        h.style.fontSize = mid + 'px';
        if (h.scrollWidth <= available) lo = mid; else hi = mid;
      }
      return lo;
    });

    var uniformSize = Math.min.apply(null, sizes);

    headers.forEach(function (h) {
      h.style.fontSize = uniformSize + 'px';
      h.style.whiteSpace = '';
    });
  }

  var resizeTimer;
  window.addEventListener('resize', function () {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(fitCardHeaders, 120);
  });

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', fitCardHeaders);
  } else {
    fitCardHeaders();
  }
  if (document.fonts && document.fonts.ready) {
    document.fonts.ready.then(fitCardHeaders);
  }
})();
</script>

</div>










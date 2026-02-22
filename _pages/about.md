---
permalink: /
title: 
excerpt: 
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
    max-width: 70%;
    margin: 0.5rem auto 2rem auto;
  }

  .section {
    padding: 1.5rem;
    margin: 2rem 0;
    border-radius: 14px;
    background: #f3f3f3;
  }

  /* .section h2 {
    color: #3a7bbc; 
    font-weight: bold;
    } 
  */

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
  }
  
  .pill-blue {
    padding: 0.25rem 0.65rem;
    font-size: 0.8rem;
    border-radius: 999px;
    background: #cce5ff;   /* light blue background */
    color: #004085;        /* dark blue text */
    border: 1px solid #99ccff;
    display: inline-block;
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

  @media (max-width: 1000px) {
    .projects-grid { grid-template-columns: repeat(2, 1fr); }
    .main-wrap { max-width: 85%; }
  }

  @media (max-width: 600px) {
    .projects-grid { grid-template-columns: 1fr; }
    .main-wrap { max-width: 95%; }
    .header-grid { grid-template-columns: 1fr; }
  }

  .project-card h3 {
    font-size: 0.9rem;
    margin: 0 0 0.2rem 0;
    font-weight: normal;
  }

  /* Click popout system */
  .figure-with-text {
    position: relative;
  }

  .clickable-figure {
    width: 100%;
    border-radius: 6px;
    cursor: pointer;
  }

  .figure-text {
    position: absolute;
    top: 0;
    left: calc(100% + 12px);
    width: min(45vw, 90%);
    max-width: min(45vw, 90%);
    background: #111;
    color: #fff;
    padding: 0.8rem;
    font-size: 0.75rem;
    line-height: 1.4;
    border-radius: 8px;
    display: none;
    z-index: 9999;
  }

  .figure-with-text.active .figure-text {
    display: block;
  }

  @media (max-width: 700px) {
    .figure-text {
      position: static;
      width: 100%;
      max-width: 100%;
      margin-top: 0.5rem;
    }
  }

  .authors { font-size: 0.75rem; margin: 0.25rem 0 0 0; }
  .venue { font-size: 0.7rem; font-style: italic; margin: 0; }
  .links { margin-top: 0.25rem; }
</style>

<script>
document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll('.figure-with-text').forEach(el => {
    const img = el.querySelector('img');
    img.addEventListener('click', e => {
      e.stopPropagation();
      document.querySelectorAll('.figure-with-text.active')
        .forEach(x => { if (x !== el) x.classList.remove('active'); });
      el.classList.toggle('active');
    });
  });

  document.addEventListener('click', () => {
    document.querySelectorAll('.figure-with-text.active')
      .forEach(el => el.classList.remove('active'));
  });
});
</script>

<div class="main-wrap">










<!-- Header -->
<div class="section" style="display:flex; gap:1rem; flex-wrap:wrap;" id="about">

  <!-- Left column: Name + About + Pills -->
  <div style="flex:2; min-width:250px;" id="left-column-wrapper">
    <div style="display:flex; flex-direction:column; gap:0.5rem;" id="left-column">

      <div style="display: flex; align-items: center; flex-wrap: wrap;">
      <!-- Name -->
      <h1 style="margin:0; font-size:2rem;">Connor Magoon</h1>
      </div>

      <!-- About Box -->
      <div style="background:#cce5ff; color:#004085; border-radius:10px; padding:0.6rem 0.8rem; font-size:0.85rem; line-height:1.3; border: 1px solid #99ccff;">
        <p style="margin:0.3rem 0 0.3rem 0;"> I am a third-year Applied Mathematics PhD student at UNC Chapel Hill. Previously, I received my BS in physics and applied math. </p>
        I have broad interests, spanning understanding physical phenomena to developing mathematical tools for solving applied problems. One central thread sewn through all my work is geometry: leveraging simple geometry as a means for explanation, and tackling complex geometry which is prevalent in the non-ideal real world. 
        I work on simulations and modeling of fluids in the <a href="https://www.pml.unc.edu/" target="_blank">Physical Mathematics Lab</a> under the direction of <a href="https://www.pml.unc.edu/about-me" target="_blank">Prof. Pedro Sáenz</a>, and in the intersection of optimization, machine learning, and graphics with advisor <a href="https://shaharkov.github.io/" target="_blank">Prof. Shahar Kovalsky</a>.
      </div>

      


      <!-- Purple Pills -->
      <div class="pill-links" style="flex-wrap:wrap; gap:0.5rem;">
        <a class="pill-blue" href="#about">About</a>
        <a class="pill-blue" href="#research">Research</a>
        <a class="pill-blue" href="#code">Code</a>
        <a class="pill" href="https://cwmagoon.github.io/files/cv.pdf" target="_blank">CV</a>
        <a class="pill" href="https://scholar.google.com/citations?user=18F4sZMAAAAJ&hl=en" target="_blank">Google Scholar</a>
        <a class="pill" href="https://orcid.org/0009-0009-1890-3279" target="_blank">ORCID</a>
        <a class="pill" href="https://github.com/cwmagoon" target="_blank">GitHub</a>
        <a class="pill" href="https://www.linkedin.com/in/connor-magoon-3189a9384" target="_blank">LinkedIn</a>
        <a class="pill">connorwm (at) live.unc.edu</a>
      </div>

    </div>
  </div>

  <!-- Right column: Photo -->
    <div style="flex:1; min-width:120px; display:flex; justify-content:center; align-items:flex-start;">
    <img src="/images/profile.jpeg"
        style="height:280px; width:auto; border-radius:10px;">
    </div>

</div>

<script>
  function matchPhotoHeight() {
    const left = document.getElementById('left-column-wrapper');
    const photo = document.getElementById('profile-photo');
    if(left && photo){
      const leftHeight = left.getBoundingClientRect().height;
      photo.style.height = leftHeight + "px";
      photo.style.width = "auto"; // preserve aspect ratio
    }
  }

  window.addEventListener('load', matchPhotoHeight);
  window.addEventListener('resize', matchPhotoHeight);
</script>































<!-- Research -->
<div class="section" id="research">
<h2 style="margin-top:0;">Research</h2>
<p style="font-style:italic; font-size:0.85rem;">Click figures for project descriptions.</p>

<div class="projects-grid">

<!-- Collective -->
<div class="project-card">
<h3>Collective Galloping Bubbles</h3>
<div class="figure-with-text">
<img src="/images/collective_bubbles_flow.png" class="clickable-figure">
<div class="figure-text">Ongoing work</div>
</div>
<p class="authors">Magoon, Liu, Guan, Tamim, Stone, Sáenz</p>
</div>

<!-- Neural Mappings -->
<div class="project-card">
<h3>Neural Mappings</h3>
<div class="figure-with-text">
<img src="/images/ant_mapping.png" class="clickable-figure">
<div class="figure-text">Ongoing work</div>
</div>
<p class="authors">Magoon, Yang, Aigerman, Kovalsky</p>
</div>

<!-- Galloping Series -->
<div class="project-card">
<h3>Galloping Bubbles: Three-Part Series</h3>
<div class="figure-with-text">
<img src="/images/galloping_laws.png" class="clickable-figure">
<div class="figure-text">
A deep-dive experimental, numerical, and theoretical follow-up to our initial discovery of galloping bubbles, which are vertically vibrating millimetric-sized bubbles that spontaneously break symmetry and self-propel along a horizontal wall. At their heart is the parametric excitation of symmetrical and asymmetrical shape modes that together generate a non-reciprocal deformation, enabling the bubble to `swim'.
</div>
</div>
<p class="authors">Experiments: Guan et al., Simulations: Magoon et al., Theory: Tamim et al.</p>
<p class="venue"><b>Coming soon</b></p>
</div>

<!-- dQP -->
<div class="project-card">
<h3>dQP: Differentiating Quadratic Programs</h3>
<div class="figure-with-text">
<img src="/images/dQP_schematic.png" class="clickable-figure">
<div class="figure-text">
dQP is a modular framework for differentiating the solution to a quadratic programming problem (QP) with respect to its parameters, enabling the seamless integration of QPs into machine learning architectures and bilevel optimization. dQP supports over 15 state-of-the-art QP solvers.
</div>
</div>
<p class="authors">Magoon*, Yang*, Aigerman, Kovalsky</p>
<p class="venue">NeurIPS (2025)</p>
<div class="links pill-links">
<a class="pill" href="https://arxiv.org/pdf/2410.06324" target="_blank">Paper</a>
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
We discover, rationalize, and apply a fluid instability in which a vertically vibrating millimetric-sized bubble spontaneously breaks symmetry and self-propels along a horizontal wall. Applications include bubble removal, bubble sorting, surface cleaning, and even solving mazes! <br> <br> Awarded an APS DFD Gallery of Fluid Motion Award.
</div>
</div>
<p class="authors">Guan*, Tamim*, Magoon*, Stone, Sáenz</p>
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
We present a Faraday wave instability where a vertically vibrated annular bath spontaneously breaks symmetry from standing waves into fast traveling waves. <br> <br> Awarded an APS DFD Gallery of Fluid Motion Award.
</div>
</div>
<p class="authors">Guan, Magoon, Durey, Camassa, Sáenz</p>
<p class="venue">Physical Review Fluids (2023)</p>
<div class="links pill-links">
<a class="pill" href="https://journals.aps.org/prfluids/abstract/10.1103/PhysRevFluids.8.110501" target="_blank">Gallery Paper</a>
<a class="pill" href="https://www.youtube.com/watch?v=0d_D6yvXAFo" target="_blank">Video</a>
</div>
</div>




</div>
</div>






<div class="section" id="code">
<h2 style="margin-top:0;">Code</h2>

<p style="font-style:italic; font-size:0.85rem;">Click figures for project repositories.</p>

<div class="projects-grid">

<!-- dQP -->
<div class="project-card">
<h3>dQP: Differentiating Quadratic Programs</h3>
<div class="figure-with-text">
  <a href="https://github.com/cwmagoon/dQP" target="_blank">
    <img src="/images/dQP_performance.png" class="clickable-figure">
  </a>
</div>

<div style="display: inline-flex; align-items: center; gap:0.5rem; margin-top:0.5rem;">
  <!-- Left text -->
  <div style="font-size:0.85rem; white-space: nowrap; flex-shrink:0;">
    Packaged by PyPI. Installation command:
  </div>

  <!-- Code box -->
  <pre style="
      display:inline-block;
      background: #f6f8fa; 
      border: 1px solid #ddd;
      padding: 0.3rem 0.6rem; 
      border-radius: 6px; 
      font-family: Menlo, Monaco, Consolas, 'Courier New', monospace; 
      font-size: 0.85rem; 
      overflow-x: auto;
      margin:0;
      line-height:1.2;
  "><code>pip install libdqp</code></pre>
</div>

</div>





</div>
</div>










</div>










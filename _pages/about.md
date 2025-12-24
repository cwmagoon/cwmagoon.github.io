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
      a {
        text-decoration: none;   /* removes underline */
        color: #8A2BE2;          /* bright purple, you can change this hex */
      }
      a:hover {
        text-decoration: underline; /* optional: show underline on hover */
      }

    /* --- Image hover/click overlay styles --- */
    .img-container {
      position: relative;
      width: 100%;
    }
    
    .img-container img {
      width: 100%;
      height: auto;
      display: block;
    }
    
    .img-overlay {
      position: absolute;
      inset: 0;
      background: rgba(40, 40, 40, 0.75);
      color: #ffffff;
      display: flex;
      align-items: center;
      justify-content: center;
      text-align: center;
      padding: 0.8rem;
      font-size: 0.75rem;
      font-family: 'Times New Roman', serif;
      opacity: 0;
      transition: opacity 0.2s ease-in-out;
    }
    
    /* Desktop hover */
    .img-container:hover .img-overlay {
      opacity: 1;
    }
    
    /* Mobile / click */
    .img-container.active .img-overlay {
      opacity: 1;
    }

</style>

<script>
document.querySelectorAll('.img-container').forEach(el => {
  el.addEventListener('click', e => {
    e.stopPropagation();
    el.classList.toggle('active');
  });
});

document.addEventListener('click', () => {
  document.querySelectorAll('.img-container.active')
    .forEach(el => el.classList.remove('active'));
});
</script>








<style>
/* =========================
   MOBILE PORTRAIT FIX
   ========================= */
@media (max-width: 768px) and (orientation: portrait) {

  /* Stack rows vertically */
  body div[style*="justify-content:space-between"] {
    flex-direction: column !important;
    gap: 1.5rem !important;
  }

  body div[style*="flex:0 0 30%"] {
    flex: 1 1 100% !important;
    width: 100% !important;
  }

  /* Overlay becomes expandable block */
  .img-overlay {
    position: relative !important;
    inset: auto !important;
    opacity: 0;
    background: rgba(40,40,40,0.08);
    color: #000;
    margin-top: 0.4rem;
    padding: 0.6rem;
    font-size: 0.75rem;
    transition: opacity 0.2s ease;
  }

  /* Show overlay when active */
  .img-container.active .img-overlay {
    opacity: 1;
  }

  /* Make image feel tappable */
  .img-container img {
    cursor: pointer;
  }
}
</style>

<script>
/* =========================
   MOBILE TAP TO TOGGLE
   ========================= */
const isMobilePortrait = window.matchMedia(
  "(max-width: 768px) and (orientation: portrait)"
).matches;

if (isMobilePortrait) {
  document.querySelectorAll('.img-container').forEach(el => {
    el.addEventListener('click', e => {
      e.stopPropagation();
      el.classList.toggle('active');
    });
  });

  document.addEventListener('click', () => {
    document.querySelectorAll('.img-container.active')
      .forEach(el => el.classList.remove('active'));
  });
}
</script>


























<!-- Centered main content with tiny top space -->
<div style="max-width: 70%; margin: 0.5rem auto 0 auto; font-family: 'Times New Roman', serif;">


<!-- Top section: profile image left, text right -->
<div style="display: flex; align-items: flex-start; margin-bottom: 1rem;">
<img src="/images/profile.jpeg" alt="Connor Magoon" 
     style="width:140px; height:auto; margin-right:1rem; border-radius:8px;">
<div style="flex:1; display:flex; flex-direction:column; justify-content:space-between;">
  <div>
    <h2 style="margin-top:0; font-size:1.3rem; font-family: 'Times New Roman', serif;">Connor Magoon</h2> 
    <p style="font-size:0.9rem; font-family: 'Times New Roman', serif;">
    <a href="https://cwmagoon.github.io/files/cv.pdf">CV</a> | <a href="https://scholar.google.com/citations?user=18F4sZMAAAAJ&hl=en">Google Scholar</a> | <a href="https://orcid.org/0009-0009-1890-3279">ORCID</a> | <a href="https://github.com/cwmagoon">GitHub</a> | <a href="https://www.linkedin.com/in/connor-magoon-3189a9384">LinkedIn</a> <br>
      I am an Applied Mathematics PhD student at The University of North Carolina at Chapel Hill. <br>
      I have broad interests, spanning understanding physical phenomena to developing mathematical tools for solving applied problems. 
      One central thread sewn through all my work is geometry: leveraging simple geometry as a means for explanation and tackling complex geometry which is prevalent in the non-ideal real world. 
      I work on simulations and modeling of fluids in the <a href="https://www.pml.unc.edu/">Physical Mathematics Lab</a> under the direction of <a href="https://www.pml.unc.edu/about-me">Prof.Pedro Sáenz</a> 
      and in the intersection of optimization, machine learning, and graphics with advisor <a href="https://shaharkov.github.io/">Prof. Shahar Kovalsky</a>. 
    </p>
  </div>
  
</div>
</div>




<!-- First row title -->
<h2 style="
text-align:left;
margin-top:0.3rem;
margin-bottom:0.6rem;
font-size:1.1rem;
font-family:'Times New Roman', serif;
">
Projects
</h2>



<div style="
width:30%;
height:1px;
background:black;
margin-bottom:1.2rem;
"></div>

<p style="font-size:0.9rem; font-family: 'Times New Roman', serif; font-style:italic"> 
Hover over figures for project descriptions. 
</p>

<!-- First row of panels (3 panels + 2 blank) -->
<div style="display:flex; justify-content:space-between; margin-bottom:1.5rem; gap:2%; align-items:flex-start;">
<!-- Panel 6 -->
<div style="flex:0 0 30%; display:flex; flex-direction:column;">
  <h3 style="text-align:left; margin:0 0 0.2rem 0; font-size:0.85rem; font-family: 'Times New Roman', serif;">Collective Galloping Bubbles</h3>
  <div class="img-container">
    <img src="/images/collective_bubbles_flow.png" alt="Collective Bubbles Flow" style="width:100%; height:auto; display:block; margin-bottom:0.2rem;">
    <div class="img-overlay">
      Ongoing work
    </div>
  </div>
  <div style="margin-top:auto;">
    <p style="margin:0; font-size:0.75rem; font-family: 'Times New Roman', serif;">Magoon, Liu, Guan, Tamim, Stone, Sáenz</p>
    <!-- <p style="margin:0; font-size:0.75rem; font-family: 'Times New Roman', serif;">Ongoing Work</p> -->
  </div>
</div>
<!-- Panel 5 -->
<div style="flex:0 0 30%; display:flex; flex-direction:column;">
  <h3 style="text-align:left; margin:0 0 0.2rem 0; font-size:0.85rem; font-family: 'Times New Roman', serif;">Neural Mappings</h3>
  <div class="img-container">
    <img src="/images/ant_mapping.png" alt="Ant Mapping" style="width:100%; height:auto; display:block; margin-bottom:0.2rem;">
    <div class="img-overlay">
      Ongoing work
    </div>
  </div>
  <div style="margin-top:auto;">
    <p style="margin:0; font-size:0.75rem; font-family: 'Times New Roman', serif;">Magoon, Yang, Aigerman, Kovalsky</p>
    <!-- <p style="margin:0; font-size:0.75rem; font-family: 'Times New Roman', serif;">Ongoing Work</p> -->
  </div>
</div>
<!-- Panel 4 -->
<div style="flex:0 0 30%; display:flex; flex-direction:column;">
  <h3 style="text-align:left; margin:0 0 0.2rem 0; font-size:0.85rem; font-family: 'Times New Roman', serif;">Galloping Bubbles: Three-Part Series</h3>
  <div class="img-container">
    <img src="/images/galloping_laws.png" alt="Faraday Waves" style="width:100%; height:auto; display:block; margin-bottom:0.2rem;">
    <div class="img-overlay">
      A deep-dive experimental, numerical, and theoretical follow-up to our initial discovery of galloping bubbles, which are vertically vibrating millimetric-sized bubbles that spontaneously break symmetry and self-propel along a horizontal wall. At their heart is the parametric excitation of symmetrical and asymmetrical shape modes that together generate a non-reciprocal deformation, enabling the bubble to `swim'.
    </div>
  </div>
  <div style="margin-top:auto;">
    <p style="margin:0; font-size:0.75rem; font-family: 'Times New Roman', serif;">Guan et al.; Magoon et al.; Tamim et al.</p>
    <p style="margin:0; font-size:0.7rem; font-style:italic;"><b>Coming Soon!</b></p>
    <!-- <p style="margin:0; font-size:0.75rem; font-family: 'Times New Roman', serif;"><a href="https://journals.aps.org/prfluids/abstract/10.1103/PhysRevFluids.8.110501">Paper</a> | <a href="https://www.youtube.com/watch?v=0d_D6yvXAFo">Video</a></p> -->
  </div>
</div>
<!-- Blank columns for spacing -->
<div style="flex:0 0 30%;"></div>
<div style="flex:0 0 30%;"></div>
</div>







<!-- Second row title -->
<!-- <h2 style="text-align:left; margin-top:0.3rem; margin-bottom:0.4rem; font-size:1.1rem; font-family: 'Times New Roman', serif;">Optimization and Geometry</h2> -->

<!-- Second row of panels (2 panels + 3 blank) -->
<div style="display:flex; justify-content:space-between; margin-bottom:1.5rem; gap:2%; align-items:flex-start;">
<!-- Panel 3 -->
<div style="flex:0 0 30%; display:flex; flex-direction:column;">
  <h3 style="text-align:left; margin:0 0 0.2rem 0; font-size:0.85rem; font-family: 'Times New Roman', serif;">dQP: Differentiating Quadratic Programs </h3>
  <div class="img-container">
    <img src="/images/dQP_schematic.png" alt="dQP Schematic" style="width:100%; height:auto; display:block; margin-bottom:0.2rem;">
    <div class="img-overlay">
      dQP is a modular framework for differentiating the solution to a quadratic programming problem (QP) with respect to its parameters, enabling the seamless integration of QPs into machine learning architectures and bilevel optimization. dQP supports over 15 state-of-the-art QP solvers.
    </div>
  </div>
  <div style="margin-top:auto;">
    <p style="margin:0; font-size:0.75rem; font-family: 'Times New Roman', serif;">Magoon<sup>*</sup>, Yang<sup>*</sup>, Aigerman, Kovalsky</p>
    <p style="margin:0; font-size:0.7rem; font-style:italic;">NeurIPS (2025)</p>
    <p style="margin:0; font-size:0.75rem; font-family: 'Times New Roman', serif;"><a href="https://arxiv.org/pdf/2410.06324">Paper</a> | <a href="https://github.com/cwmagoon/dQP">Code</a> | <a href="https://neurips.cc/media/PosterPDFs/NeurIPS%202025/119180.png?t=1762316861.5409572">Poster</a> | <a href="https://neurips.cc/virtual/2025/loc/san-diego/poster/119180">Video</a> </p>
  </div>
</div>
<!-- Panel 2 -->
<div style="flex:0 0 30%; display:flex; flex-direction:column;">
  <h3 style="text-align:left; margin:0 0 0.2rem 0; font-size:0.85rem; font-family: 'Times New Roman', serif;">Galloping Bubbles</h3>
  <div class="img-container">
    <img src="/images/galloping_bubble.png" alt="Galloping Bubble" style="width:100%; height:auto; display:block; margin-bottom:0.2rem;">
    <div class="img-overlay">
      We discover, rationalize, and apply a fluid instability in which a vertically vibrating millimetric-sized bubble spontaneously breaks symmetry and self-propels along a horizontal wall. Applications include bubble removal, bubble sorting, surface cleaning, and even solving mazes! <br> <br> Awarded an APS DFD Gallery of Fluid Motion Award.
    </div>
  </div>
  <div style="margin-top:auto;">
    <p style="margin:0; font-size:0.75rem; font-family: 'Times New Roman', serif;">Guan<sup>*</sup>, Tamim<sup>*</sup>, Magoon<sup>*</sup>, Stone, Sáenz<br> </p>
    <p style="margin:0; font-size:0.7rem; font-style:italic;">Nature Communications (2025)</p>
    <p style="margin:0; font-size:0.75rem; font-family: 'Times New Roman', serif;"><a href="https://www.nature.com/articles/s41467-025-56611-5">Paper</a> | <a href="https://doi.org/10.1103/fbdh-fnzv">Gallery Paper</a> | <a href="https://www.youtube.com/watch?v=gLbRx5nBpEo">Video</a></p>
  </div>
</div>
 <!-- Panel 1 -->
<div style="flex:0 0 30%; display:flex; flex-direction:column;">
  <h3 style="text-align:left; margin:0 0 0.2rem 0; font-size:0.85rem; font-family: 'Times New Roman', serif;">Traveling Faraday Waves</h3>
  <div class="img-container">
    <img src="/images/faraday_waves.png" alt="Faraday Waves" style="width:100%; height:auto; display:block; margin-bottom:0.2rem;">
    <div class="img-overlay">
      We present a Faraday wave instability where a vertically vibrated annular bath spontaneously breaks symmetry from standing waves into fast traveling waves. <br> <br> Awarded an APS DFD Gallery of Fluid Motion Award.
    </div>
  </div>
  <div style="margin-top:auto;">
    <p style="margin:0; font-size:0.75rem; font-family: 'Times New Roman', serif;">Guan, Magoon, Durey, Camassa, Sáenz</p>
    <p style="margin:0; font-size:0.7rem; font-style:italic;">Physical Review Fluids (2023)</p>
    <p style="margin:0; font-size:0.75rem; font-family: 'Times New Roman', serif;"><a href="https://journals.aps.org/prfluids/abstract/10.1103/PhysRevFluids.8.110501">Gallery Paper</a> | <a href="https://www.youtube.com/watch?v=0d_D6yvXAFo">Video</a></p>
  </div>
</div>
<!-- Blank columns -->
<div style="flex:0 0 30%;"></div>
<div style="flex:0 0 30%;"></div>
<div style="flex:0 0 30%;"></div>
</div>

</div>

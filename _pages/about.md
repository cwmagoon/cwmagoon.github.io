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
</style>

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
          I am an Applied Mathematics PhD student at The University of North Carolina at Chapel Hill. <br>
          My primary area of research is on simulations and modeling of fluids in the <a href="https://www.pml.unc.edu/">Physical Mathematics Lab</a> under the direction of <a href="https://www.pml.unc.edu/about-me">Prof. Pedro Sáenz</a>. <br>
          My secondary area is in the intersection of optimization, machine learning, and graphics with advisor <a href="https://shaharkov.github.io/">Prof. Shahar Kovalsky</a>. 
        </p>
      </div>
      <!-- Profile links flush with bottom of profile picture -->
      <p style="margin-top:0.5rem; font-size:0.75rem;">
        <a href="https://cwmagoon.github.io/files/cv.pdf">CV</a> | <a href="https://scholar.google.com/citations?user=18F4sZMAAAAJ&hl=en">Google Scholar</a> | <a href="https://orcid.org/0009-0009-1890-3279">ORCID</a> | <a href="https://github.com/cwmagoon">GitHub</a> | <a href="https://www.linkedin.com/in/connor-magoon-3189a9384">LinkedIn</a>
      </p>
    </div>
  </div>

  <!-- First row title -->
  <h2 style="text-align:left; margin-top:0.3rem; margin-bottom:0.4rem; font-size:1.1rem; font-family: 'Times New Roman', serif;">Fluids</h2>

  <!-- First row of panels (3 panels + 2 blank) -->
  <div style="display:flex; justify-content:space-between; margin-bottom:1.5rem; gap:2%; align-items:flex-start;">
    <!-- Panel 1 -->
    <div style="flex:0 0 30%; display:flex; flex-direction:column;">
      <h3 style="text-align:left; margin:0 0 0.2rem 0; font-size:0.85rem; font-family: 'Times New Roman', serif;">Collective Galloping Bubbles</h3>
      <img src="/images/collective_bubbles_flow.png" alt="Collective Bubbles Flow" style="width:100%; height:auto; display:block; margin-bottom:0.2rem;">
      <div style="margin-top:auto;">
        <p style="margin:0; font-size:0.75rem; font-family: 'Times New Roman', serif;">Magoon, Liu, Guan, Tamim, Stone, Sáenz</p>
        <p style="margin:0; font-size:0.75rem; font-family: 'Times New Roman', serif;">Ongoing Work</p>
      </div>
    </div>
    <!-- Panel 2 -->
    <div style="flex:0 0 30%; display:flex; flex-direction:column;">
      <h3 style="text-align:left; margin:0 0 0.2rem 0; font-size:0.85rem; font-family: 'Times New Roman', serif;">Galloping Bubbles</h3>
      <img src="/images/galloping_bubble.png" alt="Galloping Bubble" style="width:100%; height:auto; display:block; margin-bottom:0.2rem;">
      <div style="margin-top:auto;">
        <p style="margin:0; font-size:0.75rem; font-family: 'Times New Roman', serif;">Guan, Tamim, Magoon, Stone, Sáenz<br> </p>
        <p style="margin:0; font-size:0.7rem; font-style:italic;">Nature Communications (2025)</p>
        <p style="margin:0; font-size:0.75rem; font-family: 'Times New Roman', serif;"><a href="https://www.nature.com/articles/s41467-025-56611-5">Paper</a> | <a href="https://www.youtube.com/watch?v=gLbRx5nBpEo">Video</a></p>
      </div>
    </div>
    <!-- Panel 3 -->
    <div style="flex:0 0 30%; display:flex; flex-direction:column;">
      <h3 style="text-align:left; margin:0 0 0.2rem 0; font-size:0.85rem; font-family: 'Times New Roman', serif;">Traveling Faraday Waves</h3>
      <img src="/images/faraday_waves.png" alt="Faraday Waves" style="width:100%; height:auto; display:block; margin-bottom:0.2rem;">
      <div style="margin-top:auto;">
        <p style="margin:0; font-size:0.75rem; font-family: 'Times New Roman', serif;">Guan, Magoon, Durey, Camassa, Sáenz</p>
        <p style="margin:0; font-size:0.7rem; font-style:italic;">Physical Review Fluids (2023)</p>
        <p style="margin:0; font-size:0.75rem; font-family: 'Times New Roman', serif;"><a href="https://journals.aps.org/prfluids/abstract/10.1103/PhysRevFluids.8.110501">Paper</a> | <a href="https://www.youtube.com/watch?v=0d_D6yvXAFo">Video</a></p>
      </div>
    </div>
    <!-- Blank columns for spacing -->
    <div style="flex:0 0 30%;"></div>
    <div style="flex:0 0 30%;"></div>
  </div>

  <!-- Second row title -->
  <h2 style="text-align:left; margin-top:0.3rem; margin-bottom:0.4rem; font-size:1.1rem; font-family: 'Times New Roman', serif;">Optimization and Geometry</h2>

  <!-- Second row of panels (2 panels + 3 blank) -->
  <div style="display:flex; justify-content:space-between; margin-bottom:1.5rem; gap:2%; align-items:flex-start;">
    <!-- Panel 4 -->
    <div style="flex:0 0 30%; display:flex; flex-direction:column;">
      <h3 style="text-align:left; margin:0 0 0.2rem 0; font-size:0.85rem; font-family: 'Times New Roman', serif;">Neural Mappings</h3>
      <img src="/images/ant_mapping.png" alt="Ant Mapping" style="width:100%; height:auto; display:block; margin-bottom:0.2rem;">
      <div style="margin-top:auto;">
        <p style="margin:0; font-size:0.75rem; font-family: 'Times New Roman', serif;">Magoon, Yang, Aigerman, Kovalsky</p>
        <p style="margin:0; font-size:0.75rem; font-family: 'Times New Roman', serif;">Ongoing Work</p>
      </div>
    </div>
    <!-- Panel 5 -->
    <div style="flex:0 0 30%; display:flex; flex-direction:column;">
      <h3 style="text-align:left; margin:0 0 0.2rem 0; font-size:0.85rem; font-family: 'Times New Roman', serif;">dQP: Differentiating Quadratic Programs </h3>
      <img src="/images/dQP_schematic.png" alt="dQP Schematic" style="width:100%; height:auto; display:block; margin-bottom:0.2rem;">
      <div style="margin-top:auto;">
        <p style="margin:0; font-size:0.75rem; font-family: 'Times New Roman', serif;">Magoon, Yang, Aigerman, Kovalsky</p>
        <p style="margin:0; font-size:0.7rem; font-style:italic;">Accepted. NeurIPS (2025)</p>
        <p style="margin:0; font-size:0.75rem; font-family: 'Times New Roman', serif;"><a href="https://arxiv.org/pdf/2410.06324">Paper</a> | <a href="https://github.com/cwmagoon/dQP">Code</a> </p>
      </div>
    </div>
    <!-- Blank columns -->
    <div style="flex:0 0 30%;"></div>
    <div style="flex:0 0 30%;"></div>
    <div style="flex:0 0 30%;"></div>
  </div>

</div>

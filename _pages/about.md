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
  html {
    scroll-behavior: smooth;
  }

  * {
    font-family: "Times New Roman", Times, serif !important;
  }

  body {
    margin: 0;
    padding: 0;
  }

  @media (prefers-reduced-motion: reduce) {
    html {
      scroll-behavior: auto;
    }
  }

  a {
    text-decoration: none;
    color: inherit;
  }

  .main-wrap {
    max-width: min(1500px, 92vw);
    margin: 0.25rem auto 1rem auto;
  }

  .section {
    padding: 0.75rem;
    margin: 1rem 0;
    border-radius: 14px;
    background: #f3f3f3;
  }

  .section-accent-gray {
    border-left: 4px solid #8d8d8d;
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
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: 1.5rem;
  }

  @media (max-width: 1400px) {
    .projects-grid { grid-template-columns: repeat(3, minmax(0, 1fr)); }
    .main-wrap { max-width: min(1280px, 90vw); }
  }

  @media (max-width: 1100px) {
    .projects-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
    .main-wrap { max-width: 92vw; }
  }

  @media (max-width: 760px) {
    .projects-grid { grid-template-columns: 1fr; }
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
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    container-type: inline-size;
    display: flex;
    flex-direction: column;
    position: relative;
    overflow: visible;
  }

  .project-card:hover {
    transform: translateY(-8px) scale(1.015);
    box-shadow: 0 18px 40px rgba(0,0,0,0.2), 0 8px 18px rgba(0,0,0,0.12);
  }

  .project-card h3 {
    font-family: Helvetica, Arial, sans-serif !important;
    font-size: 0.9rem; /* JS will override this dynamically */
    margin: 0 0 0.4rem 0;
    font-weight: bold;
    line-height: 1.3;
    white-space: nowrap;
    overflow-wrap: normal;
    overflow: hidden;
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
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background: rgba(0,0,0,0.6);
    z-index: 10000;
    justify-content: center;
    align-items: center;
    padding: 1.5rem;
    display: flex;
    opacity: 0;
    visibility: hidden;
    pointer-events: none;
    transition: opacity 0.18s ease, visibility 0.18s ease;
  }

  .modal-overlay.active {
    opacity: 1;
    visibility: visible;
    pointer-events: auto;
  }

  .modal-content {
    background: #fff;
    border-radius: 18px;
    width: min(1020px, 92vw);
    max-height: 86vh;
    padding: 1.8rem 2.1rem;
    position: relative;
    box-sizing: border-box;
    transform-origin: top left;
    overflow: hidden;
    box-shadow: 0 28px 80px rgba(0,0,0,0.24);
    will-change: transform, opacity;
  }

  .modal-body {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.5rem;
    align-items: center;
  }

  .modal-media {
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: 0;
  }

  .modal-content img {
    width: 100%;
    max-height: min(640px, 62vh);
    object-fit: contain;
    border-radius: 10px;
    margin: 0;
    display: block;
    will-change: transform, opacity;
  }

  .modal-copy {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    min-width: 0;
    max-width: 34rem;
    padding: 0.1rem 0.2rem 0 0;
    font-size: 0.9rem;
    line-height: 1.5;
    color: #222;
  }

  .modal-copy > *:last-child {
    margin-bottom: 0;
  }

  .modal-content[data-animating="true"] .modal-copy {
    opacity: 0;
  }

  .modal-content[data-animating="false"] .modal-copy {
    opacity: 1;
    transition: opacity 0.01s linear;
  }

  .modal-content[data-reveal-copy="true"] .modal-copy {
    opacity: 1;
    transition: opacity 0.01s linear;
  }

  .modal-close {
    position: absolute;
    top: 0.85rem;
    right: 1rem;
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

  .modal-title { font-size: 1.08rem; font-weight: bold; margin: 0 0 0.45rem 0; line-height: 1.3; }
  .modal-authors { font-size: 0.87rem; margin: 0 0 0.28rem 0; color: #444; }
  .modal-venue { font-size: 0.82rem; font-style: italic; margin: 0 0 0.85rem 0; color: #666; }
  .modal-desc { margin-bottom: 0.85rem; }
  .modal-desc p:first-child { margin-top: 0; }
  .modal-desc p:last-child { margin-bottom: 0; }
  .modal-equal { font-size: 0.78rem; font-style: italic; color: #888; margin-top: 0.55rem; }
  .modal-pills { display: flex; flex-wrap: wrap; gap: 0.45rem; margin-top: 0.7rem; }

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

  /* Side-by-side previews (paper/video/poster), desktop only */
  .modal-previews {
    display: none;
    grid-template-columns: 1fr 1fr;
    gap: 1.5rem;
    margin-top: 1.5rem;
  }

  .modal-content.has-previews {
    width: min(1500px, 96vw);
    overflow-y: auto;
    max-height: 94vh;
  }

  .modal-content.has-previews .modal-previews {
    display: grid;
  }

  .preview-box {
    display: block;
    border-radius: 10px;
    overflow: hidden;
    background: #f6f8fa;
    border: 1px solid #e0e0e0;
  }

  .preview-video {
    position: relative;
    padding-top: 56.25%; /* 16:9 */
    height: 0;
  }

  .preview-video iframe {
    position: absolute;
    top: 0; left: 0;
    width: 100%;
    height: 100%;
    border: 0;
  }

  .preview-poster {
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: 160px;
    cursor: pointer;
  }

  .preview-poster img {
    width: 100%;
    height: auto;
    display: block;
  }

  .preview-paper {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
    min-height: 220px;
    color: #666;
    font-size: 0.85rem;
    text-align: center;
    border-style: dashed;
    cursor: pointer;
    transition: background 0.15s;
  }

  .preview-paper:hover {
    background: #eef1f4;
  }

  .preview-paper-icon {
    font-size: 1.8rem;
  }

  .preview-paper-img {
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
  }

  .preview-paper-img img {
    width: 100%;
    height: auto;
    display: block;
  }

  @media (max-width: 700px) {
    .modal-previews {
      grid-template-columns: 1fr;
    }
  }

  @media (max-width: 820px) {
    .modal-overlay {
      padding: 0.75rem;
      align-items: flex-start;
    }

    .modal-content {
      width: min(92vw, 640px);
      min-height: auto;
      max-height: 90vh;
      padding: 1rem;
      overflow-y: auto;
    }

    .modal-body {
      grid-template-columns: 1fr;
      gap: 1rem;
    }

    .modal-content img {
      max-height: 40vh;
    }

    .modal-copy {
      max-width: none;
      padding-right: 0;
    }
  }
</style>

<div class="modal-overlay" id="desc-modal">
  <div class="modal-content">
    <button class="modal-close" aria-label="Close">&times;</button>
    <div class="modal-body">
      <div class="modal-media">
        <img id="modal-img" src="" alt="">
      </div>
      <div class="modal-copy">
        <p class="modal-title" id="modal-title"></p>
        <p class="modal-authors" id="modal-authors"></p>
        <p class="modal-venue" id="modal-venue"></p>
        <div class="modal-desc" id="modal-text"></div>
        <p class="modal-equal" id="modal-equal" style="display:none;"><sup>*</sup>Equal contribution</p>
        <div class="modal-pills" id="modal-pills"></div>
      </div>
    </div>
    <div class="modal-previews" id="modal-previews"></div>
  </div>
</div>

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

/* Side-by-side previews shown under the modal, desktop only.
   "paper" falls back to a placeholder box when no generated preview image exists yet
   (see scripts/make_paper_preview.py). */
const paperPreviewImages = {
  "Galloping Bubbles": "/images/paper_previews/nat_com.png",
  "dQP: Differentiating Quadratic Programs": "/images/paper_previews/dqp.png",
  "Traveling Faraday Waves": "/images/paper_previews/faraday.png"
};

const modalPreviewConfig = {
  "dQP: Differentiating Quadratic Programs": [
    { type: "paper", label: "Paper" },
    { type: "poster", label: "Poster" }
  ],
  "Galloping Bubbles": [
    { type: "paper", label: "Paper" },
    { type: "video", label: "Video" }
  ],
  "Traveling Faraday Waves": [
    { type: "paper", label: "Gallery Paper" },
    { type: "video", label: "Video" }
  ]
};

function isIOSDesktopSite() {
  /* iPhone/iPad browsers in "Request Desktop Website" mode spoof a Mac user agent
     but remain touch devices, so the hover/pointer check below misses them. */
  var isMacUA = /Macintosh/.test(navigator.userAgent);
  var hasTouch = navigator.maxTouchPoints > 1 || 'ontouchend' in document;
  return isMacUA && hasTouch;
}

function isDesktopPreview() {
  return window.matchMedia('(hover: hover) and (pointer: fine)').matches || isIOSDesktopSite();
}

function getYouTubeEmbedUrl(url) {
  var idMatch = url.match(/(?:youtu\.be\/|[?&]v=)([^&]+)/);
  var id = idMatch ? idMatch[1] : '';
  return id ? ('https://www.youtube.com/embed/' + id) : '';
}

function buildPreviewHTML(card) {
  if (!card || !isDesktopPreview()) return '';
  var h3 = card.querySelector('h3');
  var title = h3 ? h3.textContent.trim() : '';
  var config = modalPreviewConfig[title];
  var links = card.querySelector('.links.pill-links');
  if (!config || !links) return '';

  var anchors = Array.from(links.querySelectorAll('a'));
  var boxes = config.map(function (item) {
    var anchor = anchors.find(function (a) { return a.textContent.trim() === item.label; });
    if (!anchor) return '';
    var href = anchor.href;

    if (item.type === 'video') {
      var embedUrl = getYouTubeEmbedUrl(href);
      if (!embedUrl) return '';
      return '<div class="preview-box preview-video"><iframe src="' + embedUrl +
        '" title="Video preview" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy"></iframe></div>';
    }
    if (item.type === 'poster') {
      return '<a class="preview-box preview-poster" href="' + href + '" target="_blank"><img src="' + href + '" alt="Poster"></a>';
    }
    var paperImg = paperPreviewImages[title];
    if (paperImg) {
      return '<a class="preview-box preview-paper-img" href="' + href + '" target="_blank"><img src="' + paperImg + '" alt="Paper preview"></a>';
    }
    return '<a class="preview-box preview-paper" href="' + href + '" target="_blank">' +
      '<span class="preview-paper-icon">&#128196;</span><span>Paper preview coming soon</span></a>';
  }).filter(Boolean);

  return boxes.join('');
}

document.addEventListener('DOMContentLoaded', function () {
  var modal = document.getElementById('desc-modal');
  var modalContent = modal ? modal.querySelector('.modal-content') : null;
  var modalImg = document.getElementById('modal-img');
  var modalTitle = document.getElementById('modal-title');
  var modalAuthors = document.getElementById('modal-authors');
  var modalVenue = document.getElementById('modal-venue');
  var modalText = document.getElementById('modal-text');
  var modalEqual = document.getElementById('modal-equal');
  var modalPills = document.getElementById('modal-pills');
  var modalPreviews = document.getElementById('modal-previews');
  var closeBtn = modal ? modal.querySelector('.modal-close') : null;
  const research = document.getElementById('research');
  if (!research || !modal || !modalContent || !closeBtn) return;

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

  var activeTrigger = null;
  var isAnimating = false;
  var animationMs = 520;
  var closeFadeMs = 180;
  var copyRevealTimer = null;

  function resetModalTransform() {
    if (copyRevealTimer) {
      window.clearTimeout(copyRevealTimer);
      copyRevealTimer = null;
    }
    modalContent.style.transform = '';
    modalContent.style.transition = '';
    modalContent.style.opacity = '';
    modalImg.style.transform = '';
    modalImg.style.transition = '';
    modalImg.style.transformOrigin = '';
    modalContent.dataset.revealCopy = 'false';
  }

  function fitModalSize() {
    var maxW = Math.min(1500, window.innerWidth * 0.96);
    var minW = Math.min(600, maxW);
    var availableH = window.innerHeight * 0.94;

    modalContent.style.transition = 'none';
    modalContent.style.overflow = 'visible';
    modalContent.style.maxHeight = 'none';

    function heightAt(w) {
      modalContent.style.width = w + 'px';
      return modalContent.scrollHeight;
    }

    var fitWidth = maxW;
    if (heightAt(maxW) > availableH) {
      var lo = minW, hi = maxW;
      for (var i = 0; i < 8; i++) {
        var mid = (lo + hi) / 2;
        if (heightAt(mid) > availableH) {
          hi = mid;
        } else {
          lo = mid;
        }
      }
      fitWidth = lo;
    }

    modalContent.style.width = fitWidth + 'px';
    modalContent.style.maxHeight = availableH + 'px';
    modalContent.style.overflow = 'hidden';
    modalContent.style.overflowY = 'auto';
  }

  function setModalContent(card, img, text) {
    modalImg.onload = null;
    modalImg.src = img.src;
    modalImg.alt = img.alt || '';
    modalText.innerHTML = text.innerHTML;
    var h3 = card ? card.querySelector('h3') : null;
    modalTitle.textContent = h3 ? h3.textContent : '';
    var authors = card ? card.querySelector('.authors') : null;
    modalAuthors.innerHTML = authors ? authors.innerHTML : '';
    var venue = card ? card.querySelector('.venue') : null;
    modalVenue.innerHTML = venue ? venue.innerHTML : '';
    modalVenue.style.display = venue ? '' : 'none';
    var hasEqual = authors && authors.innerHTML.indexOf('sup') !== -1;
    modalEqual.style.display = hasEqual ? '' : 'none';
    var links = card ? card.querySelector('.links.pill-links') : null;
    modalPills.innerHTML = links ? links.innerHTML : '';
    modalPills.style.display = links ? '' : 'none';

    var previewHTML = buildPreviewHTML(card);
    modalPreviews.innerHTML = previewHTML;
    modalContent.classList.toggle('has-previews', !!previewHTML);

    fitModalSize();

    var pendingImgs = [modalImg].concat(Array.from(modalPreviews.querySelectorAll('img')));
    pendingImgs.forEach(function (im) {
      if (!im.complete) {
        im.addEventListener('load', fitModalSize, { once: true });
      }
    });
  }

  function animateOpen(fromImg) {
    modal.classList.add('active');
    modalContent.dataset.animating = 'true';
    modalContent.dataset.revealCopy = 'false';
    modalContent.style.transition = 'none';
    modalContent.style.transform = 'none';
    modalContent.style.opacity = '1';
    modalImg.style.transition = 'none';
    modalImg.style.transform = 'none';

    var fromRect = fromImg.getBoundingClientRect();
    var toRect = modalContent.getBoundingClientRect();
    var contentScale = Math.min(fromRect.width / toRect.width, fromRect.height / toRect.height);
    var fromCenterX = fromRect.left + (fromRect.width / 2);
    var fromCenterY = fromRect.top + (fromRect.height / 2);
    var toCenterX = toRect.left + (toRect.width / 2);
    var toCenterY = toRect.top + (toRect.height / 2);
    var translateX = fromCenterX - toCenterX;
    var translateY = fromCenterY - toCenterY;

    var modalImgRect = modalImg.getBoundingClientRect();
    var imgScaleX = fromRect.width / modalImgRect.width;
    var imgScaleY = fromRect.height / modalImgRect.height;
    var imgTranslateX = fromCenterX - (modalImgRect.left + modalImgRect.width / 2);
    var imgTranslateY = fromCenterY - (modalImgRect.top + modalImgRect.height / 2);

    modalContent.style.transform = 'translate(' + translateX + 'px, ' + translateY + 'px) scale(' + contentScale + ')';
    modalContent.style.opacity = '0.7';
    modalImg.style.transformOrigin = 'center center';
    modalImg.style.transform = 'translate(' + imgTranslateX + 'px, ' + imgTranslateY + 'px) scale(' + imgScaleX + ', ' + imgScaleY + ')';
    modalContent.getBoundingClientRect();

    requestAnimationFrame(function () {
      modalContent.style.transition = 'transform ' + animationMs + 'ms cubic-bezier(0.2, 0.8, 0.2, 1), opacity ' + animationMs + 'ms ease';
      modalImg.style.transition = 'transform ' + animationMs + 'ms cubic-bezier(0.2, 0.8, 0.2, 1)';
      modalContent.style.transform = 'translate(0px, 0px) scale(1)';
      modalContent.style.opacity = '1';
      modalImg.style.transform = 'translate(0px, 0px) scale(1, 1)';
      copyRevealTimer = window.setTimeout(function () {
        modalContent.dataset.revealCopy = 'true';
      }, Math.round(animationMs * 0.68));
      window.setTimeout(function () {
        modalContent.dataset.animating = 'false';
        resetModalTransform();
        isAnimating = false;
      }, animationMs);
    });
  }

  function animateClose() {
    if (isAnimating) return;
    isAnimating = true;
    modalContent.dataset.animating = 'true';
    modalContent.style.transition = 'opacity ' + closeFadeMs + 'ms ease';
    modalContent.style.opacity = '0';
    modal.classList.remove('active');

    window.setTimeout(function () {
      modalContent.dataset.animating = 'false';
      resetModalTransform();
      modalPreviews.innerHTML = '';
      modalContent.classList.remove('has-previews');
      activeTrigger = null;
      isAnimating = false;
    }, closeFadeMs);
  }

  var figures = research.querySelectorAll('.figure-with-text');
  for (var i = 0; i < figures.length; i++) {
    (function (el) {
      var img = el.querySelector('img');
      var text = el.querySelector('.figure-text');
      if (!img || !text) return;

      img.addEventListener('click', function (e) {
        e.preventDefault();
        e.stopPropagation();
        if (isAnimating) return;

        var card = el.closest('.project-card');
        activeTrigger = img;
        isAnimating = true;
        setModalContent(card, img, text);
        animateOpen(img);
      });
    })(figures[i]);
  }

  closeBtn.addEventListener('click', animateClose);
  modal.addEventListener('click', function (e) {
    if (e.target === modal) animateClose();
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && modal.classList.contains('active')) animateClose();
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
<div class="section section-accent-gray" id="research">
<div style="display:flex; align-items:center; gap:1rem; margin-bottom:0.5rem;">
<h2 style="margin-bottom:0;">Research</h2>
<span style="font-style:italic; font-size:0.85rem; white-space:nowrap;">Click figures to enlarge and display short project descriptions.</span>
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






<div class="section section-accent-gray" id="code">
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
      var available = h.clientWidth;

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
      h.style.whiteSpace = 'nowrap';
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

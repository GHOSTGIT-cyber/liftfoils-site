import json, urllib.request, urllib.error, base64

html = """<!-- wp:html -->
<style>
/* ============================================================
   ATELIER CHILD — RESET COMPLET POUR PLEIN ECRAN
   ============================================================ */

/* 1) Neutraliser TOUS les conteneurs Atelier/WP qui limitent la largeur */
body.page #page,
body.page #content,
body.page #primary,
body.page #inner-content,
body.page .content-area,
body.page .site-content,
body.page .entry-content,
body.page .entry-content-wrap,
body.page .page-content,
body.page article.page,
body.page .hentry,
body.page main#main,
#page, #content, #primary, #inner-content,
.content-area, .site-content, .entry-content,
.entry-content-wrap, .page-content, .hentry,
main#main, .wrap, .container, .site-inner {
  max-width: none !important;
  width: 100% !important;
  padding-left: 0 !important;
  padding-right: 0 !important;
  margin-left: 0 !important;
  margin-right: 0 !important;
}

/* 2) FIX MEGAMENU V4 — supprime le padding-top:72px du body
   Le megamenu v4 (body.lfmm-v4-active) ajoute 72px sur le body
   pour compenser le header fixe. On le retire et on remonte le hero. */
body.lfmm-v4-active {
  padding-top: 0 !important;
  margin-top: 0 !important;
}
@media (max-width: 900px) {
  body.lfmm-v4-active {
    padding-top: 0 !important;
  }
}

/* 2b) Supprimer tout autre espace résiduel */
.site-header, #site-header, #site-header-wrap,
.header-wrap, .header-main, #header,
.top-bar, #top-bar-wrap, .header-top,
.oceanwp-mobile-menu-icon {
  margin-bottom: 0 !important;
}
#page, .site-content, #content,
.entry-content-wrap, #primary, .content-area {
  padding-top: 0 !important;
  margin-top: 0 !important;
}

/* 2c) ZONE BLANCHE ATELIER — .page-heading génère une zone blanche
   même avec page-heading-hidden, il a du height. On le colle. */
.page-heading,
.page-heading-hidden,
.page-heading.page-heading-hidden,
#main-container > .page-heading,
.page-heading .container,
.page-heading .heading-text,
#main-container {
  padding-top: 0 !important;
  margin-top: 0 !important;
  min-height: 0 !important;
  height: auto !important;
}
.page-heading-hidden {
  display: none !important;
}

/* 2d) Fond body turquoise Atelier (#1fe2c5) — on le passe en noir
   pour que si un espace subsiste il ne soit pas visible */
body.wp-theme-atelier,
body.wp-child-theme-atelier-child {
  background-color: #000 !important;
}
#container, #main-container {
  background-color: #000 !important;
}

/* 3) Le div lf2 prend 100% */
*,*::before,*::after{box-sizing:border-box}
.lf2 {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  width: 100%;
  max-width: 100%;
  overflow-x: hidden;
}

/* 4) Chaque section = 100vw absolu */
.lf2 > section,
.lf2 > div.lf2-marquee-wrap,
.lf2 > div.lf2-narrative,
.lf2 > div.lf2-split {
  display: block;
  width: 100vw !important;
  max-width: 100vw !important;
  position: relative;
  left: 50%;
  right: 50%;
  margin-left: -50vw !important;
  margin-right: -50vw !important;
  box-sizing: border-box;
}

/* ===== HERO ===== */
.lf2-hero {
  position: relative;
  height: 100vh;
  min-height: 600px;
  overflow: hidden;
  display: flex;
  align-items: flex-end;
  justify-content: flex-start;
  background: #000;
}
.lf2-hero video {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  opacity: .88;
}
.lf2-hero-grad {
  position: absolute;
  inset: 0;
  background: linear-gradient(to top, rgba(0,0,0,.92) 0%, rgba(0,0,0,.4) 50%, transparent 100%);
}
.lf2-hero-content {
  position: relative;
  z-index: 2;
  padding: 0 7vw 90px;
  color: #fff;
}
.lf2-hero-eyebrow {
  font-size: .72rem;
  letter-spacing: .3em;
  text-transform: uppercase;
  opacity: .75;
  margin-bottom: 1.5rem;
  display: block;
  font-weight: 500;
}
.lf2-hero-title {
  font-size: clamp(5rem, 14vw, 13rem);
  font-weight: 900;
  line-height: .88;
  letter-spacing: -.03em;
  margin: 0 0 2rem;
  text-transform: uppercase;
  text-shadow: 0 4px 40px rgba(0,0,0,.5);
}
.lf2-hero-title .accent { color: #36B7B2; }
.lf2-hero-title .dim { color: rgba(255,255,255,.22); }
.lf2-hero-sub {
  font-size: 1.2rem;
  font-weight: 400;
  opacity: .9;
  margin-bottom: 2.5rem;
  max-width: 520px;
  line-height: 1.7;
  text-shadow: 0 2px 12px rgba(0,0,0,.6);
}
.lf2-hero-actions { display: flex; gap: 16px; flex-wrap: wrap; }
.lf2-btn-teal {
  padding: 16px 48px;
  background: #36B7B2;
  color: #fff;
  text-decoration: none;
  font-size: .8rem;
  letter-spacing: .15em;
  text-transform: uppercase;
  font-weight: 700;
  display: inline-block;
}
.lf2-btn-ghost {
  padding: 16px 48px;
  border: 2px solid rgba(255,255,255,.8);
  color: #fff;
  text-decoration: none;
  font-size: .8rem;
  letter-spacing: .15em;
  text-transform: uppercase;
  font-weight: 600;
  display: inline-block;
}
.lf2-btn-ghost:hover { background: #fff; color: #000; }

/* ===== MARQUEE VERT — directement sous hero ===== */
.lf2-marquee-wrap {
  background: #36B7B2;
  overflow: hidden;
  padding: 15px 0;
  white-space: nowrap;
}
.lf2-marquee-track {
  display: inline-flex;
  animation: lf2-scroll 35s linear infinite;
}
.lf2-marquee-track span {
  font-size: .72rem;
  font-weight: 800;
  letter-spacing: .25em;
  text-transform: uppercase;
  color: #fff;
  padding: 0 36px;
}
.lf2-marquee-track span::after {
  content: '·';
  margin-left: 36px;
  opacity: .5;
}
@keyframes lf2-scroll {
  from { transform: translateX(0); }
  to   { transform: translateX(-50%); }
}

/* ===== NARRATIVE ===== */
.lf2-narrative {
  display: grid;
  grid-template-columns: 1fr 1fr;
  min-height: 80vh;
}
.lf2-narrative-img {
  overflow: hidden;
  background: #222;
  position: relative;
  min-height: 500px;
}
.lf2-narrative-img img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
  display: block;
  position: absolute;
  inset: 0;
  filter: contrast(1.08) saturate(1.1);
}
.lf2-narrative-text {
  background: #1a1a1a;
  color: #fff;
  display: flex;
  align-items: center;
  padding: 80px 70px;
}
.lf2-narrative-inner { max-width: 460px; }
.lf2-eyebrow {
  font-size: .68rem;
  letter-spacing: .35em;
  text-transform: uppercase;
  color: #36B7B2;
  margin-bottom: 1.5rem;
  display: block;
  font-weight: 700;
}
.lf2-narrative-text h2 {
  font-size: clamp(2rem, 3vw, 2.8rem);
  font-weight: 800;
  line-height: 1.1;
  margin: 0 0 1.5rem;
  color: #fff;
}
.lf2-narrative-text p {
  font-size: 1rem;
  line-height: 1.9;
  color: #aaa;
  font-weight: 300;
  margin-bottom: 2rem;
}
.lf2-link-arrow {
  color: #36B7B2;
  text-decoration: none;
  font-size: .8rem;
  letter-spacing: .15em;
  text-transform: uppercase;
  font-weight: 700;
  border-bottom: 1px solid #36B7B2;
  padding-bottom: 2px;
}

/* ===== COLLECTION ===== */
.lf2-collection {
  padding: 100px 6vw;
  background: #f4f4f2;
}
.lf2-collection-header {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  margin-bottom: 60px;
}
.lf2-collection-header h2 {
  font-size: clamp(3rem, 6vw, 5rem);
  font-weight: 900;
  letter-spacing: -.04em;
  margin: 0;
  text-transform: uppercase;
  color: #111;
}
.lf2-collection-header a {
  color: #111;
  text-decoration: none;
  font-size: .75rem;
  letter-spacing: .18em;
  text-transform: uppercase;
  border-bottom: 2px solid #111;
  font-weight: 700;
  padding-bottom: 2px;
}
.lf2-grid-3 {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 3px;
  background: #ddd;
}
.lf2-product-tile { background: #fff; overflow: hidden; }
.lf2-product-img-wrap {
  overflow: hidden;
  aspect-ratio: 1/1;
  background: #f5f5f5;
}
.lf2-product-img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  display: block;
  padding: 24px;
  transition: transform .5s;
}
.lf2-product-tile:hover .lf2-product-img { transform: scale(1.06); }
.lf2-product-info { padding: 24px 28px 36px; border-top: 1px solid #eee; }
.lf2-product-tag {
  font-size: .62rem;
  letter-spacing: .22em;
  text-transform: uppercase;
  color: #36B7B2;
  margin-bottom: 6px;
  display: block;
  font-weight: 700;
}
.lf2-product-name { font-size: 1.3rem; font-weight: 800; margin: 0 0 6px; color: #111; }
.lf2-product-tagline { font-size: .88rem; color: #777; font-weight: 300; margin: 0 0 16px; }
.lf2-product-price { font-size: 1.05rem; font-weight: 700; color: #111; }
.lf2-product-cta {
  display: inline-block;
  margin-top: 14px;
  font-size: .72rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: #36B7B2;
  text-decoration: none;
  font-weight: 700;
  border-bottom: 2px solid #36B7B2;
}

/* ===== SPLIT ===== */
.lf2-split {
  display: grid;
  grid-template-columns: 1fr 1fr;
  min-height: 90vh;
}
.lf2-split-panel {
  position: relative;
  overflow: hidden;
  display: flex;
  align-items: flex-end;
  padding: 60px;
  min-height: 500px;
}
.lf2-split-panel video {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.lf2-split-panel-bg { position: absolute; inset: 0; }
.lf2-split-panel-bg img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
  display: block;
  filter: contrast(1.12) saturate(1.1);
}
.lf2-split-grad {
  position: absolute;
  inset: 0;
  background: linear-gradient(to top, rgba(0,0,0,.9) 0%, rgba(0,0,0,.3) 55%, rgba(0,0,0,.05) 100%);
}
.lf2-split-content { position: relative; z-index: 1; color: #fff; }
.lf2-split-content h3 {
  font-size: clamp(2rem, 3.5vw, 3.2rem);
  font-weight: 900;
  margin: 0 0 .6rem;
  text-transform: uppercase;
  line-height: 1;
  text-shadow: 0 2px 20px rgba(0,0,0,.5);
}
.lf2-split-content p {
  font-size: .95rem;
  color: rgba(255,255,255,.85);
  margin: 0 0 1.8rem;
  font-weight: 300;
  max-width: 300px;
  line-height: 1.7;
}
.lf2-btn-white {
  padding: 14px 40px;
  border: 2px solid #fff;
  color: #fff;
  text-decoration: none;
  font-size: .75rem;
  letter-spacing: .18em;
  text-transform: uppercase;
  font-weight: 700;
  display: inline-block;
  transition: all .3s;
}
.lf2-btn-white:hover { background: #fff; color: #000; }

/* ===== LIFTX ===== */
.lf2-liftx-section {
  padding: 100px 6vw;
  background: #eeede9;
}
.lf2-liftx-inner {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 80px;
  align-items: center;
  max-width: 1300px;
  margin: 0 auto;
}
.lf2-liftx-text h2 {
  font-size: clamp(2.5rem, 4.5vw, 4rem);
  font-weight: 900;
  margin: 0 0 1.5rem;
  text-transform: uppercase;
  line-height: 1;
  color: #111;
}
.lf2-liftx-text h2 .x { color: #36B7B2; }
.lf2-liftx-text p {
  font-size: 1rem;
  line-height: 1.85;
  color: #555;
  margin-bottom: 2rem;
  font-weight: 300;
}
.lf2-liftx-tags { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 2.5rem; }
.lf2-tag {
  padding: 7px 18px;
  border: 2px solid #bbb;
  font-size: .68rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: #444;
  font-weight: 600;
}
.lf2-liftx-img img { width: 100%; height: auto; display: block; }
.lf2-btn-dark {
  padding: 16px 48px;
  background: #111;
  color: #fff;
  text-decoration: none;
  font-size: .78rem;
  letter-spacing: .15em;
  text-transform: uppercase;
  font-weight: 700;
  display: inline-block;
}

/* ===== SPECS ===== */
.lf2-specs-section {
  padding: 110px 6vw;
  background: #1c1c1c;
  color: #fff;
}
.lf2-specs-title { text-align: center; margin-bottom: 80px; }
.lf2-specs-title .lf2-eyebrow { display: block; text-align: center; }
.lf2-specs-title h2 {
  font-size: clamp(2.5rem, 5vw, 4.5rem);
  font-weight: 900;
  color: #fff;
  margin: .5rem 0 0;
  text-transform: uppercase;
  letter-spacing: -.03em;
}
.lf2-specs-layout {
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  gap: 40px;
  align-items: center;
  max-width: 1200px;
  margin: 0 auto;
}
.lf2-specs-col { display: flex; flex-direction: column; gap: 40px; }
.lf2-spec-item { display: flex; flex-direction: column; gap: 4px; }
.lf2-spec-item.right { text-align: right; }
.lf2-spec-val {
  font-size: 3rem;
  font-weight: 900;
  color: #36B7B2;
  line-height: 1;
  letter-spacing: -.02em;
}
.lf2-spec-label {
  font-size: .65rem;
  letter-spacing: .22em;
  text-transform: uppercase;
  color: #888;
  font-weight: 600;
}
.lf2-spec-desc { font-size: .82rem; color: #555; margin-top: 2px; font-weight: 300; }
.lf2-specs-img { text-align: center; padding: 0 20px; }
.lf2-specs-img img {
  width: 100%;
  max-width: 380px;
  height: auto;
  filter: drop-shadow(0 30px 80px rgba(54,183,178,.25));
}

/* ===== FEATURES ===== */
.lf2-features-section {
  padding: 110px 6vw;
  background: #f4f4f2;
}
.lf2-features-section h2 {
  font-size: clamp(2rem, 4vw, 3.2rem);
  font-weight: 800;
  text-align: center;
  margin: 0 0 80px;
  color: #111;
}
.lf2-features-grid {
  display: grid;
  grid-template-columns: repeat(4,1fr);
  gap: 3px;
  background: #ddd;
  max-width: 100%;
}
.lf2-feat {
  text-align: center;
  padding: 50px 24px;
  background: #fff;
}
.lf2-feat-num {
  font-size: 4.5rem;
  font-weight: 900;
  color: #36B7B2;
  display: block;
  margin-bottom: .4rem;
  line-height: 1;
  letter-spacing: -.02em;
}
.lf2-feat h3 {
  font-size: .75rem;
  font-weight: 700;
  margin: 0 0 .8rem;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: #111;
}
.lf2-feat p { font-size: .88rem; color: #777; font-weight: 300; line-height: 1.7; }

/* ===== LIFESTYLE GRID ===== */
.lf2-lifestyle-section {
  background: #eeecea;
  padding: 100px 6vw;
}
.lf2-lifestyle-head {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  margin-bottom: 60px;
}
.lf2-lifestyle-head h2 {
  font-size: clamp(2.5rem, 5vw, 4rem);
  font-weight: 900;
  letter-spacing: -.04em;
  margin: 0;
  text-transform: uppercase;
  color: #111;
}
.lf2-lifestyle-head a {
  color: #111;
  font-size: .72rem;
  letter-spacing: .18em;
  text-transform: uppercase;
  font-weight: 700;
  text-decoration: none;
  border-bottom: 2px solid #111;
  padding-bottom: 2px;
}
.lf2-lifestyle-tiles {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 4px;
  background: #ccc;
}
.lf2-lifestyle-tile {
  position: relative;
  overflow: hidden;
  background: #333;
  aspect-ratio: 3/4;
}
.lf2-lifestyle-tile img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
  display: block;
  transition: transform .6s ease;
}
.lf2-lifestyle-tile:hover img { transform: scale(1.05); }
.lf2-lifestyle-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(to top, rgba(0,0,0,.82) 0%, transparent 55%);
  display: flex;
  align-items: flex-end;
  padding: 28px 24px;
}
.lf2-lifestyle-label { color: #fff; }
.lf2-lifestyle-label span {
  display: block;
  font-size: .6rem;
  letter-spacing: .28em;
  text-transform: uppercase;
  color: #36B7B2;
  font-weight: 700;
  margin-bottom: 4px;
}
.lf2-lifestyle-label h3 {
  font-size: 1.4rem;
  font-weight: 800;
  margin: 0;
  text-transform: uppercase;
  line-height: 1;
  color: #fff;
}

/* ===== YOUTUBE ===== */
.lf2-youtube-section {
  background: #f4f4f2;
  padding: 100px 6vw;
}
.lf2-yt-header { text-align: center; margin-bottom: 60px; }
.lf2-yt-header .lf2-eyebrow { color: #36B7B2; display: block; text-align: center; }
.lf2-yt-header h2 {
  font-size: clamp(2rem, 4vw, 3.5rem);
  font-weight: 900;
  color: #111;
  margin: .5rem 0 0;
  text-transform: uppercase;
}
.lf2-yt-grid {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 16px;
  max-width: 1300px;
  margin: 0 auto;
}
.lf2-yt-card {
  background: #fff;
  overflow: hidden;
  box-shadow: 0 2px 20px rgba(0,0,0,.1);
  cursor: pointer;
}
.lf2-yt-thumb {
  position: relative;
  aspect-ratio: 16/9;
  overflow: hidden;
  background: #111;
}
.lf2-yt-thumb img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: transform .4s;
}
.lf2-yt-card:hover .lf2-yt-thumb img { transform: scale(1.04); }
.lf2-yt-play {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
}
.lf2-yt-play-btn {
  width: 60px;
  height: 60px;
  background: rgba(255,255,255,.95);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 20px rgba(0,0,0,.3);
  transition: transform .25s;
}
.lf2-yt-card:hover .lf2-yt-play-btn { transform: scale(1.15); }
.lf2-yt-play-icon {
  width: 0;
  height: 0;
  border-top: 11px solid transparent;
  border-bottom: 11px solid transparent;
  border-left: 20px solid #ff0000;
  margin-left: 5px;
}
.lf2-yt-info { padding: 16px 18px 20px; }
.lf2-yt-info h4 { font-size: .88rem; font-weight: 700; color: #111; margin: 0 0 5px; line-height: 1.4; }
.lf2-yt-info p { font-size: .72rem; color: #999; margin: 0; }
.lf2-yt-cta { text-align: center; margin-top: 48px; }
.lf2-yt-cta a {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  padding: 16px 48px;
  background: #ff0000;
  color: #fff;
  text-decoration: none;
  font-size: .78rem;
  letter-spacing: .15em;
  text-transform: uppercase;
  font-weight: 700;
}
.lf2-yt-cta a:hover { background: #cc0000; }

/* ===== VIDEO FINALE ===== */
.lf2-video-full {
  position: relative;
  height: 85vh;
  min-height: 500px;
  overflow: hidden;
  background: #000;
}
.lf2-video-full video {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}
.lf2-video-overlay {
  position: absolute;
  inset: 0;
  background: rgba(0,0,0,.45);
  display: flex;
  align-items: center;
  justify-content: center;
}
.lf2-video-overlay-text { text-align: center; color: #fff; }
.lf2-video-overlay-text p {
  font-size: clamp(2.5rem, 6vw, 5rem);
  font-weight: 900;
  margin: 0 0 2.5rem;
  text-transform: uppercase;
  line-height: 1;
  text-shadow: 0 4px 30px rgba(0,0,0,.5);
}
.lf2-video-overlay-text a {
  display: inline-block;
  padding: 18px 60px;
  background: #36B7B2;
  color: #fff;
  text-decoration: none;
  font-size: .8rem;
  letter-spacing: .2em;
  text-transform: uppercase;
  font-weight: 700;
}

/* ===== RESPONSIVE ===== */
@media(max-width:900px){
  .lf2-grid-3, .lf2-lifestyle-tiles, .lf2-yt-grid { grid-template-columns: 1fr 1fr; }
  .lf2-narrative, .lf2-split, .lf2-liftx-inner { grid-template-columns: 1fr; }
  .lf2-narrative-img { min-height: 400px; }
  .lf2-features-grid { grid-template-columns: repeat(2,1fr); }
  .lf2-narrative-text { padding: 60px 40px; }
  .lf2-specs-layout { grid-template-columns: 1fr 1fr; }
  .lf2-specs-img { grid-column: 1/-1; order: -1; }
  .lf2-spec-item.right { text-align: left; }
}
@media(max-width:600px){
  .lf2-grid-3, .lf2-lifestyle-tiles, .lf2-yt-grid { grid-template-columns: 1fr; }
  .lf2-hero-title { font-size: 3.5rem; }
  .lf2-narrative-text { padding: 50px 28px; }
  .lf2-features-grid { grid-template-columns: 1fr 1fr; }
  .lf2-specs-layout { grid-template-columns: 1fr; }
}
</style>
<!-- /wp:html -->
<!-- wp:html -->
<div class="lf2">

<!-- === HERO VIDEO PLEIN ECRAN === -->
<section class="lf2-hero">
<video autoplay muted loop playsinline poster="https://liftfoils.fr/wp-content/uploads/2025/12/Cannes_day1-177-edited.jpg">
<source src="https://liftfoils.fr/wp-content/uploads/2021/03/Lift-Foils-eFoil-Electric-Surfboard-Premium-Surf-Hydrofoils-10.mp4" type="video/mp4">
</video>
<div class="lf2-hero-grad"></div>
<div class="lf2-hero-content">
<span class="lf2-hero-eyebrow">Revendeur officiel Lift Foils France</span>
<h1 class="lf2-hero-title">FLY<br><span class="accent">OVER</span><br><span class="dim">WATER</span></h1>
<p class="lf2-hero-sub">Les eFoils les plus avanc&#233;s au monde. Disponibles en France avec essais sur la C&#244;te d&#8217;Azur.</p>
<div class="lf2-hero-actions">
<a href="/efoil-lift-foils/" class="lf2-btn-teal">Voir les eFoils</a>
<a href="/location-de-surf-electrique-a-foil-le-paddle-electrique-volant/" class="lf2-btn-ghost">R&#233;server un essai</a>
</div>
</div>
</section>

<!-- === MARQUEE VERT JUSTE SOUS LE HERO === -->
<div class="lf2-marquee-wrap">
<div class="lf2-marquee-track">
<span>eFoil</span><span>Lift Foils France</span><span>C&#244;te d&#8217;Azur</span><span>Essai gratuit</span><span>Foil &#233;lectrique</span><span>LIFT5 Pro</span><span>LIFT5 Sport</span><span>LIFT5 Cruiser</span><span>LiftX Hybride</span><span>100% carbone</span><span>Silencieux</span><span>64 km/h</span><span>eFoil</span><span>Lift Foils France</span><span>C&#244;te d&#8217;Azur</span><span>Essai gratuit</span><span>Foil &#233;lectrique</span><span>LIFT5 Pro</span><span>LIFT5 Sport</span><span>LIFT5 Cruiser</span><span>LiftX Hybride</span><span>100% carbone</span><span>Silencieux</span><span>64 km/h</span>
</div>
</div>

<!-- === NARRATIVE : photo + texte === -->
<div class="lf2-narrative">
<div class="lf2-narrative-img">
<img src="https://liftfoils.fr/wp-content/uploads/2025/12/DSC1001_RodrigoSnaps-Inc.-1-edited-scaled.jpg" alt="eFoil action Lift Foils" loading="lazy">
</div>
<div class="lf2-narrative-text">
<div class="lf2-narrative-inner">
<span class="lf2-eyebrow">Notre histoire</span>
<h2>Nous construisons des foils depuis avant que ce mot existait</h2>
<p>Lift Foils est n&#233; d&#8217;une passion absolue pour la glisse. Plus de 15 ans de R&amp;D, des mat&#233;riaux a&#233;rospatiaux, des ing&#233;nieurs obss&#233;d&#233;s par la perfection.</p>
<a href="/efoil-lift-foils/" class="lf2-link-arrow">D&#233;couvrir notre gamme &#8594;</a>
</div>
</div>
</div>

<!-- === COLLECTION LIFT5 === -->
<section class="lf2-collection">
<div class="lf2-collection-header">
<h2>LIFT<span style="color:#36B7B2">5</span></h2>
<a href="/efoil-lift5-decouvrez-le-nouveau-foil-electrique-lift-5/">Voir toute la gamme &#8594;</a>
</div>
<div class="lf2-grid-3">
<div class="lf2-product-tile">
<div class="lf2-product-img-wrap">
<img class="lf2-product-img" src="https://cdn.shopify.com/s/files/1/0607/0907/7155/files/2025_LIFT5_4_4_SUNKISSED_Package_Iso_Shadow_2000x2000_07c630aa-b1ef-4ab3-b824-407ba3d03c1f.png" alt="LIFT5 Pro" loading="lazy">
</div>
<div class="lf2-product-info">
<span class="lf2-product-tag">Expert &#183; Carving pr&#233;cis</span>
<h3 class="lf2-product-name">Lift5 Pro 4&#8217;4&#8221;</h3>
<p class="lf2-product-tagline">Le plus l&#233;ger. Le plus vif.</p>
<div class="lf2-product-price">&#192; partir de 13&#8239;499&#160;&#8364;</div>
<a href="/efoil-lift5-pro-44-lefoil-lift-expert-pour-le-carving-precis/" class="lf2-product-cta">D&#233;couvrir &#8594;</a>
</div>
</div>
<div class="lf2-product-tile">
<div class="lf2-product-img-wrap">
<img class="lf2-product-img" src="https://cdn.shopify.com/s/files/1/0607/0907/7155/files/2025_LIFT5_4_9_STEELBLUE_Package_Iso_Shadow_2000x2000_5a4014ba-a3ec-4a38-8006-2e4d32168877.png" alt="LIFT5 Sport" loading="lazy">
</div>
<div class="lf2-product-info">
<span class="lf2-product-tag">Polyvalent &#183; Tous niveaux</span>
<h3 class="lf2-product-name">Lift5 Sport 4&#8217;9&#8221;</h3>
<p class="lf2-product-tagline">L&#8217;&#233;quilibre parfait.</p>
<div class="lf2-product-price">&#192; partir de 13&#8239;499&#160;&#8364;</div>
<a href="/efoil-lift5-sport-49-lefoil-lift-adaptable-pour-tous-les-terrains/" class="lf2-product-cta">D&#233;couvrir &#8594;</a>
</div>
</div>
<div class="lf2-product-tile">
<div class="lf2-product-img-wrap">
<img class="lf2-product-img" src="https://cdn.shopify.com/s/files/1/0607/0907/7155/files/2025_LIFT5_5_4_CARBONBLACK_Package_Iso_Shadow_2000x2000_c59a7777-4dde-4045-8362-15f929401768.png" alt="LIFT5 Cruiser" loading="lazy">
</div>
<div class="lf2-product-info">
<span class="lf2-product-tag">D&#233;butants &#183; Familles</span>
<h3 class="lf2-product-name">Lift5 Cruiser 5&#8217;4&#8221;</h3>
<p class="lf2-product-tagline">Stabilit&#233; maximale.</p>
<div class="lf2-product-price">&#192; partir de 13&#8239;499&#160;&#8364;</div>
<a href="/efoil-lift5-cruiser-54-lefoil-lift-serenite-pour-debutants-et-familles/" class="lf2-product-cta">D&#233;couvrir &#8594;</a>
</div>
</div>
</div>
</section>

<!-- === SPLIT 2 PANNEAUX === -->
<div class="lf2-split">
<div class="lf2-split-panel">
<div class="lf2-split-panel-bg">
<img src="https://liftfoils.fr/wp-content/uploads/2025/12/Lift_sunrise-120-scaled-edited.jpg" alt="Glisse pure eFoil">
</div>
<div class="lf2-split-grad"></div>
<div class="lf2-split-content">
<h3>Glisse pure.<br>Silence total.</h3>
<p>Le moteur brushless Lift ne fait aucun bruit. Seul le vent et l&#8217;eau.</p>
<a href="/efoil-lift5-decouvrez-le-nouveau-foil-electrique-lift-5/" class="lf2-btn-white">LIFT5</a>
</div>
</div>
<div class="lf2-split-panel">
<video autoplay muted loop playsinline>
<source src="https://liftfoils.fr/wp-content/uploads/2021/03/LIFTX-eFoil-Hybrid-eFoil-Beyond-Foil-Assist-for-Surf-Progression-3.mp4" type="video/mp4">
</video>
<div class="lf2-split-grad"></div>
<div class="lf2-split-content">
<h3>Au-del&#224;<br>du foil.</h3>
<p>LiftX&#160;: surf, wing, tow. L&#8217;assistance &#233;lectrique qui transforme tout.</p>
<a href="/efoil-lift-x-le-foil-electrique-reinvente-surf-foil-hybride-motorise/" class="lf2-btn-white">LIFT X</a>
</div>
</div>
</div>

<!-- === LIFTX === -->
<section class="lf2-liftx-section">
<div class="lf2-liftx-inner">
<div class="lf2-liftx-text">
<span class="lf2-eyebrow">Nouveau &#183; 2025</span>
<h2>LIFT<span class="x">X</span><br>Le foil hybride<br>r&#233;invent&#233;</h2>
<p>LiftX va au-del&#224; du simple eFoil. Con&#231;u pour le surf, le wing et le tow foil, il apporte une assistance &#233;lectrique intelligente.</p>
<div class="lf2-liftx-tags">
<span class="lf2-tag">eFoil</span>
<span class="lf2-tag">Wing Foil</span>
<span class="lf2-tag">Surf Foil</span>
<span class="lf2-tag">Tow Foil</span>
</div>
<a href="/efoil-lift-x-le-foil-electrique-reinvente-surf-foil-hybride-motorise/" class="lf2-btn-dark">D&#233;couvrir LiftX</a>
</div>
<div class="lf2-liftx-img">
<img src="https://liftfoils.fr/wp-content/uploads/2026/02/2025_LIFTX_43_DAWNPATROL_Package_Iso_Shadow_2000x2000.png" alt="LiftX 2025" loading="lazy">
</div>
</div>
</section>

<!-- === SPECS PRODUIT === -->
<section class="lf2-specs-section">
<div class="lf2-specs-title">
<span class="lf2-eyebrow">Technologie</span>
<h2>Fait pour voler</h2>
</div>
<div class="lf2-specs-layout">
<div class="lf2-specs-col">
<div class="lf2-spec-item">
<span class="lf2-spec-val">120</span>
<span class="lf2-spec-label">Minutes d&#8217;autonomie</span>
<span class="lf2-spec-desc">Batterie lithium haute densit&#233;</span>
</div>
<div class="lf2-spec-item">
<span class="lf2-spec-val">100%</span>
<span class="lf2-spec-label">Carbone</span>
<span class="lf2-spec-desc">Board et foil en carbone a&#233;rospatial</span>
</div>
<div class="lf2-spec-item">
<span class="lf2-spec-val">64</span>
<span class="lf2-spec-label">km/h max</span>
<span class="lf2-spec-desc">Vitesse de pointe en mode expert</span>
</div>
</div>
<div class="lf2-specs-img">
<img src="https://liftfoils.fr/wp-content/uploads/2026/02/2025_LIFT5_44_STEELBLUE_Package_Iso_Shadow_2000x2000.png" alt="Lift5 Steel Blue" loading="lazy">
</div>
<div class="lf2-specs-col">
<div class="lf2-spec-item right">
<span class="lf2-spec-val">0</span>
<span class="lf2-spec-label">C&#226;bles ext&#233;rieurs</span>
<span class="lf2-spec-desc">Design totalement int&#233;gr&#233;</span>
</div>
<div class="lf2-spec-item right">
<span class="lf2-spec-val">50</span>
<span class="lf2-spec-label">Min de recharge</span>
<span class="lf2-spec-desc">Chargeur rapide inclus</span>
</div>
<div class="lf2-spec-item right">
<span class="lf2-spec-val">24</span>
<span class="lf2-spec-label">kg tout compris</span>
<span class="lf2-spec-desc">Le plus l&#233;ger de sa cat&#233;gorie</span>
</div>
</div>
</div>
</section>

<!-- === FEATURES STATS === -->
<section class="lf2-features-section">
<h2>Technologie de r&#233;f&#233;rence mondiale</h2>
<div class="lf2-features-grid">
<div class="lf2-feat">
<span class="lf2-feat-num">15+</span>
<h3>Ann&#233;es de R&amp;D</h3>
<p>Pionniers du foil &#233;lectrique depuis 2010.</p>
</div>
<div class="lf2-feat">
<span class="lf2-feat-num">40+</span>
<h3>km/h</h3>
<p>Motorisation brushless ultra-silencieuse.</p>
</div>
<div class="lf2-feat">
<span class="lf2-feat-num">90+</span>
<h3>Min d&#8217;autonomie</h3>
<p>Batteries lithium haute densit&#233;.</p>
</div>
<div class="lf2-feat">
<span class="lf2-feat-num">0 dB</span>
<h3>Silencieux</h3>
<p>Aucun bruit de moteur, juste la nature.</p>
</div>
</div>
</section>

<!-- === LIFESTYLE GRID 3 COLONNES === -->
<section class="lf2-lifestyle-section">
<div class="lf2-lifestyle-head">
<h2>Nos sessions</h2>
<a href="/location-de-surf-electrique-a-foil-le-paddle-electrique-volant/">Voir les essais &#8594;</a>
</div>
<div class="lf2-lifestyle-tiles">
<div class="lf2-lifestyle-tile">
<img src="https://liftfoils.fr/wp-content/uploads/2025/12/Cannes_day1-177-edited.jpg" alt="Session Cannes eFoil" loading="lazy">
<div class="lf2-lifestyle-overlay">
<div class="lf2-lifestyle-label">
<span>C&#244;te d&#8217;Azur</span>
<h3>Cannes</h3>
</div>
</div>
</div>
<div class="lf2-lifestyle-tile">
<img src="https://liftfoils.fr/wp-content/uploads/2025/12/Lift_sunrise-71-e1677709687465-edited.jpg" alt="eFoil lever du soleil" loading="lazy">
<div class="lf2-lifestyle-overlay">
<div class="lf2-lifestyle-label">
<span>Session</span>
<h3>Lever du soleil</h3>
</div>
</div>
</div>
<div class="lf2-lifestyle-tile">
<img src="https://liftfoils.fr/wp-content/uploads/2026/01/Foilin_paris-357-scaled.jpg" alt="Foilin Paris" loading="lazy">
<div class="lf2-lifestyle-overlay">
<div class="lf2-lifestyle-label">
<span>Paris</span>
<h3>Sur la Seine</h3>
</div>
</div>
</div>
</div>
</section>

<!-- === YOUTUBE CARROUSEL — vrais IDs de la chaine @liftfoils === -->
<section class="lf2-youtube-section">
<div class="lf2-yt-header">
<span class="lf2-eyebrow">Notre cha&#238;ne YouTube</span>
<h2>Lift Foils en vid&#233;o</h2>
</div>
<div class="lf2-yt-grid">
<div class="lf2-yt-card" onclick="window.open('https://www.youtube.com/watch?v=n9I_tRjQ_k0','_blank')">
<div class="lf2-yt-thumb">
<img src="https://img.youtube.com/vi/n9I_tRjQ_k0/mqdefault.jpg" alt="Lift Foils video" loading="lazy">
<div class="lf2-yt-play"><div class="lf2-yt-play-btn"><div class="lf2-yt-play-icon"></div></div></div>
</div>
<div class="lf2-yt-info">
<h4>Lift Foils &#8212; LIFT5 Official</h4>
<p>@liftfoils</p>
</div>
</div>
<div class="lf2-yt-card" onclick="window.open('https://www.youtube.com/watch?v=5cmGpMZI7Kc','_blank')">
<div class="lf2-yt-thumb">
<img src="https://img.youtube.com/vi/5cmGpMZI7Kc/mqdefault.jpg" alt="Lift Foils video" loading="lazy">
<div class="lf2-yt-play"><div class="lf2-yt-play-btn"><div class="lf2-yt-play-icon"></div></div></div>
</div>
<div class="lf2-yt-info">
<h4>Lift Foils &#8212; LiftX Hybrid</h4>
<p>@liftfoils</p>
</div>
</div>
<div class="lf2-yt-card" onclick="window.open('https://www.youtube.com/watch?v=W1aA0mURZQg','_blank')">
<div class="lf2-yt-thumb">
<img src="https://img.youtube.com/vi/W1aA0mURZQg/mqdefault.jpg" alt="Lift Foils video" loading="lazy">
<div class="lf2-yt-play"><div class="lf2-yt-play-btn"><div class="lf2-yt-play-icon"></div></div></div>
</div>
<div class="lf2-yt-info">
<h4>Lift Foils &#8212; Electric Surfboard</h4>
<p>@liftfoils</p>
</div>
</div>
</div>
<div class="lf2-yt-cta">
<a href="https://www.youtube.com/@liftfoils" target="_blank" rel="noopener noreferrer">
&#9654; Voir toutes nos vid&#233;os sur YouTube
</a>
</div>
</section>

<!-- === VIDEO FINALE === -->
<section class="lf2-video-full">
<video autoplay muted loop playsinline>
<source src="https://liftfoils.fr/wp-content/uploads/2021/03/Lift-Foils-eFoil-Lift-5-vue-drone.mp4" type="video/mp4">
</video>
<div class="lf2-video-overlay">
<div class="lf2-video-overlay-text">
<p>Pr&#234;t &#224; voler<br>sur l&#8217;eau&#160;?</p>
<a href="/location-de-surf-electrique-a-foil-le-paddle-electrique-volant/">R&#233;server votre essai</a>
</div>
</div>
</section>

</div>
<!-- SCRIPT : force plein ecran via JS pour Atelier -->
<script>
(function(){
  var lf2 = document.querySelector('.lf2');
  if(!lf2) return;
  // Remonter jusqu'au body et neutraliser tous les wrappers
  var el = lf2.parentElement;
  while(el && el !== document.body){
    el.style.maxWidth = 'none';
    el.style.width = '100%';
    el.style.paddingLeft = '0';
    el.style.paddingRight = '0';
    el.style.marginLeft = '0';
    el.style.marginRight = '0';
    el = el.parentElement;
  }
  // Supprimer aussi les paddings sur .entry-content si present
  var ec = document.querySelector('.entry-content');
  if(ec){
    ec.style.padding = '0';
    ec.style.maxWidth = 'none';
  }
})();
</script>
<!-- /wp:html -->"""

creds = base64.b64encode(b"bakari06@live.fr:sbXs yBir OURU h0vQ ubXa pBtN").decode()
payload = json.dumps({"content": html}).encode("utf-8")

req = urllib.request.Request(
    "https://liftfoils.fr/wp-json/wp/v2/pages/29946",
    data=payload,
    method="POST",
    headers={
        "Authorization": "Basic " + creds,
        "Content-Type": "application/json",
        "X-HTTP-Method-Override": "PUT",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
)
try:
    with urllib.request.urlopen(req) as r:
        resp = json.loads(r.read())
        print("OK - modified:", resp.get("modified"), "| status:", resp.get("status"))
        content = resp.get("content",{}).get("raw","")
        print("Content length:", len(content))
        print("Starts with:", content[:80])
except urllib.error.HTTPError as e:
    print("ERROR", e.code, e.read()[:400])

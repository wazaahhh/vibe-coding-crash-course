---
marp: true
paginate: true
size: 16:9
title: "FacMed Hack #1 — Crash Course #2, 22 October 2026"
author: Faculty of Medicine, UNIGE
style: |
  /* FacMed Hack edition of Vibe Coding for Scientists. FacMed hackathon design system — tokens verbatim from
     apps/facmed-hack/workers/api/src/site/styles.ts, as in Crash Course #1.
     Ink ground for the title and the moments the room does the work
     (opening question, quiz); light ground for everything else. */
  :root {
    --ink: #11233F;
    --accent: #96004B;        /* UNIGE burgundy */
    --science: #4FA5B8;       /* teal */
    --energy: #6E7CF6;        /* periwinkle */
    --accent-soft: #EBCFDC;
    --science-soft: #D9F0F4;
    --energy-soft: #E3E7FF;
    --bg-soft: #F7F9FC;
    --bg-inset: #EEF4FA;
    --fg-muted: #4D5B73;
    --fg-faint: #7C8AA1;
    --line: #D7E1EC;
    --on-ink: #F2F6FB;
    --on-ink-muted: #A9B8CE;
  }
  section {
    font-family: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    font-size: 25px;
    background: #ffffff;
    color: var(--ink);
    line-height: 1.4;
    padding: 46px 64px 54px;
    display: block !important;
  }
  p { margin: 0 0 0.6em; }
  ul, ol { margin: 0 0 0.6em; padding-left: 1.2em; }
  li { margin-bottom: 0.28em; }
  h1, h2, h3 { color: var(--ink); letter-spacing: -0.018em; line-height: 1.16; margin: 0; }
  h1 { font-size: 1.9em; font-weight: 800; }
  h2 {
    display: inline-block; font-size: 1.45em; font-weight: 700;
    border-bottom: 3px solid var(--accent);
    padding-bottom: 6px; margin-bottom: 0.55em;
  }
  h3 { font-size: 1.0em; font-weight: 700; margin-bottom: 0.25em; }
  strong { color: var(--accent); }
  a { color: var(--accent); text-decoration: none; }
  .kicker {
    display: block; font-size: 0.62em; font-weight: 700; letter-spacing: 0.12em;
    text-transform: uppercase; color: var(--fg-faint); margin-bottom: 6px;
  }
  .small { font-size: 0.74em; color: var(--fg-muted); }
  .muted { color: var(--fg-muted); }
  blockquote {
    margin: 0.3em 0 0.7em; padding: 14px 22px; border: 0;
    border-left: 5px solid var(--accent); background: var(--bg-soft);
    border-radius: 0 12px 12px 0; color: var(--ink); font-size: 1.05em;
  }
  blockquote p { margin: 0; }

  /* House table: uppercase faint headers over hairline rules, no fills. */
  table, thead, tbody, tr { background: transparent !important; color: inherit; }
  table { border-collapse: collapse; font-size: 0.78em; width: 100%; display: table; }
  th, td { border: 0; border-bottom: 1px solid var(--line); padding: 8px 12px 8px 0; text-align: left; vertical-align: top; background: transparent !important; }
  th { font-size: 0.72em; letter-spacing: 0.08em; text-transform: uppercase; color: var(--fg-faint); font-weight: 700; }
  tr:last-child td { border-bottom: 0; }

  /* Layout helpers */
  .cols { display: grid; grid-template-columns: 1fr 1fr; gap: 34px; }
  .card { background: var(--bg-soft); border: 1px solid var(--line); border-radius: 14px; padding: 16px 20px; }
  .card h3 { margin-bottom: 0.3em; }
  .card p { font-size: 0.8em; margin: 0; color: var(--fg-muted); }
  .clock {
    position: absolute; top: 40px; right: 64px;
    font-size: 0.8em; font-weight: 700; color: var(--accent);
    background: var(--accent-soft); padding: 4px 14px; border-radius: 8px;
  }
  footer { color: var(--fg-faint); font-size: 0.5em; left: 64px; }
  section::after { color: var(--fg-faint); font-size: 0.55em; }
  /* Slide numbers: n / total. Backup slides use <!-- _paginate: skip -->, which hides
     their number and leaves them out of the count. */
  section::after { content: attr(data-marpit-pagination) ' / ' attr(data-marpit-pagination-total); }

  /* Quiz: four answer cards in a 2 × 2 grid, letter badge on the left. */
  .opts { display: grid; grid-template-columns: 1fr 1fr; gap: 14px 22px; margin-top: 6px; }
  .opt {
    display: flex; align-items: center; gap: 16px;
    background: var(--bg-soft); border: 1px solid var(--line); border-radius: 14px;
    padding: 14px 18px; font-size: 0.86em; line-height: 1.3;
  }
  .opt b {
    flex: none; width: 40px; height: 40px; border-radius: 10px;
    display: flex; align-items: center; justify-content: center;
    background: var(--accent); color: #fff; font-size: 1.05em;
  }
  .qnum { font-size: 0.62em; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; color: var(--accent); }

  /* Ink slides: title, opening question, quiz cover */
  section.ink {
    background: radial-gradient(900px 520px at 88% 8%, rgba(110,124,246,0.38), transparent 60%),
                radial-gradient(760px 460px at 4% 100%, rgba(79,165,184,0.30), transparent 60%),
                var(--ink);
    color: var(--on-ink);
  }
  section.ink h1, section.ink h2, section.ink h3 { color: #fff; }
  section.ink h2 { border-bottom-color: #F08BB4; }
  section.ink strong { color: #F6A9C8; }
  section.ink .kicker, section.ink .small, section.ink .muted { color: var(--on-ink-muted); }
  section.ink .clock { background: rgba(240,139,180,0.18); color: #F6A9C8; }
  section.ink .card { background: rgba(255,255,255,0.06); border-color: rgba(255,255,255,0.14); }
  section.ink .card p { color: var(--on-ink-muted); }
  section.ink blockquote { background: rgba(255,255,255,0.06); border-left-color: #F08BB4; color: var(--on-ink); }
  section.ink footer, section.ink::after { color: var(--on-ink-muted); }

  .cols3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 22px; }
  .cols4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; }
  pre { font-size: 0.62em; background: var(--bg-inset); border: 1px solid var(--line); border-radius: 12px; padding: 14px 18px; line-height: 1.35; }
  code { font-size: 0.9em; background: var(--bg-inset); border-radius: 6px; padding: 1px 6px; }
  pre code { background: transparent; padding: 0; }
  section.ink pre, section.ink code { background: rgba(255,255,255,0.08); border-color: rgba(255,255,255,0.14); color: var(--on-ink); }
  .divider h1 { font-size: 2.3em; margin-bottom: 0.3em; }
  /* Dense: for the few slides that carry a long table or two full columns. */
  section.dense { font-size: 22px; padding-top: 40px; }
  section.dense table { font-size: 0.74em; }
  section.dense th, section.dense td { padding-top: 6px; padding-bottom: 6px; }
  /* Live quiz call-out: QR code + link, bottom right of poll slides. */
  .quizbox { position: absolute; right: 64px; bottom: 58px; display: flex; align-items: center; gap: 14px;
    background: #fff; border: 2px solid var(--accent); border-radius: 14px; padding: 10px 16px 10px 10px; }
  .quizbox img { width: 112px; height: 112px; display: block; }
  .quizbox b { display: block; color: var(--accent); font-size: 0.7em; letter-spacing: 0.08em; text-transform: uppercase; }
  .quizbox span { font-size: 0.78em; font-weight: 700; color: var(--ink); }
  .quizbox.big img { width: 230px; height: 230px; }
  .quizbox.big span { font-size: 1em; }
  /* Figures with captions. */
  .fig { text-align: center; }
  .fig img { max-width: 100%; display: block; margin: 0 auto; }
  .fig .cap { font-size: 0.62em; color: var(--fg-muted); margin-top: 4px; }
  /* Full-slide quote: opening and closing bookends. */
  section.quote { display: flex !important; flex-direction: column; justify-content: center; }
  section.quote blockquote {
    font-size: 1.75em; font-weight: 700; line-height: 1.28; letter-spacing: -0.012em;
    padding: 0 0 0 34px; background: transparent; border-left: 6px solid #F08BB4; margin: 0 0 26px;
  }
  section.quote .who { font-size: 0.85em; color: var(--on-ink-muted); padding-left: 40px; }
  section.quote .who b { color: #fff; }
  .logos {
    display: flex; flex-wrap: nowrap; align-items: center; justify-content: flex-start;
    gap: 20px; background: #fff; border-radius: 14px; padding: 14px 24px; margin-top: 18px;
  }
  .logos img { height: 24px; width: auto; }
  .logos img.tall { height: 38px; }
footer: "FacMed Hack #1 · Digital Phenotyping of Mental Health · Crash Course #2 · 22 Oct 2026"
---


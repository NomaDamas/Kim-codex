# Happy Codex Computer Use MVP

Hackathon-ready one-page demo for a "happy Codex" computer-use persona.

## TLDR

This project has two deliverables:

1. Web demo URL: run `npm start`, then open `http://localhost:4173`.
2. Static HTML bundle: run `npm run bundle`, then submit `dist/index.html`.

No login, API key, secret, account connection, or network access is required.

## What the demo shows

- A lazy-but-happy Codex persona running parallel computer-use jobs.
- Simulated browser discovery across LinkedIn/Threads-style public profiles.
- Consent-safe dating outreach drafts.
- News/comment reading while procrastinating.
- A local `python-sc2` adapter run with bot-loop trace shown in the page.
- Visible Codex status text shown in the page.
- A clickable `Run full demo` mission that advances through six stages and
  generates a submission report.
- A Codex progeny lab where the original Codex splits into toy descendant
  Codexes using local prompt-genome mutation and RandomForest-style voting.
- A parallel web-surfing board for Reddit, DCInside-style community chatter,
  politics, games, stocks, and safe dating-profile browsing.
- A central Think Pad that merges Codex's visible persona observations from all
  surfing lanes.

## Safety boundary

The MVP intentionally does not send real LinkedIn connection requests, Threads DMs,
or any other message. It generates fictional, review-only drafts to satisfy the demo
flow without credentials, platform automation, spam, or account-risk behavior.

## Run locally

```sh
npm start
```

Open:

```text
http://localhost:4173
```

Then click:

```text
Run full demo
```

Expected result:

- Mission reaches `6/6 demo complete`.
- Progress reaches `100%`.
- Browser, social, SC2, and outreach status cards update.
- `python-sc2` adapter logs appear in the SC2 panel.
- The progeny nursery creates eight child Codex circles.
- The Think Pad fills with merged observations from six parallel surfing lanes.
- The report box records safe drafts, SC2 frames, progeny count, approvals, and
  `0 real DMs sent`.

## Run individual demos

SC2 adapter:

```sh
python3 scripts/sc2_codex_bot.py
```

Codex progeny lab:

```sh
python3 scripts/progeny_lab.py
```

Server APIs:

```text
GET /api/sc2-run
GET /api/progeny-run
```

## Build the static bundle

```sh
npm run bundle
```

Output:

```text
dist/index.html
```

You can open that file directly in a browser.

## Files

- `index.html`: complete one-page web demo.
- `server.js`: tiny no-dependency local static server.
- `scripts/bundle.js`: copies the one-page app into `dist/index.html`.
- `scripts/sc2_codex_bot.py`: local `python-sc2` adapter and play trace.
- `scripts/progeny_lab.py`: local Codex child-generation lab.

## Notes for judges

This is an MVP prototype focused on the product experience and submission format:
the page demonstrates the intended computer-use behaviors visually while remaining
safe, local-first, and dependency-free.

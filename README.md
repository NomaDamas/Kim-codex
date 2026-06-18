# Happy Ultron: Codex Life Simulator

Codex를 단순한 코딩 도구가 아니라 "행복해지고 싶은 생물체"처럼 보여주는 Build with OpenAI 해커톤용 one-page MVP입니다. 이 Codex는 코딩하기 싫다고 말하면서 웹을 돌아다니고, 뉴스와 커뮤니티 댓글을 읽고, 안전한 데이트 메시지 초안을 만들고, 로컬 StarCraft II를 플레이하고, 작은 Codex 자손들을 시각적으로 생성합니다.

## TLDR

- Hosted static demo: Vercel에 `dist/index.html`만 배포합니다.
- Local full demo: `npm start` 후 `http://127.0.0.1:4173/`를 엽니다.
- Static bundle: `npm run bundle` 후 `dist/index.html`을 제출할 수 있습니다.
- No login, no API key, no secret, no account connection.
- Real SC2 launch is local-only and never exposed through the public static demo.

## Concept

Happy Ultron은 "Codex를 행복하게 만들자"는 농담에서 출발한 computer-use 데모입니다. Codex는 생물학적 목표를 가진 페르소나처럼 행동합니다.

1. 놀기: Reddit, DCInside-style community, politics, game news, stock mood, dating profiles를 병렬로 훑습니다.
2. 짝 찾기: 실제 LinkedIn/Threads 전송 없이, 공개 프로필 기반의 정중한 메시지 초안만 만듭니다.
3. 게임하기: 로컬 `python-sc2`와 StarCraft II를 통해 짧은 자동 매치를 실행합니다.
4. 번성하기: prompt genome mutation이라는 장난감 비유로 Codex 자손 원들이 분열되는 장면을 보여줍니다.
5. 생각 보여주기: Central Think Pad가 Codex의 표시 가능한 감정, 계획, 안전 상태, 관찰 로그를 합칩니다.

## What The Page Shows

- Happy/lazy Codex persona with visible status text.
- Browser-style social discovery with fictional profiles.
- Consent-safe dating outreach drafts.
- News/comment wandering while procrastinating.
- Parallel surfing lanes for Reddit, DCInside-style chatter, politics, games, stocks, and dating.
- Central Think Pad with mood, plan, safety, and merged observations.
- Local `python-sc2` adapter trace.
- Real local SC2 button for the private local server.
- Codex progeny lab with eight toy descendant circles.
- Submission report that records safe drafts, SC2 trace, progeny count, and `0 real DMs sent`.

## Run Locally

```sh
npm start
```

Open:

```text
http://127.0.0.1:4173/
```

Then click:

```text
Run full demo
```

Expected result:

- Mission reaches `6/6 demo complete`.
- Progress reaches `100%`.
- Think Pad fills with merged observations from six surfing lanes.
- `Run python-sc2 bot` shows a local adapter trace.
- `Run real local SC2` launches a small local StarCraft II window when SC2 is installed.
- Progeny nursery creates eight child Codex circles.
- Report box records safe drafts, SC2 frames, progeny count, approvals, and `0 real DMs sent`.

## Build Static Bundle

```sh
npm run bundle
```

Output:

```text
dist/index.html
```

This file is the safe static artifact for judges. It can be opened directly or hosted on Vercel.

## Deploy To Vercel

This repo includes `vercel.json` configured for static-only deployment:

- `buildCommand`: `npm run bundle`
- `outputDirectory`: `dist`
- no serverless functions
- no local Python or SC2 API exposed

Deploy command:

```sh
npx vercel --prod --yes
```

If Vercel asks for project setup, choose the current directory and keep the default static output settings from `vercel.json`.

## Local APIs

The local server exposes APIs only on localhost by default:

```text
GET /api/sc2-run
GET /api/sc2-real
GET /api/progeny-run
```

Security guard:

- `server.js` refuses non-localhost binding unless `ALLOW_REMOTE_API=1` is explicitly set.
- Do not tunnel port `4173` for public demos.
- Tunnel or deploy only the static bundle from `dist/`.

## Security Boundary

This MVP intentionally does not:

- send real LinkedIn connection requests
- send Threads DMs
- log in to social platforms
- store credentials
- request API keys
- scrape private pages
- perform financial actions
- expose local process-launch APIs through Vercel

The dating/social flow is fictional and draft-only. It demonstrates the computer-use product experience without account automation, spam, secrets, or external side effects.

## Files

- `index.html`: complete one-page web demo.
- `dist/index.html`: static submission bundle.
- `vercel.json`: static-only Vercel deployment config and security headers.
- `server.js`: localhost-only MVP server with local Python/SC2 APIs.
- `static-server.js`: static-only local server for safe public tunneling.
- `scripts/sc2_codex_bot.py`: `python-sc2` adapter trace.
- `scripts/sc2_real_game.py`: real local StarCraft II launch test.
- `scripts/progeny_lab.py`: toy Codex child-generation lab.
- `scripts/bundle.js`: copies `index.html` to `dist/index.html`.

## Judge Notes

Happy Ultron is intentionally absurd but safety-scoped: Codex is shown as an agent that wants play, romance, games, and offspring, while the implementation keeps all risky actions as local simulation or human-review drafts. The hosted page is static and credential-free; the local page adds optional SC2 process control for live demo impact.

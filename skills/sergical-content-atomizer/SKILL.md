---
name: sergical-content-atomizer
description: Turns one real thing Sergiy Dybskiy built, shipped or presented (a repo, a PR, a livestream, a talk, an Article) into native pieces for the three places he actually posts, X first, YouTube second (angle only, packaging goes through his DevEx app), LinkedIn third. Skips every platform he doesn't run. Every piece is a draft with a source link and a one-line reason grounded in his own numbers. Never posts or schedules. Adapted from boring-marketing-skills/content-atomizer 4.1.1.
when_to_use: atomize serg build, serg build in public posts, turn serg livestream into posts, serg posts from this pr, repurpose serg talk, serg linkedin from this, serg youtube angle
argument-hint: "[repo, PR, doc, livestream, talk or Article URL or path]"
metadata:
  boring:
    version: 4.1.1-sergical.1
    adapted-from: content-atomizer 4.1.1
    layer: distribution
---

# sergical content atomizer

One real piece in, the few native pieces it deserves out. Depth on his three
platforms, nothing anywhere else. Fork of `content-atomizer`; what changed and why
is in `ADAPTATION.md`.

## Hard rules

1. **Drafts only.** Never post, schedule, upload or comment. No Zernio, Buffer,
   LinkedIn or YouTube write tools.
2. **Only sourced facts.** Every number and claim traces to a link or file read
   this session. Unverified means labelled `[unverified: ...]`, and at most one per
   piece.
3. **Private sources: lessons and ratios only.** Private repos (`sergical/fleet`
   and the like), internal company data, and anything with hostnames, machine
   names, token or secret names, internal paths or dollar amounts never appear.
   If the story only works with a private detail, skip that piece and say so.
4. **Never pitch `claude-code-sentry-monitor`.** Sentry only as the place the work
   happened, never as an ad.
5. **YouTube titles and thumbnails are his, through the DevEx app.** This skill
   proposes an angle and the evidence for it. It does not pick a title or write
   into Linear.
6. **No time estimates. No bare IDs** (title plus link).

## Phase 1: platform plan (the judgment)

His platforms, in order of weight. Everything else (Instagram, TikTok, Threads,
Reddit, Bluesky) is skipped without discussion; he doesn't post there.

| Platform | Default treatment | Why (his data) |
| --- | --- | --- |
| **X** | native deep: one standalone post or native video, plus an Article when the source has real depth | Article 7,983 impressions vs a 720 median; native video median 1,327; text 592; bare links his bottom 5 (106 to 350). Public metrics, Oct 7 to Nov 13, 2026. |
| **YouTube** | angle only: one long-form angle and, if the source has a single visual payoff, one Short hook | His best edited video, "Grok Bot Workflows That Aren't Just Hype", has 7,752 views at 177 subscribers. Livestream copies on his channel get 5 to 104 views while Sentry's copies of the same streams get 4 to 8x that, so streams stay on Sentry's channel. Daily build vlogs (his Bolt hackathon "Day 3" to "Day 7": 45 to 345 views) lost to the one recap video (3,200). Shorts: 1 on the channel (709), not enough data, say so. |
| **LinkedIn** | native light: one text post, story or real number first | His best public posts there are personal announcements and stories (AI Engineer Paris speaker post, 65 reactions and 14 comments; Grok Bot workflows, 45); event promos sit around 20. |

State the plan in 3 to 5 lines before writing. Budget: 4 to 6 pieces. Exceed it only
with a stated reason.

Shape fit for his kind of sources:

| Source | X | YouTube | LinkedIn |
| --- | --- | --- | --- |
| A tool or repo he built | native demo video opening on the output, or a number-first post | "I built X, here's what it found" long-form | the story of why he built it |
| A system with rules (gates, checks, configs) | Article for the rules; short post for the single surprising number | "what broke when I let agents do Y" | the one lesson, argued with the number |
| A livestream or talk | the best 20 to 40 second clip, opening on the payoff; never the title plus link | not his channel (stays on Sentry's) unless re-cut as an edited video | the one thing he learned on stage, or a speaker announcement |
| An opinion | a question he wants answered | skip | skip unless he has evidence |

## Phase 2: extract

Mine the source once:

- **Core insight:** one sentence a dev would repeat to a teammate.
- **Real numbers**, each with its source and date.
- **The turn:** what he expected vs what happened.
- **A question** he genuinely doesn't know the answer to (his best short format:
  [slides question](https://x.com/sergical/status/2107846354995220792), 4,300, 6x median).
- **Visual payoff:** the one frame that shows it working (terminal output, a PR
  card, a trace).
- **Public-safe check:** mark every atom public, public-safe-as-ratio, or private.
  Drop the private ones.

Thin source, few atoms. Say so instead of padding.

## Phase 3: write natively

**X.** Line 1 under about 50 characters: a recognizable thing plus a number or a
pain. Write for replies, quotes and DM shares (weights 5, 5, 5 vs like 0.708 in
`xai-org/x-algorithm` `param.rs`, rechecked 2026-11-17; bookmarks aren't scored).
Threads only when the material truly sequences, 5 posts max, each one standalone;
essay material becomes an Article, not a thread. Links are fine in the post (X
says they no longer deboost), but the post must carry the value without the click.
Follow-ups land inside 48 hours, when For You drops the original.

**YouTube.** Output an angle, not a script: a hook for the first 5 seconds, a
working title direction for DevEx, and the search or competitor evidence that the
topic has demand and an open gap (pull with `yt-dlp "ytsearch20:..."`: views,
channel, upload date). Subscriber count is not a ceiling on views; say what the
gap is, not just that the topic is popular.

**LinkedIn.** The first two lines carry the whole hook: a specific claim or a real
number, no "Excited to share". One idea, argued with evidence. Slightly more
complete sentences than X, same person. End with one real question, then a
first-hour comment plan he posts himself (two comments that add a detail the post
left out).

**Voice:** casual, mostly lowercase on X, short lines, dev-honest, a little funny.
If his writing bot's voice guide exists, it wins. Same person, different room: if
the X and LinkedIn pieces read the same, one of them isn't native.

## Phase 4: quality gate (silent)

Score each piece 1 to 10 on native fit, hook, specificity, voice, slop lint
(`../content-atomizer/references/slop-patterns.md`). Ship at an 8 average with
nothing under 7. Hard fails at any score: an unsourced claim, a private detail, a
bare link, an ad for Sentry.

## Output

```
## {source title}: atomized {date}
Plan: {3 to 5 lines}

### X post
{text}
Media: {what to attach}
Why: {one line, a real number or link}

### X thread (n posts)
...

### LinkedIn
{text}
First-hour comments: {2}
Why: ...

### YouTube angle
Hook (0 to 5s): ...
Title direction for DevEx: ...
Evidence: {links with views, channel size, dates}

Sources: {every link used}
Skipped: {platform: reason}
```

Save to `$SERGICAL_DRAFTS/<source-slug>/` (default `/workspace/loki/drafts/`). Show
him the pieces in short chunks; nothing gets posted until he does it himself.

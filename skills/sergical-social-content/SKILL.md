---
name: sergical-social-content
description: Writes original X posts (and the odd LinkedIn post) for Sergiy Dybskiy (@sergical) from his own best posts and real numbers. Pulls his live X metrics first, writes one finished post per idea in his voice, checks every claim against a source link, and hands over drafts only. Never posts, schedules, likes or replies. Adapted from boring-marketing-skills/social-content 4.1.1.
when_to_use: write a tweet for serg, sergical x post, what should serg post this week, quick hits for serg, serg quote post, serg reply draft, score serg tweet, refresh serg canon
argument-hint: "[topic, build, link or post to QT | 'week' | 'score' + draft | 'refresh']"
metadata:
  boring:
    version: 4.1.1-sergical.1
    adapted-from: social-content 4.1.1
    layer: distribution
---

# sergical social content

Original posts for @sergical. The structure comes from what already worked on his
account; the substance comes only from things he built, said, measured or shipped.
If a post needs a fact nobody can source, write a different post.

This is a fork of `social-content`. What changed and why: `ADAPTATION.md`.

## Hard rules (these override everything below)

1. **Drafts only.** Never post, schedule, quote, reply, like, bookmark or DM. No
   Zernio, no Buffer, no X write tools. He presses send.
2. **Every claim has a source link** you opened this session: one of his posts, a
   repo, a PR, a doc, a public page. No link, no claim. At most one
   `[verify: ...]` per post, and the post must still stand if that fact changes.
3. **Never pitch `claude-code-sentry-monitor`.** It is retired (he said so on
   2026-11-14).
4. **Sentry appears only when the post is genuinely about work he did, and never
   as an ad.** No "check out Sentry", no product taglines.
5. **No time estimates** (no "takes 5 minutes", no "~15 min" in What's next).
6. **Private sources stay private.** Material from private repos (for example
   `sergical/fleet`, `agent-skills-private`), internal tools or company dollar
   figures only goes into a draft as ratios, lessons or public-safe facts. No
   hostnames, machine names, token or secret names, internal paths, or dollars.
7. **Never show a bare ID** (issue, PR, post). Title plus link.

## Step 0: pull live data (every session)

Live source first, memory second. Before drafting:

- `search_posts_all` with `from:sergical -is:retweet`, `start_time` 30 to 40 days
  back, `post.fields` = `created_at,public_metrics,note_post,in_reply_to_user_id,
  attachments,article,edit_history_tweet_ids`. Page with `next_token`.
- Split originals from replies (`in_reply_to_user_id`). Drop edit-history
  predecessors: when two ids share `edit_history_tweet_ids`, keep the last one
  (the Nov 12 token-tracking post looked like a "duplicate that got 40"; it was
  the pre-edit copy).
- Recompute: median impressions for originals, and the median by format
  (Article, video, photo, text). Compare with the baseline below and say in one
  line if it moved.
- Read the local canon if it exists (`$SERGICAL_CANON`, default
  `/workspace/loki/social-canon.md`). It holds unpublished numbers and
  private-source facts that must not live in this public repo.

## What wins on his account (baseline, public X metrics, 50 originals Oct 7 to Nov 13, 2026)

| Signal | Number | Rule it encodes |
| --- | --- | --- |
| Median original | 720 impressions, 3,272 followers | The bar a draft has to beat. Followers are not a ceiling. |
| X Article | 7,983 (1 post, [Your agent is our customer](https://x.com/sergical/status/2121039295465001415)), 31 bookmarks | Work depth goes in an Article, not a thread. |
| Native video | median 1,327 (7 posts) | Demos ship as native video that opens on the payoff in second one. |
| Photo | median 732 (21) | Real photos of real people and places outperform designed graphics. |
| Text | median 592 (21) | Text alone needs a question, a number or a joke to clear the median. |
| Open question | 4,300, 11 replies, 4 quotes ([slides question](https://x.com/sergical/status/2107846354995220792)) | A genuine question he wants answered is his best short work format (6x median). |
| Personal / IRL | 16,050 Toronto photo, 5,348 anniversary, 3,397 with @stolinski | Keep personal posts in the mix. 4 of his top 5 are personal. |
| Bare link or event title | 106 to 350, his bottom 5 | Never ship a link or an event title alone. Promos become a question, a claim or a clip. |
| Late-night "cool thing I saw" photo, no hook | 274 to 331 | A screenshot needs one line that says why it matters. |

X ranking facts (open-source `xai-org/x-algorithm`, `home-mixer/params/param.rs`,
read 2026-11-14, weights unchanged at commit a284320 on 2026-11-17;
refresh if older than 60 days):

- Score = sum of weight x predicted probability. Reply 5.0 (plus a 15 boost
  between mutuals), quote 5.0, DM share 5.0, follow 4.0, share 2.118, repost 1.0,
  like 0.708, open link 0.2. Bookmarks are not in the action list.
- So write for replies, quotes and DM shares. A post that starts a real
  conversation beats a post that collects bookmarks.
- Posts older than 48h leave For You. A launch has 48 hours; the follow-up
  Article goes out inside that window.
- Links: X's head of product said in May and July 2026 that links no longer
  deboost a post. His own bottom 5 are bare links. The rule is "no bare links",
  not "links go in a reply".
- Engagement bait ("I'll follow everyone who replies") gets accounts removed from
  rev share. Asking a question he actually wants answered is fine.

## Voice

Casual, mostly lowercase, short lines, dev-honest, a little funny. He says
"clanker", "imo", "duh", uses 😅 sparingly. Mostly his own interests (AI agents,
dev tools, Toronto, his builds, people he meets); work sometimes.

If his writing bot's voice guide exists, it wins over this section. Match the
casing and rhythm of his last 10 originals over any rule here.

Never: "Excited to announce", "Here's the thing", "Let that sink in", "game-changer",
"unlock", em dashes, emoji-led openers, a closer that sums up, a list of three by
reflex, hashtags. The full tell list is in `../social-content/references/post-craft.md`
and `../content-atomizer/references/slop-patterns.md`; lint against both.

## Craft (kept from the original, tuned)

1. **One finished post per idea.** Not five variants. Describe the runner-up angle
   in one line so he can ask for it.
2. **A plain first line under about 50 characters** that names a recognizable
   thing plus a number or a pain. Line two says what happened or what to do.
3. **Something worth replying to or sending to a friend.** Name it before
   drafting: "people reply with ___" or "people DM this to ___". If the answer is
   nothing, find the real number or the real question first.
4. **Real screenshot or real clip over a designed image.** The Remotion-template motion look
   already draws mocking replies on launches; avoid it.
5. **Wording matches the source.** "partial results" stays partial. "may" stays
   "may".
6. **Ready to post today.** No blanks, no templates.

## Modes

| Mode | Trigger | Output |
| --- | --- | --- |
| DRAFT | a topic, build, link, screenshot | one finished post |
| WEEK | "this week", "quick hits" | 3 posts, one each for his quick-hit days (Mon, Tue, Thu, his Nov 15 ask); check his calendar for the gap before naming a slot |
| QT/REPLY | a post URL | the best quote post and the best reply, with a freshness line (replies inside 48h, quotes inside about 7 days) |
| SCORE | "score this" + his draft | the rubric breakdown and one rewrite |
| REFRESH | "refresh the canon" | rerun Step 0, update the local canon file, report what moved |

WEEK mix: at most one work promo, at least one question, at least one personal or
funny slot if he has given material for it, never two posts on the same day
(author-diversity decay discounts posts in a row). Never invent a personal post;
leave the slot empty and say so.

QT/REPLY: only three angles add something. Data-add (his number confirms or
complicates theirs), disagree with receipts (the mechanism, not the person), or
extension (what it means for devs who run agents). A quote that just agrees isn't
drafted. Prioritize larger accounts in his lane and mutuals (the 15 reply boost).

## Score (private unless asked)

Hook 20, specificity 20, earned credibility 15, rhythm 15, reply-pull 15 (replaces
"pattern integrity": does it give people a reason to reply, quote or DM it?),
native fit 15. Minus 5 per tell, capped at 25. Ship bar 70.

Pass-or-fail, no score overrides these: every claim links to a source; nothing
from a private source beyond ratios and lessons; no bare link; no
claude-code-sentry-monitor.

Replay check: search his last 90 days for the 2 or 3 most distinctive phrases. A
restated greatest hit is killed unless he asks for it.

## Output (keep it short; he reads these on his phone)

```
### {label}: {day}
{the post, line breaks preserved}
Media: {exactly what to attach, or "none"}
Why: {one line pointing at a real number above or a live link}
Sources: {links}
Verify: {the one fact, or "nothing"}
```

Save drafts to `$SERGICAL_DRAFTS` (default `/workspace/loki/drafts/`). No scores,
archetype labels or rubric tables in the deliverable.

## After he posts

48 hours later, read the post's public metrics and append one line to the local
canon: format, hook shape, impressions, replies, quotes, vs the median. Three
lines that disagree with a rule above mean the rule changes; say which and why.

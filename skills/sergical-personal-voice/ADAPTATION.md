# What changed from brand-voice 4.1.1

`brand-voice` is built for a brand and its marketing team. This fork is for one
person who writes a personal blog and a company blog, and who already has a
hand-written voice guide. Upstream `brand-voice` is untouched, so merges stay clean.

## Kept

- The falsifiability rule and exhibit mechanics (read from upstream's
  `voice-extraction-judgment.md`, not copied).
- The six dimensions and the "describe what the writer does, not what it's about" bar.
- Drift check, as a re-run tool for drafts.
- The AI-tells list (read from upstream), now with a whitelist.

## Changed

- **Competitor-paste test -> peer-paste test.** A person has peers, not competitors.
- **Source weighting** ranks how much an editor touched the words, and skips
  co-authored and SEO-shaped company posts.
- **Era dating.** Every exhibit carries a year; old-only habits go to "Retired habits".
  A 2016 Medium post and a 2026 X Article are not the same voice.
- **AI-tell whitelist.** Run against this writer's real posts, the generic list
  flagged his own best moves ("logs capture the journey", literal "actually",
  self-asked questions). Anything proven in his exhibits is exempt.
- **Registers** replace the 8-platform table. He writes long-form, company blog and X.
- **Voice test samples** are a blog opener, a blog closer and an X post, not an
  email-to-list, social post and landing-page hero.
- **Diff mode** added: compare the extraction to an existing guide instead of
  replacing it.
- **`scripts/voice_stats.py`** adds the countable layer (rates, punctuation,
  sentence mix) so "no em dashes" is a count, not a vibe.

## Dropped

- `brand_context.py`, `./brand/` memory, positioning and audience inputs.
- Build mode's brand intake questions (there is a decade of published writing).
- Platform rows for LinkedIn, Instagram, TikTok, YouTube, Threads, Reddit, email.
- Landing-page hero, "What's next" routing to copy and ads skills, gold-case saving.

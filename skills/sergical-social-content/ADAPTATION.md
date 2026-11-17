# What changed from social-content 4.1.1, and why

| Original | sergical version | Why |
| --- | --- | --- |
| Generic SaaS / creator / local-business framing; SETUP scrapes 5 to 10 niche accounts with parallel subagents | Starts from his own live X metrics (Step 0) and a fixed baseline table | He has 50+ recent originals with public metrics. His own winners beat a niche scrape for structure, and it costs one search call. |
| X weights: like 0.5, copy-link share 20, "+75 author reply" history | Weights from `param.rs` read 2026-11-14: like 0.708, share 2.118, bookmarks not scored | The original's numbers were older than the repo he checked. Bookmarks matter for his decisions because his best posts collect them. |
| "External links cost 30 to 50% of reach, put them in a reply" | "No bare links"; links in the post are fine | X's head of product said in May and July 2026 that links no longer deboost. His own data says the problem is bare links (106 to 350), not links. |
| Archetype weights from a niche pattern library | His format medians: Article 7,983, video 1,327, photo 732, text 592; question 4,300; personal posts 4 of top 5 | These are the rules his account actually follows. |
| Queue with Zernio or Buffer after a yes | Drafts only, no scheduling at all | His standing rule: he presses send. |
| "When the posts have to sell a service": launch arc, DM routine, booked calls | Removed | He's not selling a service. |
| `./brand/` files, `brand_context.py`, `/performance-review` and other cross-skill links with "~15 min" estimates | A local canon file outside the repo, and a 48h metrics read-back | He has no `./brand/` folder; he doesn't want time estimates; private numbers must not live in a public fork. |
| Rubric dimension "pattern integrity" | "Reply-pull" | Replies, quotes and DM shares are what the ranker weights 5x; whether a post runs one clean archetype is less useful for him. |
| Seven craft rules, tell list, replay check, QT angle families | Kept, shortened | These are the genuinely good parts. |
| Weekly cadence 3 to 5 posts | 3 posts on his quick-hit days (Mon, Tue, Thu) | His Nov 15 ask. |
| (none) | Hard rules: never pitch claude-code-sentry-monitor, Sentry never as an ad, private-source handling, no bare IDs | His standing rules. |

---
name: sergical-personal-voice
description: Builds or re-checks a falsifiable voice profile for one writer (Sergiy Dybskiy, @sergical) from verbatim quotes in his own posts across eras and platforms, then diffs it against his existing voice guide. For a person who writes a personal blog and a company blog, not a brand or marketing team. Read-only on his sources; writes markdown files only; never publishes. Adapted from boring-marketing-skills/brand-voice 4.1.1.
when_to_use: build serg's writing voice profile from his posts, re-run the personal voice extraction, personal voice drift check on a draft, diff the voice profile against the voice guide, what did the voice guide miss
argument-hint: "['extract' | 'drift' + draft path or URL | 'diff' + guide path]"
metadata:
  boring:
    version: 4.1.1
    adapted-from: brand-voice 4.1.1
    layer: foundation
---

# sergical personal voice

A voice profile for one human who writes, built only from what he actually wrote.
Every line names a habit you could count or quote, and every line rules something
out. What changed from `brand-voice` and why: `ADAPTATION.md`.

**Load before writing any profile line:** `../brand-voice/references/voice-extraction-judgment.md`
(falsifiability rule, exhibit mechanics, the paste test). This skill reads it from
upstream instead of copying it, so upstream fixes arrive with each merge.

## Hard rules

1. **Verbatim or nothing.** Exhibits are copied from a page or API response you
   opened this session, 5 to 60 words, with the URL and the year. Never paraphrase
   inside quotes. Never invent a trait to fill a section; leave it out.
2. **Read-only.** Never post, comment, submit or edit anything on his sites or
   accounts. Output is markdown files on disk.
3. **Never edit his voice guide.** The diff goes in its own file. He (or his editor)
   decides what to fold in.
4. **No bare IDs.** Link posts by title or URL, never a naked status or issue number.

## Sources and weighting

Weight by how little anyone else touched the words:

| Rank | Source | Why |
|---|---|---|
| 1 | Long-form on his own platform (X Articles, Substack, personal blog) | No editor |
| 2 | His X originals and replies | Unedited, but a different register (see Registers) |
| 3 | Solo company-blog posts written in first person | Editor-reviewed, still him |
| 4 | Old personal blogs (Medium, archived personal site) | Him, but an earlier era |
| skip | Co-authored, SEO-shaped or interview-built company posts | Not his voice alone; label them, don't mine them |

Dead sites: query the Wayback Machine CDX API
(`https://web.archive.org/cdx/search/cdx?url=<domain>&matchType=domain&filter=statuscode:200&collapse=urlkey`)
and fetch the archived HTML. Medium: `https://medium.com/feed/@<handle>` returns
full text for recent posts. X: use the platform's read API, never scrape a
signed-in session.

**Date every exhibit.** A habit seen only before a cutoff (default: 5 years ago) goes
under "Retired habits", not into the live profile. A habit seen in every era is the
strongest kind of evidence.

Under about 1,500 words of rank 1 to 3 material, say the corpus is thin and stop.

## Method (Extract)

1. Pull the corpus to `corpus/` as plain text, one file per source, URL on line 1.
2. Run `scripts/voice_stats.py corpus/*.txt` for the countable layer: first-person
   rate per 1,000 words, sentence-length mix, and counts of `!`, `?`, `(`, em dashes,
   spaced slashes and ALL-CAPS words. Code blocks skew sentence stats on tutorials;
   say so instead of reporting them as voice.
3. Read everything once for the gestalt, then once per dimension (from `brand-voice`):
   tone, vocabulary, rhythm, structure, personality, POV.
4. Pull 15 to 30 exhibits as you go. Every pattern gets pinned to a quote.
5. Run the **peer-paste test** on each line: paste it into the profile of another
   developer who blogs about the same tools. If nobody would notice, sharpen or cut.
   "Writes clearly and credits others" fails. "Uses a spaced slash as 'or' in every
   era, 2016 to 2026" passes.
6. Find three habits he'd be surprised to see written down. If you can't, read again.

## Registers (replaces the 8-platform table)

Only the places he actually writes, each with exhibits:

- **Personal long-form:** the default for his own blog.
- **Company blog:** one notch tighter; the employer's style guide wins on spelling,
  headings and product mentions.
- **X:** one-liner register and thread/Article register. Say which X habits must
  not travel into long-form.

## AI-tell screen, with a whitelist

Load `../brand-voice/references/ai-tells.md` for the AVOID section and drift checks,
then **whitelist anything the writer already does in his exhibits.** The generic
list flags real human habits: "actually" used literally, "journey" inside a line he
wrote on purpose, a self-asked question answered in the next line. For each
whitelisted tell, cite the exhibit that proves it's his. Flag a tell only when it
clusters (3 or more in one piece) and none of them are whitelisted.

## Profile format

```markdown
# Voice profile: {name}
Built {YYYY-MM-DD} · {n} sources, ~{words} words · eras {first year}-{last year}

## Voice in three lines
## Habits (each with exhibit IDs, era span, and a count where countable)
## Registers (personal long-form / company blog / X)
## Structure: openings, closings, what he does mid-piece
## Habits to cut (real slips from the corpus, quoted)
## Retired habits (old-era only; do not imitate)
## AVOID (AI tells minus the whitelist, with why)
## Numbers (the voice_stats table)
## Evidence appendix (ID · quote · URL · year)
```

About 1,200 to 2,500 words. No example landing-page hero, no email-to-list sample.

## Diff mode (against an existing guide)

Read the guide in full first. Then write `comparison.md` with three lists:

- **Caught:** in the profile, absent from the guide. Each with a quote and URL.
- **Noise:** generic, marketing-shaped, dated, or wrong. Say which and why.
- **Guide-only:** what the guide has that the extraction didn't produce.

End with one recommendation: what to fold into the guide, and whether to re-run.

## Drift mode (on a draft)

Score the draft against the profile on the six dimensions. For each dimension below
8/10, quote the draft line next to the exhibit it drifts from. Two quotes side by
side or it isn't a finding. Same direction across several recent pieces means the
voice moved: suggest updating the profile, don't scold the draft.

## Voice test (replaces the email/social/landing samples)

Write three short samples from the profile alone: a personal-blog opening paragraph,
a closing paragraph, and one X post. If they could have been written without the
profile, the profile failed; fix it before showing anyone. Hand them over as
samples, clearly labeled, never as drafts to publish.

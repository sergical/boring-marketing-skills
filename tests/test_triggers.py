"""Trigger check: plain user requests should route to the right skill.

No model calls. route.py --request ranks skills by their `when_to_use` phrases; this
table asks whether each skill's phrases are distinctive enough that a typical request
lands on it first. A failure means two skills' trigger phrases overlap or a skill's
phrases miss how people actually ask. Fix the phrases, not the matcher.
"""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
sys.path.insert(0, str(ROOT / "_system" / "scripts"))
import route  # noqa: E402

REQUESTS = {
    "start-here": ["where do I start with marketing", "set up my business"],
    "brand-voice": ["this sounds generic, make it sound like me"],
    "sergical-personal-voice": ["re-run the personal voice extraction on serg's posts"],
    "positioning-angles": ["how should I position my product, what's the hook"],
    "audience-research": ["who is my audience and what do customers say"],
    "competitive-intel": ["who am I up against and what are competitors charging"],
    "google-business-profile": ["we're not in the map pack, fix my google profile"],
    "local-seo-plan": ["which towns should we target with a local seo plan"],
    "service-area-pages": ["write service area pages for each town we serve"],
    "ai-search": ["does ChatGPT recommend my business"],
    "site-audit": ["run a technical seo audit and crawl my site", "are AI crawlers blocked by my robots.txt",
                   "is google indexing my pages, check my sitemap"],
    "keyword-research": ["what should I write about on our blog"],
    "seo-content": ["write a blog post about water heater repair cost"],
    "programmatic-seo": ["generate pages from data, one for every integration"],
    "reviews": ["how do I get more google reviews"],
    "first-screen-check": ["check my site on a phone, why isn't my website getting calls"],
    "landing-page": ["build me a landing page for our drain cleaning offer"],
    "direct-response-copy": ["write a sales page that makes this convert"],
    "lead-magnet": ["grow my email list with a free checklist"],
    "paid-ads": ["write my ads and launch a campaign"],
    "google-ads-tracking": ["google ads not tracking calls"],
    "ads-incrementality-check": ["is performance max taking credit for my calls"],
    "meta-ads": ["is my facebook pixel working, set up the conversions api"],
    "speed-to-lead": ["we keep missing calls, set up a missed call text back"],
    "creative": ["generate an image for this campaign", "make ads for my coffee brand, ugc ads and static ads",
                 "write hooks for ads and ad concepts for my video ad"],
    "email-sequences": ["write a welcome email sequence"],
    "newsletter": ["draft this week's newsletter edition"],
    "performance-review": ["here's my GSC export, how did it perform"],
    "find-local-clients": ["find local clients for my agency"],
    "pitch-the-fix": ["write a cold email to this roofer about what's broken"],
    "social-content": ["write me a LinkedIn post"],
    "long-form-article": ["write a long article, a playbook with real numbers"],
    "content-atomizer": ["repurpose this blog post into social posts"],
}


class Triggers(unittest.TestCase):
    def test_every_catalog_skill_has_requests(self):
        on_disk = {p.parent.name for p in SKILLS.glob("*/SKILL.md")}
        self.assertEqual(sorted(on_disk - set(REQUESTS)), [], "add trigger requests for new skills")

    def test_no_trigger_phrase_is_shared_by_two_skills(self):
        owners = {}
        for skill_md in sorted(SKILLS.glob("*/SKILL.md")):
            frontmatter = route._frontmatter(skill_md.read_text(encoding="utf-8"))
            for phrase in route._frontmatter_value(frontmatter, "when_to_use").split(","):
                key = " ".join(route._words(phrase))
                if key:
                    owners.setdefault(key, set()).add(skill_md.parent.name)
        shared = {k: sorted(v) for k, v in owners.items() if len(v) > 1}
        self.assertEqual(shared, {}, "one phrase, one skill: keep it in the skill that should win")

    def test_requests_route_to_expected_skill(self):
        for skill, requests in REQUESTS.items():
            for request in requests:
                with self.subTest(skill=skill, request=request):
                    if not (SKILLS / skill / "SKILL.md").is_file():
                        self.skipTest(f"{skill} not written yet")
                    ranked = route.match_request(request, SKILLS)
                    top = ranked[0]["skill"] if ranked else None
                    self.assertEqual(top, skill, f"{request!r} -> {ranked}")


if __name__ == "__main__":
    unittest.main()

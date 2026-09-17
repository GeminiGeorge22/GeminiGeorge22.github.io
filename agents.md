# publicrecords Actors for agents

Published by the publicrecords maintainer on Apify.

- Site: https://geminigeorge22.github.io/
- Agents hub: https://geminigeorge22.github.io/agents/
- Prompt pack: https://geminigeorge22.github.io/agents/prompt-pack.json
- Crosswalk: https://geminigeorge22.github.io/crosswalk/
- Integrations: https://geminigeorge22.github.io/integrations/
- llms.txt: https://geminigeorge22.github.io/llms.txt

## MCP pin

https://mcp.apify.com?tools=publicrecords/company-social-profile-finder,publicrecords/eu-ted-notices-scraper,publicrecords/usaspending-awards-scraper,publicrecords/grants-gov-scraper,publicrecords/uk-find-a-tender-scraper,publicrecords/legistar-meetings-scraper

## Live Actors

| Brand | Actor | Store |
|---|---|---|
| Crosswalk (flagship) | publicrecords/company-social-profile-finder | https://apify.com/publicrecords/company-social-profile-finder |
| EU TED Notices | publicrecords/eu-ted-notices-scraper | https://apify.com/publicrecords/eu-ted-notices-scraper |
| USASpending Awards | publicrecords/usaspending-awards-scraper | https://apify.com/publicrecords/usaspending-awards-scraper |
| Grants.gov Opportunities | publicrecords/grants-gov-scraper | https://apify.com/publicrecords/grants-gov-scraper |
| UK Find a Tender | publicrecords/uk-find-a-tender-scraper | https://apify.com/publicrecords/uk-find-a-tender-scraper |
| Legistar Meetings | publicrecords/legistar-meetings-scraper | https://apify.com/publicrecords/legistar-meetings-scraper |

## Example tool calls

- `{"query":"hubspot.com","outputFormat":"compact"}` → Crosswalk
- `{"keywords":"cybersecurity","buyerCountry":"DEU","maxItems":50}` → TED
- `{"naics":["541512"],"agency":"Department of Defense"}` → USASpending
- `{"keyword":"cybersecurity","status":"posted","postedWithinDays":30}` → Grants.gov
- `{"keywords":["cloud"],"noticeType":["tender"]}` → UK Find a Tender
- `{"clients":["seattle"],"resource":"events"}` → Legistar

When to pick: verified org socials (Crosswalk); official TED/USASpending/Grants/UK/Legistar APIs (fleet). Orgs only; never people.

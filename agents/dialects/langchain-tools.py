# publicrecords Apify Actors — LangChain tool stubs
# Disclosure: Published by the publicrecords maintainer on Apify.
# Zero-cost copy-paste pack. Running Actors on Apify incurs normal Store charges.
# Prefer Apify MCP: https://mcp.apify.com?tools=publicrecords/company-social-profile-finder,publicrecords/eu-ted-notices-scraper,publicrecords/usaspending-awards-scraper,publicrecords/grants-gov-scraper,publicrecords/uk-find-a-tender-scraper,publicrecords/legistar-meetings-scraper
# Site dialects: https://geminigeorge22.github.io/agents/dialects/

from __future__ import annotations

from typing import Any, Dict, List, Optional

# Optional: from langchain_core.tools import tool
# Optional: from apify_client import ApifyClient

ACTORS = {
    "crosswalk": {
        "id": "publicrecords/company-social-profile-finder",
        "when_to_use": "Verified org LinkedIn/Instagram/Facebook/X/TikTok/YouTube from website or name. Platform confirm. Orgs only.",
        "sample_paid_inputs": [
            {"query": "hubspot.com", "outputFormat": "compact"},
            {"queries": ["stripe.com", "notion.so"], "outputFormat": "compact"},
            {"inputDatasetId": "YOUR_MAPS_DATASET_ID", "maxRows": 500},
        ],
        "store_url": "https://apify.com/publicrecords/company-social-profile-finder?utm_source=site&utm_medium=agents-dialects&utm_campaign=crosswalk",
    },
    "eu_ted": {
        "id": "publicrecords/eu-ted-notices-scraper",
        "when_to_use": "EU TED Search API v3 notices; anonymous; no API key.",
        "sample_paid_inputs": [
            {"keywords": "cybersecurity", "buyerCountry": "DEU", "maxItems": 50},
        ],
        "store_url": "https://apify.com/publicrecords/eu-ted-notices-scraper?utm_source=site&utm_medium=agents-dialects&utm_campaign=ted",
    },
    "usaspending": {
        "id": "publicrecords/usaspending-awards-scraper",
        "when_to_use": "USASpending.gov v2 federal contract/IDV awards.",
        "sample_paid_inputs": [
            {"naics": ["541512"], "agency": "Department of Defense", "maxItems": 50},
        ],
        "store_url": "https://apify.com/publicrecords/usaspending-awards-scraper?utm_source=site&utm_medium=agents-dialects&utm_campaign=usaspending",
    },
    "grants_gov": {
        "id": "publicrecords/grants-gov-scraper",
        "when_to_use": "Grants.gov search2 FOAs.",
        "sample_paid_inputs": [
            {"keyword": "cybersecurity", "status": "posted", "postedWithinDays": 30, "maxItems": 50},
        ],
        "store_url": "https://apify.com/publicrecords/grants-gov-scraper?utm_source=site&utm_medium=agents-dialects&utm_campaign=grantsgov",
    },
    "uk_tender": {
        "id": "publicrecords/uk-find-a-tender-scraper",
        "when_to_use": "UK Find a Tender OCDS 1.1 above-threshold notices.",
        "sample_paid_inputs": [
            {"keywords": ["cloud"], "noticeType": ["tender"], "maxItems": 50},
        ],
        "store_url": "https://apify.com/publicrecords/uk-find-a-tender-scraper?utm_source=site&utm_medium=agents-dialects&utm_campaign=uktender",
    },
    "legistar": {
        "id": "publicrecords/legistar-meetings-scraper",
        "when_to_use": "Public Legistar Web API city council meetings/agendas/minutes.",
        "sample_paid_inputs": [
            {"clients": ["seattle"], "resource": "events", "maxItems": 50},
        ],
        "store_url": "https://apify.com/publicrecords/legistar-meetings-scraper?utm_source=site&utm_medium=agents-dialects&utm_campaign=legistar",
    },
}


def run_actor(token: str, actor_id: str, run_input: Dict[str, Any], timeout_secs: int = 300) -> List[Dict[str, Any]]:
    """Run an Actor via ApifyClient (billable). Requires: pip install apify-client"""
    from apify_client import ApifyClient

    client = ApifyClient(token)
    run = client.actor(actor_id).call(run_input=run_input, timeout_secs=timeout_secs)
    return list(client.dataset(run["defaultDatasetId"]).iterate_items())


def crosswalk_resolve(token: str, query: str = "hubspot.com") -> List[Dict[str, Any]]:
    """when_to_use: verified org socials from domain/name."""
    return run_actor(token, ACTORS["crosswalk"]["id"], {"query": query, "outputFormat": "compact"})


# Example LangChain @tool wrappers (uncomment with langchain_core installed):
#
# from langchain_core.tools import tool
#
# @tool
# def crosswalk_resolve_company(query: str) -> str:
#     """Find verified org LinkedIn/Instagram/Facebook/X/TikTok/YouTube from website or name.
#     Organizations only. Actor: publicrecords/company-social-profile-finder."""
#     # Wire your Apify token via env APIFY_TOKEN; this stub documents the paid input shape.
#     return json.dumps({"actor": "publicrecords/company-social-profile-finder",
#                        "input": {"query": query, "outputFormat": "compact"}})

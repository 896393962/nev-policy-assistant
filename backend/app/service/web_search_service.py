import json
import os
from typing import Any, Dict, List

import requests
from dotenv import load_dotenv

load_dotenv()


class WebSearchService:
    """Service for performing web searches using the Bocha Web Search API."""

    def __init__(self, api_key: str = None):
        """
        Initialize the WebSearchService with API key.

        Args:
            api_key: Bocha API key. If not provided, read BOCHA_API_KEY from environment.
        """
        self.api_key = api_key or os.environ.get("BOCHA_API_KEY")
        self.url = "https://api.bochaai.com/v1/web-search"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}" if self.api_key else "",
            "Content-Type": "application/json",
        }

    def search(
        self,
        query: str,
        gl: str = "cn",
        hl: str = "zh-cn",
        autocorrect: bool = True,
        page: int = 1,
        search_type: str = "search",
        count: int = 10,
    ) -> Dict[str, Any]:
        """
        Perform a web search using Bocha API.

        The gl, hl, autocorrect and search_type parameters are kept for
        compatibility with older callers that used the Serper wrapper.
        """
        if not self.api_key:
            return {
                "error": True,
                "message": "BOCHA_API_KEY is not configured",
            }

        payload = {
            "query": query,
            "summary": True,
            "count": count,
            "page": page,
            "freshness": "noLimit",
        }

        try:
            response = requests.post(
                self.url,
                headers=self.headers,
                data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
                timeout=30,
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return {
                "error": True,
                "message": f"Search failed: {str(e)}",
            }

    def extract_search_results(self, search_results: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Extract formatted search results from the Bocha API response.

        Returns:
            List of simplified search result items.
        """
        results: List[Dict[str, Any]] = []
        web_pages = search_results.get("data", {}).get("webPages", {}).get("value", [])
        if not isinstance(web_pages, list):
            return results

        for position, item in enumerate(web_pages, start=1):
            results.append({
                "type": "web",
                "title": item.get("name", ""),
                "link": item.get("url", ""),
                "snippet": item.get("snippet", "") or item.get("summary", ""),
                "summary": item.get("summary", ""),
                "source": item.get("siteName", ""),
                "published_at": item.get("datePublished", ""),
                "position": position,
            })

        return results

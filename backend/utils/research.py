from duckduckgo_search import DDGS


def search_topic(topic: str):

    results = []

    with DDGS() as ddgs:
        data = ddgs.text(topic, max_results=5)

        for r in data:
            results.append({
                "title": r.get("title"),
                "snippet": r.get("body")
            })

    return results
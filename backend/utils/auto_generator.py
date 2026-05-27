import json
from backend.workflows.graph import app
from backend.utils.trend_collector import get_google_trends

def generate_all_content():

    trends = get_google_trends()

    results = []

    for topic in trends:

        result = app.invoke({
            "topic": topic
        })

        results.append({
            "topic": topic,
            "analysis": result.get("analysis"),
            "viral_ideas": result.get("viral_ideas"),
            "script": result.get("script"),
            "hooks": result.get("hooks")
        })

    with open("outputs/content_results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4)

    return results
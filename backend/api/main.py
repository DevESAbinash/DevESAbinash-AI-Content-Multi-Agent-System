from fastapi import FastAPI
from pydantic import BaseModel

from backend.workflows.graph import app
from backend.utils.trend_collector import get_google_trends
from backend.utils.auto_generator import generate_all_content

api = FastAPI()


class TopicRequest(BaseModel):
    topic: str


@api.get("/")
def home():
    return {
        "message": "AI Content Multi-Agent System Running"
    }


@api.get("/trends")
def trends():

    return {
        "trends": get_google_trends()
    }


@api.post("/generate")
def generate_content(data: TopicRequest):

    result = app.invoke({
        "topic": data.topic
    })

    return {
        "topic": data.topic,
        "analysis": result.get("analysis"),
        "viral_ideas": result.get("viral_ideas"),
        "script": result.get("script"),
        "hooks": result.get("hooks")
    }


@api.get("/generate-all")
def generate_all():

    results = generate_all_content()

    return {
        "status": "success",
        "total_generated": len(results),
        "results": results
    }
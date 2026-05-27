# AI Content Multi-Agent System

An automated pipeline that generates content ideas (analysis, viral angles, video scripts, and hook variations) from trending topics using a multi-step **LangGraph** workflow.

## Features

- Fetch trending topics (Google Trends via `pytrends`, with a safe fallback list)
- Research each topic using DuckDuckGo (`duckduckgo-search`)
- Generate:
  - Audience/creator/strategy analysis
  - Viral ideas (including controversial + storytelling angles)
  - Short video script (hook → story → CTA)
  - 10 viral hook options
- Expose results via a **FastAPI** HTTP service

## Tech Stack

- **FastAPI** + **Pydantic** (API)
- **LangGraph** (workflow orchestration)
- **LangChain OpenAI** (`ChatOpenAI`) (LLM calls)
- **OpenRouter** as the model gateway
- **DuckDuckGo search** for lightweight research
- **pytrends** for trending topic discovery

## Project Structure

- `backend/api/main.py` – FastAPI app + endpoints
- `backend/workflows/graph.py` – LangGraph state machine
- `backend/agents/*` – individual workflow steps (analysis, viral ideas, script, hooks)
- `backend/utils/*` – LLM wiring, research, trend collection, batch generation
- `backend/memory/trends.json` – included data placeholder (not required by the current code)
- `outputs/content_results.json` – generated batch output (created by `/generate-all`)

## Prerequisites

- Python 3.9+ recommended
- An **OpenRouter** API key

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Create a `.env` file in the project root:

```env
OPENROUTER_API_KEY=your_openrouter_api_key
```

> The LLM client is configured in `backend/utils/llm.py` and uses `base_url=https://openrouter.ai/api/v1`.

## Run the API

```bash
uvicorn backend.api.main:api --reload --port 8000
```

API base URL: `http://localhost:8000`

## API Endpoints

### `GET /`
Health message.

### `GET /trends`
Returns a list of trending topics.

### `POST /generate`
Generate content for a single topic.

Request body:

```json
{
  "topic": "AI automation"
}
```

Response:

```json
{
  "topic": "AI automation",
  "analysis": "...",
  "viral_ideas": "...",
  "script": "...",
  "hooks": "..."
}
```

### `GET /generate-all`
Fetches trends and runs generation for each topic.

Response:

```json
{
  "status": "success",
  "total_generated": 5,
  "results": [
    {
      "topic": "...",
      "analysis": "...",
      "viral_ideas": "...",
      "script": "...",
      "hooks": "..."
    }
  ]
}
```

Additionally writes results to:

- `outputs/content_results.json`

## How the Workflow Works

`backend/workflows/graph.py` compiles a LangGraph state machine with these steps:

1. `analyze_trend` –
   - runs DuckDuckGo research
   - asks the LLM to produce analysis
2. `find_viral_angle` – uses analysis + research to produce viral ideas
3. `generate_script` – writes a short video script using viral ideas
4. `generate_hooks` – creates 10 hook variations based on the script

All agents mutate the shared `AgentState`.

## Notes / Configuration

- If trend fetching fails, `backend/utils/trend_collector.py` returns a fallback list:
  - `AI automation`, `Personal branding`, `Faceless content`, `Business automation`, `Content systems`
- LLM model used by all agents: `openai/gpt-3.5-turbo` (via OpenRouter).

## Output
- you can run this by putting command: `uvicorn backend.api.main:api --reload --port 8000`

- Single topic: returned directly from `/generate`
- Batch generation: stored in `outputs/content_results.json`

## License

Add your license information here.

# AI-Content-Multi-Agent-System

# CLAUDE.md — ThinkTank AI

AI-powered startup idea validator using CrewAI multi-agent orchestration.

## Architecture

CrewAI agents: Market Analyst → Feasibility Checker → Persona Builder → Business Model Reviewer → Investment Readiness Assessor.

## Stack

- Backend: FastAPI, CrewAI
- Frontend: Next.js
- Database: PostgreSQL

## Running

```bash
# Backend
pip install -r requirements.txt
uvicorn main:app --reload

# Frontend
cd frontend && npm install && npm run dev
```

Requires API keys for LLM providers configured via environment variables.

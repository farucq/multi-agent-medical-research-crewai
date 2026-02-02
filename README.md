
# Multi-Agent Medical Research System using CrewAI

## Project Overview
This project implements a **multi-agent medical research assistant** using CrewAI.
The system autonomously researches recent ischemic stroke clinical trials (2024–2026),
analyzes clinical efficacy and safety, and generates a structured medical report in Markdown.

---

## Project Objectives
- Research recent ischemic stroke clinical trials (2024–2026)
- Analyze treatment efficacy and safety
- Generate a professional medical report
- Demonstrate a multi-agent AI workflow

---

## Agent Architecture
The system consists of three autonomous agents:

1. **Senior Medical Researcher**
   - Searches and gathers recent medical literature

2. **Clinical Analyst**
   - Evaluates clinical efficacy, safety, and relevance

3. **Medical Communicator**
   - Converts analysis into a structured Markdown report

---

## Technology Stack
- Python 3.10+
- CrewAI (multi-agent orchestration)
- DuckDuckGo Search (DDGS)
- Groq LLM (LLaMA 3.3 70B)
- Google Colab compatible

---

## How to Run
- Install dependencies:
- Run the project:

---

## Repository Structure
multi-agent-medical-research/
├── README.md
├── requirements.txt
├── output/
│ └── report.md
├── src/
│ ├── main.py
│ ├── agents.py
│ ├── tasks.py
│ └── tools.py
├── notebook/
  └── multi_agent_medical_research.ipynb

---

## Output
- **report.md** — Generated medical research report in Markdown format

<h1 align="center">🧠 SynapseSQL Agent</h1>

<p align="center">
  <em>Text-to-SQL that knows when to ask instead of guess.</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.10+-blue" />
  <img src="https://img.shields.io/badge/LangGraph-agent-purple" />
  <img src="https://img.shields.io/badge/FastAPI-backend-green" />
  <img src="https://img.shields.io/badge/status-in%20development-orange" />
</p>

---

**SynapseSQL** turns plain-English questions into safe, read-only SQL. Most
text-to-SQL systems guess when a question is vague. "Who is the top customer?"
could mean most revenue or most orders. SynapseSQL detects that, asks one short
follow-up, and only then writes the query.

## ✨ Features
- 🔌 Plug into any SQL database: schema and foreign keys are read automatically
- 🧭 Three ambiguity detectors compared head to head: prompt-based, rule-based,
  and execution-based consensus
- 🔁 Self-repair loop for failing queries
- 🛡️ Read-only execution with SQL validation, timeouts, and row limits
- 🧠 Conversation memory plus remembered clarifications
- 🏠 Runs on free or local models (Qwen via Ollama)

## 📊 Results
*Coming soon: accuracy, ask rate, and unnecessary-question rate for each detector.*

## 🏗️ Architecture
*Diagram coming soon.*

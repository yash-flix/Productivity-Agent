# AI Productivity Agent

An AI-powered productivity assistant built with **LangGraph**, **FastAPI**, **Streamlit**, and **LangChain** that orchestrates multiple productivity tools through structured tool calling.

## Features

* AI Agent powered by LangGraph
* Todo Management (SQLite + SQLAlchemy)
* Google Calendar Integration
* Meeting Notes Summarization
* Excel Analysis
* PowerPoint Generation
* Modular Tool Architecture
* FastAPI Backend
* Streamlit Frontend

---

## Tech Stack

### AI

* LangGraph
* LangChain
* Groq / OpenAI Compatible LLM
* Tool Calling

### Backend

* FastAPI
* SQLAlchemy
* SQLite

### Frontend

* Streamlit

### Productivity Tools

* Google Calendar API
* Excel Analysis
* PowerPoint Generation
* Meeting Summarization

---

## Project Structure

```text
app/
│
├── agents/
├── api/
├── core/
├── database/
├── graph/
├── prompts/
├── services/
├── tools/
├── utils/
└── server.py
```

---

## Workflow

```text
User
   │
   ▼
FastAPI
   │
   ▼
LangGraph
   │
   ▼
Assistant
   │
   ▼
Tool Selection
   │
   ▼
Tool Execution
   │
   ▼
Final Response
```

---

## Available Tools

### Todo

* Add Todo
* List Todos
* Complete Todo
* Delete Todo

### Google Calendar

* List Events
* Create Event
* Update Event
* Delete Event
* Find Free Slots

### Meetings

* Summarize Meeting Notes

### Excel

* Analyze Spreadsheet
* Missing Values
* Pivot Tables
* Charts
* Correlation Analysis

### Presentations

* Generate PowerPoint Presentations

---

## Installation

Clone the repository

```bash
git clone https://github.com/yash-flix/Productivity-Agent.git
```

Install dependencies

```bash
uv sync
```

Create a `.env` file

```env
GROQ_API_KEY=your_api_key
OPENAI_API_KEY=your_api_key
GOOGLE_CALENDAR_CREDENTIALS=...
```

Initialize the database

```bash
uv run python -m app.database.init_db
```

Run the backend

```bash
uv run uvicorn app.server:app --reload
```

Run Streamlit

```bash
cd streamlit-app

streamlit run app.py
```

---

## Example Prompts

### Todo

* Add a todo to finish my report
* List my todos
* Complete Finish my report

### Calendar

* What's on my calendar tomorrow?
* Find a free slot tomorrow afternoon
* Create a meeting with John tomorrow at 3 PM

### Meetings

* Summarize these meeting notes

### Excel

* Analyze sales.xlsx
* Show missing values
* Generate a pivot table

### Presentations

* Create a presentation about AI Agents

---

## Future Improvements

* Human Approval Layer for Write Operations
* Authentication
* Multi-user Support
* Persistent Memory
* LangSmith Tracing
* Docker Deployment
* Cloud Deployment
* Background Task Execution

---

## License

MIT License

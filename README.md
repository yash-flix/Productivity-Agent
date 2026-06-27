# AI Productivity Agent

An AI-powered productivity assistant built with **LangGraph**, **FastAPI**, **Streamlit**, and **LangChain** that orchestrates multiple productivity tools through structured tool calling.
<img width="1046" height="391" alt="image" src="https://github.com/user-attachments/assets/10604aca-d9ec-4dcf-8d51-f468e3ad0d4a" />
<img width="1046" height="391" alt="image" src="https://github.com/user-attachments/assets/99a48b7f-edc8-4186-9bd9-3903d3864f0c" />

<img width="1040" height="304" alt="WhatsApp Image 2026-06-26 at 7 29 14 AM" src="https://github.com/user-attachments/assets/b2ea76e3-4496-4d89-831a-baf042028a78" />
<img width="739" height="139" alt="WhatsApp Image 2026-06-26 at 7 37 30 AM" src="https://github.com/user-attachments/assets/712b2c5f-781e-48ab-aaaa-b1c4328e3f99" />
<img width="1363" height="672" alt="WhatsApp Image 2026-06-26 at 11 15 06 PM" src="https://github.com/user-attachments/assets/41371861-682e-497d-bf65-fa6ae41a97ef" />
<img width="1365" height="628" alt="WhatsApp Image 2026-06-26 at 8 37 38 AM" src="https://github.com/user-attachments/assets/20c84775-2e52-4d32-b3aa-f524afb06fb1" />
<img width="1365" height="628" alt="WhatsApp Image 2026-06-26 at 8 37 38 AM" src="https://github.com/user-attachments/assets/173994e3-0baa-4992-91ca-7e95ea32f160" />


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

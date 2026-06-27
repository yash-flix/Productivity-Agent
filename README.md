# AI Productivity Agent

An AI-powered productivity assistant built with **LangGraph**, **FastAPI**, **Streamlit**, and **LangChain** that orchestrates multiple productivity tools through structured tool calling.
<img width="1097" height="417" alt="image" src="https://github.com/user-attachments/assets/23e7bafc-bb3c-4f3a-90ef-e6d27054b26e" />
<img width="1040" height="214" alt="WhatsApp Image 2026-06-26 at 6 39 54 AM" src="https://github.com/user-attachments/assets/01b1f013-1af6-475e-80d4-c35957779cc0" />
<img width="942" height="257" alt="image" src="https://github.com/user-attachments/assets/0e945dab-4d8c-459d-85c6-18b417987a42" />
<img width="739" height="139" alt="WhatsApp Image 2026-06-26 at 7 37 30 AM" src="https://github.com/user-attachments/assets/60099290-c782-4f71-9187-7d6eca78ab08" />
<img width="1365" height="628" alt="WhatsApp Image 2026-06-26 at 8 37 38 AM" src="https://github.com/user-attachments/assets/aee795a3-61ee-4374-a04b-4329ee7a4049" />

<img width="1363" height="636" alt="WhatsApp Image 2026-06-26 at 11 23 44 PM" src="https://github.com/user-attachments/assets/78fae915-afee-4687-ba59-916ffdde3f5a" />



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

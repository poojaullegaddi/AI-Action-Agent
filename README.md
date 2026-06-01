
# 🤖 AI Action Agent

An AI-powered assistant that can not only answer questions but also take actions such as researching information from the web, generating summaries, maintaining conversation history, and saving reports to files when requested.

## 📌 Project Overview

Traditional chatbots primarily answer questions based on their training data. This project extends that capability by creating an **AI Action Agent** that can perform actions on behalf of the user.

The agent can:

* Answer general knowledge questions
* Research topics using web search
* Generate structured summaries and reports
* Maintain chat history during a session
* Save reports to files when explicitly requested

This project demonstrates the concept of **Agentic AI**, where an AI system can decide and execute actions based on user instructions.

---

## 🚀 Features

### 1. Conversational AI

* Handles general questions using a Large Language Model (LLM)
* Supports interactive chat sessions

### 2. Web Research

* Searches the web for current information
* Retrieves relevant search results
* Generates concise research summaries

### 3. Report Generation

* Creates structured reports from research findings
* Summarizes key insights

### 4. Report Saving

* Saves reports only when the user explicitly requests it
* Stores reports with timestamp-based filenames

### 5. Chat History

* Maintains conversation context within the Streamlit session
* Allows follow-up questions

### 6. Error Handling

* Handles search failures gracefully
* Prevents application crashes

---

# 🏗️ Architecture

## 🏗️ Architecture

```text
+------------------+
|      User        |
+------------------+
         |
         v
+------------------+
|   Streamlit UI   |
+------------------+
         |
         v
+------------------+
| Intent Detection |
+------------------+
         |
         +----------------------+
         |                      |
         v                      v

+------------------+    +------------------+
| General Question |    | Research Request |
+------------------+    +------------------+
         |                      |
         v                      v
+------------------+    +------------------+
|    Groq LLM      |    |  Search Tool     |
+------------------+    +------------------+
         |                      |
         |                      v
         |            +------------------+
         |            | Search Results   |
         |            +------------------+
         |                      |
         |                      v
         |            +------------------+
         |            |    Groq LLM      |
         |            +------------------+
         |                      |
         |                      v
         |            +------------------+
         |            | Summary Report   |
         |            +------------------+
         |                      |
         |          (Optional Save)
         |                      |
         |                      v
         |            +------------------+
         |            |  Save Report     |
         |            +------------------+
         |
         v
+------------------+
| Final Response   |
+------------------+
```

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### AI Model

* Groq LLM
* Llama 3.3 70B Versatile

### Search

* DDGS (DuckDuckGo Search)

### Utilities

* Python Dotenv

---

## 📂 Project Structure

ai-action-agent/

├── app.py

├── agent.py

├── tools.py

├── requirements.txt

├── .env

├── reports/

│ └── report_YYYYMMDD_HHMMSS.txt

└── README.md

---

## 🧪 Example Queries

### General Questions

```text
What is Generative AI?
```

```text
Explain Agentic AI.
```

### Research Queries

```text
Research the top 5 competitors of Tesla.
```

```text
Research the latest trends in Artificial Intelligence.
```

### Save Report

```text
Research the top 5 competitors of Tesla and save the report.
```

---

## 📋 Sample Workflow

### User Query

```text
Research the top 5 competitors of Tesla.
```

### Agent Actions

1. Detects research intent
2. Calls search tool
3. Retrieves search results
4. Generates summary
5. Returns structured report

### User Query

```text
Research the top 5 competitors of Tesla and save the report.
```

### Agent Actions

1. Searches the web
2. Generates report
3. Saves report to file
4. Returns confirmation message

---

## 🔍 How the Agent Decides What To Do

The application performs intent detection based on user input.

### General Queries

Examples:

```text
What is AI?
```

```text
Explain LangGraph.
```

The request is handled directly by the LLM.

### Research Queries

Examples:

```text
Research Tesla competitors.
```

```text
Latest AI news.
```

The search tool is invoked before generating a response.

### Save Requests

Examples:

```text
Save the report.
```

```text
Export findings.
```

The save tool is executed.

---

## 🧠 Concepts Demonstrated

* Agentic AI
* Tool Calling
* LLM Integration
* Retrieval-Augmented Workflows
* Prompt Engineering
* Session Management
* Error Handling
* Report Generation

---
# ![Live Demo](image/Screenshot 2026-06-01 234530.png)

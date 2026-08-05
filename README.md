# ✦ ResolveAI

### AI-Powered Customer Support Intelligence Platform

ResolveAI is an AI-powered customer support intelligence platform designed to help analyze customer requests, retrieve verified support knowledge, generate grounded AI responses, detect escalation needs, manage support tickets, and provide operational analytics through a unified workspace.

ResolveAI combines conversational AI with local verified knowledge retrieval and support intelligence to create safer, more explainable customer-support interactions.

---

## ✨ Key Features

### AI Support

- Conversational customer-support assistant
- OpenRouter-powered AI responses
- Conversation memory
- Context-aware responses
- Quick support actions
- Controlled AI error handling
- Premium Streamlit chat workspace

### Support Intelligence

ResolveAI automatically analyzes customer messages for:

- Intent
- Sentiment
- Priority
- Escalation requirement
- Escalation reason
- Retrieval confidence
- Knowledge verification status

This provides support intelligence alongside the AI conversation.

### Verified Knowledge Retrieval

ResolveAI evaluates local verified company policies before generating policy-based responses.

The retrieval system supports:

- Policy retrieval
- Retrieval confidence
- Strong, moderate, and weak match handling
- Verified-response eligibility
- Ambiguous retrieval detection
- Competing-policy detection
- Retrieval decision tracing
- Conflict handling
- Knowledge-grounded AI responses

When retrieval is ambiguous, ResolveAI can request clarification instead of presenting uncertain policy information as verified fact.

### Ticket Management

ResolveAI includes a local support-ticket system with:

- Automatic ticket ID generation
- Ticket creation
- Automatic escalation-based ticket creation
- Ticket status management
- Ticket search
- Priority tracking
- Intent tracking
- Sentiment information
- Escalation reasons
- AI-generated support summaries

Ticket information is persisted locally in JSON storage.

### Knowledge Workspace

The Knowledge workspace provides visibility into ResolveAI's verified support knowledge.

Capabilities include:

- Policy browsing
- Knowledge retrieval diagnostics
- Knowledge coverage analysis
- Retrieval performance
- Knowledge health
- Knowledge-gap detection
- Knowledge recommendations
- Policy utilization analysis

### Analytics

ResolveAI provides operational and executive support analytics including:

- Total tickets
- Open tickets
- Resolved tickets
- Critical tickets
- Resolution rate
- Ticket status distribution
- Priority distribution
- Customer intent distribution
- Escalation metrics
- Retrieval success
- Verified response rate
- Knowledge coverage
- Knowledge health
- Automation rate
- Retrieval reliability
- Operational efficiency
- Executive support index

Analytics can also be exported as:

- CSV
- JSON

### Settings & System Status

The Settings workspace displays:

- Application status
- AI service configuration status
- Knowledge system status
- AI provider
- Knowledge configuration
- Verification status
- Retrieval decision tracing status
- Conflict detection status
- Local data/privacy information

---

## 🧠 ResolveAI Workflow

```text
Customer Message
       │
       ▼
Support Intelligence
       │
       ├── Intent Detection
       ├── Sentiment Detection
       ├── Priority Detection
       └── Escalation Detection
       │
       ▼
Verified Knowledge Retrieval
       │
       ├── Policy Matching
       ├── Confidence Evaluation
       ├── Ambiguity Detection
       ├── Conflict Detection
       └── Decision Trace
       │
       ▼
AI Response Generation
       │
       ├── Verified Knowledge Context
       ├── Conversation Context
       └── OpenRouter
       │
       ▼
Customer Response
       │
       └── Ticket Creation when escalation is required
```

---

## 🏗️ Architecture

ResolveAI V1 uses a modular Python architecture.

```text
ResolveAI
│
├── User Interface
│   ├── AI Support
│   ├── Tickets
│   ├── Knowledge
│   ├── Analytics
│   └── Settings
│
├── AI Layer
│   ├── Chatbot orchestration
│   ├── Prompt management
│   └── OpenRouter client
│
├── Support Intelligence
│   ├── Intent detection
│   ├── Sentiment detection
│   ├── Priority detection
│   └── Escalation detection
│
├── Knowledge Layer
│   ├── Verified policies
│   ├── Retrieval
│   ├── Confidence evaluation
│   ├── Conflict detection
│   └── Retrieval observability
│
├── Ticket System
│   ├── Ticket creation
│   ├── Ticket persistence
│   └── Ticket management
│
└── Analytics
    ├── Support analytics
    ├── Knowledge analytics
    ├── Executive KPIs
    └── Analytics export
```

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application |
| Streamlit | User interface |
| OpenRouter | AI model access |
| Requests | AI API communication |
| python-dotenv | Environment configuration |
| JSON | Local knowledge and ticket persistence |
| Pytest | Automated testing |
| Ruff | Python code quality |

---

## 📁 Project Structure

```text
ResolveAI/
│
├── app.py
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
│
├── .streamlit/
│   └── config.toml
│
├── data/
│   ├── knowledge_base.json
│   └── tickets.json
│
├── src/
│   ├── analytics.py
│   ├── analytics_export.py
│   ├── chatbot.py
│   ├── escalation.py
│   ├── executive_kpi.py
│   ├── intent.py
│   ├── knowledge_analytics.py
│   ├── knowledge_base.py
│   ├── memory.py
│   ├── openrouter_client.py
│   ├── priority.py
│   ├── prompts.py
│   ├── retrieval_observability.py
│   ├── sentiment.py
│   ├── summary.py
│   ├── support_intelligence.py
│   ├── ticket.py
│   ├── ticket_manager.py
│   │
│   ├── components/
│   │   ├── analytics_dashboard.py
│   │   ├── knowledge_dashboard.py
│   │   ├── settings_dashboard.py
│   │   └── ticket_dashboard.py
│   │
│   └── ui/
│       ├── ai_support.py
│       ├── sidebar.py
│       └── theme.py
│
└── tests/
    ├── test_auto_ticket.py
    ├── test_chatbot_structure.py
    ├── test_error_handling.py
    ├── test_escalation.py
    ├── test_intent.py
    ├── test_priority.py
    ├── test_retrieval_conflicts.py
    ├── test_retrieval_observability.py
    ├── test_sentiment.py
    ├── test_summary.py
    ├── test_support_intelligence.py
    ├── test_ticket_manager.py
    └── test_verification.py
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd ResolveAI
```

### 2. Create a virtual environment

macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Configuration

ResolveAI uses OpenRouter for AI response generation.

Create a `.env` file in the project root:

```env
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

A safe template is included as:

```text
.env.example
```

Never commit your real `.env` file or API key to a public repository.

---

## ▶️ Running ResolveAI

Activate the virtual environment and run:

```bash
streamlit run app.py
```

Streamlit will provide the local application URL in the terminal.

---

## 🧪 Testing

Run the automated test suite with:

```bash
python -m pytest
```

ResolveAI includes tests covering core functionality such as:

- Intent detection
- Sentiment detection
- Priority detection
- Escalation
- Ticket management
- Automatic ticket creation
- Support intelligence
- Chatbot response structure
- Knowledge verification
- Retrieval conflicts
- Retrieval observability
- Error handling

---

## 🧹 Code Quality

ResolveAI uses Ruff for Python code-quality checks.

Run:

```bash
ruff check app.py src tests
```

Some intentionally broad application-level error boundaries may remain where ResolveAI needs to return a controlled support response rather than expose an internal failure to the user.

---

## 🔒 Security Notes

- API credentials are loaded from environment variables.
- Real API keys should never be committed to source control.
- Verified company knowledge is stored locally.
- Support tickets are stored locally in the V1 implementation.
- AI service failures are converted into controlled user-facing responses.

ResolveAI V1 is intended as a project/demo deployment and should receive additional authentication, authorization, database, secret-management, rate-limiting, and infrastructure hardening before production use with sensitive customer data.

---

## 📊 Data Storage

ResolveAI V1 uses local JSON persistence:

```text
data/knowledge_base.json
data/tickets.json
```

`knowledge_base.json` contains verified support knowledge.

`tickets.json` stores generated support tickets.

---

## 🚧 V1 Limitations

ResolveAI V1 intentionally keeps the architecture lightweight.

Current limitations include:

- Local JSON persistence
- No multi-user authentication
- No role-based access control
- No production database
- No multi-agent support workspace
- No document/vector-database RAG pipeline
- No external CRM/helpdesk integration
- No persistent multi-session conversation database
- Dark appearance is the primary V1 interface

These capabilities are candidates for future versions.

---

## 🚀 V2 Roadmap

Planned improvements may include:

- Light and dark appearance modes
- Authentication and role-based access
- PostgreSQL persistence
- Persistent conversation history
- Advanced agent workspace
- Document ingestion
- Embeddings and vector search
- Hybrid RAG retrieval
- Source citations
- Retrieval reranking
- Configurable AI models
- Token and AI cost analytics
- Advanced ticket automation
- SLA management
- Human handoff
- Notifications
- Advanced analytics
- Knowledge intelligence
- PDF and executive reporting
- External support integrations
- Docker and production deployment

---

## 📌 Project Status

**ResolveAI V1.0 — Release Candidate**

Core development, functional testing, and project cleanup are complete.

Current release workflow:

```text
TEST     ✅
CLEAN    ✅
DOCUMENT 🔄
RELEASE  ⏳
```

---

## 👨‍💻 Author

**Chandrabhan**

ResolveAI was developed as an AI-powered customer support intelligence project demonstrating conversational AI, verified knowledge retrieval, support automation, explainable retrieval decisions, ticket management, and operational analytics.

---

## 📄 License

No open-source license has been selected yet.

All rights reserved unless a license is added to this repository.
<div align="center">

# 🦜🔗 GenAI LangChain Journey

### *A complete, self-taught journey through LangChain — from basic LLM integration to autonomous multi-agent systems*

<br/>

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/🦜🔗_LangChain-1C3C3C?style=for-the-badge)](https://www.langchain.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Status](https://img.shields.io/badge/Status-Actively_Growing-brightgreen?style=for-the-badge)]()
[![Stars](https://img.shields.io/github/stars/yogeshsikhwal77/genai-langchain?style=for-the-badge&color=gold)](https://github.com/yogeshsikhwal77/genai-langchain/stargazers)

<br/>

</div>

> This repository is a hands-on, ground-up implementation of core Generative AI concepts using the LangChain framework. Instead of passive learning, every script and module here represents a concept implemented, tested, and understood from scratch — progressing logically from initializing basic LLMs to building complex, tool-calling multi-agent architectures.

<br/>

## 📑 Table of Contents

<table>
<tr>
<td valign="top">

- [🗂️ Repository Structure](#️-repository-structure)
- [📚 Topics Covered](#-topics-covered)
- [🚀 Highlights](#-highlights)
- [🛠️ Tech Stack](#️-tech-stack)

</td>
<td valign="top">

- [⚙️ Getting Started](#️-getting-started)
- [🧠 Learning Path](#-learning-path)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [🙋 About](#-about)

</td>
</tr>
</table>

<br/>

## 🗂️ Repository Structure

<details open>
<summary><strong>Click to expand / collapse the full folder tree</strong></summary>

```text
genai-langchain/
│
├── 01_Models/              → LLMs, ChatModels (OpenAI, Gemini, Anthropic, HuggingFace), and Embeddings
├── 02_Prompts/              → Prompt templates, few-shot prompting, and a chatbot implementation
├── 03_structured_output/    → TypedDict, Pydantic, and JSON schemas for LLM output
├── 04_output_parser/        → Parsing string, JSON, and structured outputs
├── 05_chain/                → Sequential, parallel, simple, and conditional chains
├── 06_runnables/            → LCEL sequence, parallel, passthrough, lambda, and branch runnables
├── 07_document_loader/      → Loaders for Text, PDF, Web, CSV, and Directories
├── 08_text_splitters/       → Length, structural, markdown, Python, and semantic splitters
├── 09_vector_store/         → ChromaDB integration for local vector storage
├── 10_retrievers/           → Wikipedia, vector store, MMR, multi-query, and contextual retrievers
├── 11_yt_bot/                → RAG-based YouTube chatbot project
├── 12_tools/                 → Built-in (DuckDuckGo, Shell) and custom tools/toolkits
├── 13_tool_calling/          → Teaching LLMs to autonomously trigger tools
├── 14_agents/                 → Single-agent and multi-agent systems (e.g. search + weather agent)
│
├── .venv/                   → Local virtual environment (not versioned)
├── .env                     → Environment variable configuration (API keys)
├── .gitignore                → Git ignore rules
├── requirements.txt           → Exact package dependencies
└── README.md
```

</details>

<br/>

## 📚 Topics Covered

| # | Folder | Topic | Description | Status |
|:-:|---|---|---|:-:|
| 01 | [`01_Models`](./01_Models) | Models & Embeddings | Initializing OpenAI, Gemini, Anthropic, and local/API HuggingFace models, plus document similarity and embedding generation. | ✅ |
| 02 | [`02_Prompts`](./02_Prompts) | Prompt Engineering | Prompt templates, chat history, message placeholders, and a Streamlit chatbot demo. | ✅ |
| 03 | [`03_structured_output`](./03_structured_output) | Structured Outputs | Enforcing strict LLM responses using Pydantic, TypedDict, and JSON. | ✅ |
| 04 | [`04_output_parser`](./04_output_parser) | Output Parsing | Extracting and casting raw LLM strings into actionable code objects (string, JSON, structured, Pydantic). | ✅ |
| 05 | [`05_chain`](./05_chain) | LangChain Chains | Linking components using simple, parallel, sequential, and conditional chaining logic. | ✅ |
| 06 | [`06_runnables`](./06_runnables) | LCEL Runnables | LangChain Expression Language (LCEL) routing using passthroughs, lambdas, and branches. | ✅ |
| 07 | [`07_document_loader`](./07_document_loader) | Data Ingestion | Loading custom data from `.txt`, `.csv`, `.pdf`, URLs, and bulk directory processing. | ✅ |
| 08 | [`08_text_splitters`](./08_text_splitters) | Chunking Strategies | Splitting text by length, document structure, markdown elements, Python code, and semantic meaning. | ✅ |
| 09 | [`09_vector_store`](./09_vector_store) | Vector Databases | Setting up and querying local ChromaDB instances for semantic search. | ✅ |
| 10 | [`10_retrievers`](./10_retrievers) | Retrieval Systems | Wikipedia retrieval, vector store retrieval, Maximum Marginal Relevance (MMR), multi-query, and contextual retrieval. | ✅ |
| 11 | [`11_yt_bot`](./11_yt_bot) | Project: YouTube RAG Bot | A practical RAG chatbot built over YouTube video transcripts. | ✅ |
| 12 | [`12_tools`](./12_tools) | Tools & Toolkits | Built-in tools (DuckDuckGo, Shell) and custom-engineered Python tools/toolkits. | ✅ |
| 13 | [`13_tool_calling`](./13_tool_calling) | Tool Calling | Teaching the LLM when and how to autonomously trigger external tools. | ✅ |
| 14 | [`14_agents`](./14_agents) | AI Agents | Single-agent loops and a multi-agent system for search + weather lookup. | ✅ |

<br/>

## 🚀 Highlights

<table>
<tr>
<td width="50%" valign="top">

**🧠 Multi-Model Integration**
Connected OpenAI, Anthropic Claude, Google Gemini, and HuggingFace models (both local and API).

**🗃️ Robust Data Pipelines**
Automated ingestion flows for PDFs, CSVs, and web data using tailored text splitters (semantic, markdown, length-based).

**🔍 Advanced RAG Architectures**
ChromaDB vector stores paired with Contextual, MMR, and Multi-query retrievers for accurate, grounded answers.

</td>
<td width="50%" valign="top">

**🛠️ Custom Tool Execution**
A custom toolkit enabling LLMs to autonomously execute Python and shell commands.

**🤖 Autonomous Agents**
Progressed from simple linear chains to a working multi-agent system (search + weather).

**📼 Real Project**
A YouTube-transcript RAG chatbot built entirely on concepts learned in this repo.

</td>
</tr>
</table>

<br/>

## 🛠️ Tech Stack

<div align="center">

![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-1C3C3C?style=flat-square)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=flat-square&logo=openai&logoColor=white)
![Anthropic](https://img.shields.io/badge/Anthropic_Claude-D97757?style=flat-square)
![Gemini](https://img.shields.io/badge/Google_Gemini-8E75B2?style=flat-square&logo=googlegemini&logoColor=white)
![HuggingFace](https://img.shields.io/badge/HuggingFace-FFD21E?style=flat-square&logo=huggingface&logoColor=black)
![ChromaDB](https://img.shields.io/badge/ChromaDB-FF6F61?style=flat-square)
![FAISS](https://img.shields.io/badge/FAISS-0467DF?style=flat-square)
![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=flat-square&logo=pydantic&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)

</div>

| Category | Tools & Libraries |
|---|---|
| **Framework** | LangChain, LangChain-Core, LangChain-Community, LangChain-Classic, LangGraph |
| **Language Models** | OpenAI, Google Gemini (`google-genai`), Anthropic Claude, HuggingFace |
| **Vector Database** | ChromaDB, FAISS |
| **Data Processing** | Pydantic, TypedDict, JSON |
| **Retrieval & Search** | Wikipedia, DuckDuckGo Search, PyPDF |
| **UI / App** | Streamlit |
| **Environment** | Python virtual environments, `python-dotenv` |

<br/>

## ⚙️ Getting Started

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yogeshsikhwal77/genai-langchain.git
cd genai-langchain
```

### 2️⃣ Create and activate a virtual environment
```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS/Linux
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set up environment variables
Create a `.env` file in the root directory and add your API keys:
```env
OPENAI_API_KEY="your_openai_api_key"
GEMINI_API_KEY="your_gemini_api_key"
ANTHROPIC_API_KEY="your_anthropic_api_key"
HUGGINGFACE_API_KEY="your_huggingface_api_key"
```

### 5️⃣ Explore the modules
Navigate to any numbered directory (e.g., `01_Models`) and run the Python scripts to see each concept in action.

<br/>

## 🧠 Learning Path

- [x] Basic LLM & ChatModel Integration
- [x] Prompt Templates & Chat History
- [x] Structured Outputs (Pydantic / TypedDict / JSON)
- [x] Output Parsers
- [x] LCEL Runnables & Chains
- [x] Document Loaders & Text Splitters
- [x] Vector Databases (ChromaDB)
- [x] Advanced Retrievers (MMR, Multi-query, Contextual)
- [x] Built-in & Custom Tools / Toolkits
- [x] Function / Tool Calling
- [x] Single & Multi-Agent Systems

<br/>

## 🤝 Contributing

This is primarily a personal learning repository, but suggestions, corrections, and discussion are always welcome!

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/your-idea`)
3. Commit your changes
4. Open a Pull Request

<br/>

## 📄 License

This project is licensed under the **MIT License** — you're free to use, modify, and distribute this code with attribution.

<br/>

## 🙋 About

This is a personal, self-driven learning project built to strengthen understanding of Generative AI, RAG (Retrieval-Augmented Generation), and agentic workflows through hands-on implementation.

**Author:** [@yogeshsikhwal77](https://github.com/yogeshsikhwal77)

<div align="center">

<br/>

### ⭐ If this helped your own LangChain learning journey, consider giving it a star!

[![GitHub stars](https://img.shields.io/github/stars/yogeshsikhwal77/genai-langchain?style=social)](https://github.com/yogeshsikhwal77/genai-langchain/stargazers)
[![GitHub followers](https://img.shields.io/github/followers/yogeshsikhwal77?style=social)](https://github.com/yogeshsikhwal77)

</div>
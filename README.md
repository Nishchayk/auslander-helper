# Ausländer Helper

A RAG-powered assistant that answers questions about German bureaucracy for international students in Berlin.

## The Problem

International students in Berlin struggle with German bureaucracy — Anmeldung, visa extensions, health insurance, tax registration, Bürgeramt appointments. Official information is scattered, often only in German, and written in complex legal language. Students waste hours Googling and asking WhatsApp groups for answers that should be simple to find.

## The Solution

A retrieval-augmented generation (RAG) system that:

- Ingests trusted English-language sources about German bureaucracy
- Uses a local large language model to answer student questions in plain English
- Cites which source each answer came from, so users can verify

## Tech Stack

- **Language Model:** Llama 3.2 (3B) via Ollama, running locally
- **Vector Database:** ChromaDB for semantic search over documents
- **Embeddings:** sentence-transformers
- **Backend:** FastAPI (Python)
- **Frontend:** HTML + vanilla JavaScript
- **Deployment:** Hugging Face Spaces

## Status

**Week 1 (April 2026):** In progress — building foundational setup and first LLM integration.

**Day 1-2 (April 18-19):** Python virtual environment created. FastAPI installed and hello-world endpoint running locally. GitHub repo initialized with .gitignore and README.

**Day 3 (April 22):** Ollama installed. Llama 3.2 (3B) model pulled and running locally. First Python-to-LLM call successful via `test_llm.py`. Experimented with and without system prompts to observe behavior differences.

**Key observation — hallucinations:** Model invented a fake government office acronym ("AEMV") in one response, and incorrectly stated the Anmeldung is done at the Ausländerbehörde in another. The correct location is the Bürgeramt. System prompts reduced verbosity but did not fix factual errors. This confirms the core premise of the project: generic LLMs cannot be trusted with specific bureaucratic facts without RAG grounding.

Building in public — roadmap and weekly progress updates below.

## Roadmap

- [x] Week 1: Python environment + FastAPI running
- [ ] Week 2: Document ingestion pipeline
- [ ] Week 3: Embeddings + ChromaDB setup
- [ ] Week 4: Retrieval system
- [ ] Week 5: Full RAG pipeline
- [ ] Week 6: Frontend
- [ ] Week 7: Deployment to Hugging Face Spaces
- [ ] Week 8: Polish + error handling
- [ ] Week 9: Blog post writeup
- [ ] Week 10: Launch + feedback

## Why I'm Building This

I'm an international student in Berlin doing an MS in AI. I'm building this both because the problem is real for me and my classmates, and because it's a learning project to develop production AI engineering skills with LLMs, vector databases, and deployment.

## About Me

Software engineer with 2 years of Python backend experience from India, currently pursuing MS in AI in Berlin. Graduating August 2027.

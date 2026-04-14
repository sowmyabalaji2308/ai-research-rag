[README.md](https://github.com/user-attachments/files/26693688/README.md)
# ai-research-rag# AI Research Papers RAG System

A production-grade Retrieval-Augmented Generation (RAG) system
that answers questions about AI research papers with cited, grounded responses.

## Results

| Metric | Score |
|--------|-------|
| Avg Faithfulness | 0.84 |
| Citation Coverage | 100% |
| Questions Passed | 9/10 |
| Avg Latency | 0.63s |

## Before vs After Hybrid Retrieval

| | Vector Only | Hybrid |
|--|--|--|
| Faithfulness | 0.71 | 0.84 |
| Questions Passed | 6/10 | 9/10 |

## Features
- Hybrid retrieval: BM25 + vector search
- 100% citation coverage on all answers
- Automated eval suite with faithfulness scoring
- Request logging with latency and token tracking
- Prompt versioning with config management
- FastAPI REST endpoint
- Streamlit UI with citation viewer

## Tech Stack
- LLM: Groq llama-3.1-8b-instant
- Embeddings: HuggingFace all-MiniLM-L6-v2
- Vector DB: ChromaDB
- API: FastAPI
- UI: Streamlit

## API Usage
POST /ask
{"query": "What is LoRA?"}

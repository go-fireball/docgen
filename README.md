# DocGen 📝✨

Generate Markdown summaries for every TypeScript (`.ts`) and JavaScript (`.js`) file in any repository using an LLM (Ollama).  
Great for quick codebase overviews, technical documentation, or onboarding material.

---

## Features

| Feature | Description |
|---------|-------------|
| 🔍 **Automatic repo scan** | Walks a directory tree and collects all `.ts` and `.js` files. |
| 🤖 **LLM-powered summaries** | Uses **Ollama** (or any compatible LLM wrapper) to create concise, human-readable explanations of each file. |
| 🗂️ **Markdown output** | Saves per-file docs with original folder structure inside an `output_docs/` directory. |
| 🏃 **CLI entry point** | Run with `python -m docgen` and pass `--input` / `--output` arguments. |
| ⏱️ **Timing info** | Prints how long each summary takes for quick performance insight. |

---

## Quick start

> Requires **Python 3.10+** and a running instance of **Ollama** with a model that understands code (e.g., `codellama`).

```bash
# 1. Install dependencies (Poetry)
poetry install

# 2. Activate virtualenv
poetry shell   # or `poetry run ...` for one-offs

# 3. Run DocGen
python -m docgen --input /path/to/repo --output output_docs
```

## 🔧 Ollama Setup (Required)

This tool relies on Ollama for running local LLMs.

You must install Ollama and download a model mistral. 

### Install Ollama

Follow instructions at https://ollama.com/download

## How it works

    scan_repo recursively finds .ts / .js files.

    For each file:

        Read the source code.

        Send it to prompt_ollama for summarization.

        write_markdown saves the summary as output_docs/<relative_path>.md.

    CLI prints elapsed time per file so you can spot bottlenecks.

The core logic lives in src/docgen/__main__.py, so importing the module elsewhere (e.g., for tests) is straightforward:
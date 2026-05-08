# HIT AI Unleashed workshop


This repo will contain all the necessary materials for the 1 day HiT AI Unleashed workshop

NOTE: Currently this project has only code. Might include PPTs and other reference later as well

The project is structued in such a way that each topic has its own folder
. Each folder has one or 2 notebooks max for the ease of understanding


# Setup Docs


## Install `uv` (fast Python package manager)

### macOS / Linux (curl)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Windows (powershell)

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Windows (winget)

```powershell
winget install astral-sh.uv
```

### macOS (Homebrew)

```bash
brew install uv
```



### Verify installation

```bash
uv --version
```

## Setup the project for running

```bash
# Clone the repo
git clone https://github.com/Astrasv/hit-ai-unleashed
cd ai_unleashed_hit

# Create a virtual environment and install dependencies
uv sync

# Activate the virtual environment
# macOS / Linux:
source .venv/bin/activate
# Windows (cmd):
.venv\Scripts\activate
# Windows (PowerShell):
.venv\Scripts\Activate.ps1

# Start Jupyter Lab
uv run jupyter lab
```

> **Tip:** You can run a notebook directly without activating the venv:  
> `uv run jupyter notebook path/to/notebook.ipynb`



# Project Folder Structure

## `simple_agents`
- Create simple agents
- Use different models

## `agents_with_tools`
- Create custom tool (`sqrt`)
- Access file tools
- Web search tool

## `mcps`
- Build local MCPs
- Connect with online MCPs

## `rags`
- Create simple in-memory RAGs
- Call RAG as a tool

## `memory`
- Manual memory
- Checkpointer

## `multimodel`
- Image handling
- Audio handling

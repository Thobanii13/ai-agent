# AI Agent Project

## Project Overview
A local-first AI agent that works offline using Ollama and upgrades responses online using Gemini Flash.

## Architecture
- **Local model**: deepseek-r1:1.5b / phi (via Ollama)
- **Cloud model**: Gemini Flash (when online)
- **Router**: Automatically switches between local and cloud
- **Memory**: Chat history saved locally and pushed to GitHub

## File Structure
- `agent.py` — main orchestrator
- `connectivity.py` — checks online/offline status
- `local_model.py` — talks to Ollama
- `cloud_model.py` — talks to Gemini API
- `router.py` — decides which model to use
- `memory.py` — saves chat history and pushes to GitHub
- `logger.py` — logs interactions
- `compiler.py` — compiles knowledge from logs
- `AI_AGENT_CLAUDE.md` — this file, project memory

## Git Rules
- Always commit with clean, descriptive messages
- Push to GitHub after every working change
- Never lose progress — commit often

## Models
- Offline: deepseek-r1:1.5b (reasoning), phi (general)
- Online: Gemini 1.5 Flash (free tier)

## Current Status
- [x] Git + GitHub connected
- [x] CLAUDE.md created
- [x] logger.py working
- [x] compiler.py working - knowledge extracted from session logs
- [x] agent.py (main orchestrator with routing, logging and cloud upgrade)

## Next Steps (Phase 4)
- [ ] Implement Shopify integration tools
- [ ] Implement YouTube content creation tools
- [ ] Add OpenRouter/qwen3.5 integration as secondary cloud option
- [ ] Enhance memory system with more sophisticated indexing
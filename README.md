# 🌌 The Cosmos

> A personal tracker for everything we're consuming, have consumed, and still want to experience together.

Built as a couples project. ✨

---

## What It Does

The Cosmos is our shared space for keeping track of movies, shows, games, manga, visual novels, and books — who's done what, what we can still experience together, and what we've been meaning to recommend to each other.

### Supported Media
- 🎬 Movies & TV Shows
- 🎮 Games & Visual Novels
- 📚 Books & Manga / Manhwa

---

## Features

### 👤 User System
Each user can rate, review, and favorite items, build a **Top 10 per medium**, and mark who has consumed what.

### 🔍 Search System
- Keyword search
- Filters by genre, rating, etc.
- *(Planned)* Semantic search on synopses

### ⚡ Cache System
- Fetched data is stored in a cache DB
- Cache refreshes every 2 days or on user prompt
- Search hits cache first → API → "No results found"

---

## Tech Stack

| Layer | Tech |
|---|---|
| Backend | FastAPI (Python) |
| Frontend | Vue + Tailwind CSS |
| Containerization | Docker + Docker Compose |
| Database | PostgreSQL |
| External APIs | TMDB · MAL · VNDB · Open Library |

---

## Project Structure

```
the-cosmos/
├── backend/            # FastAPI app
├── frontend/           # Vue + Tailwind
├── docker-compose.yml
└── .dockerignore
```

---

## Getting Started

### Prerequisites
- [Docker](https://www.docker.com/get-started) and Docker Compose installed

### Run the app

```bash
git clone https://github.com/bgrivero/the-cosmos.git
cd the-cosmos
docker compose up --build
```

The frontend and backend will be available at their respective ports once the containers are up.

---

*A project by two people with too many things left to experience.*
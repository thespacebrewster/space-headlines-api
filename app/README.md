# Space Headlines API 🚀

A REST API that aggregates space news headlines from multiple RSS feeds and returns normalized JSON data.

## Features

- ✅ Fetches headlines from NASA, Space.com, and Spaceflight Now
- ✅ Returns clean, normalized JSON
- ✅ Optional limit parameter to control number of results
- ✅ Auto-generated interactive documentation (Swagger UI)
- ✅ Health check endpoint

## Tech Stack

- **FastAPI** - Modern Python web framework
- **uvicorn** - ASGI server
- **feedparser** - RSS feed parsing
- **Python 3.11+**

## Installation

1. Clone the repository:
```bash
git clone https://github.com/thespacebrewster/space-headlines-api.git
cd space-headlines-api
```

2. Create and activate virtual environment:
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Mac/Linux
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Start the server:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`

## Endpoints

### GET /health
Health check endpoint
```bash
curl http://127.0.0.1:8000/health
```

### GET /headlines
Get space news headlines

**Parameters:**
- `limit` (optional, default: 20) - Number of headlines per source

**Example:**
```bash
curl http://127.0.0.1:8000/headlines?limit=5
```

## Interactive Documentation

Visit `http://127.0.0.1:8000/docs` for auto-generated Swagger UI documentation where you can test all endpoints interactively.

## Project Structure

```
space-headlines-api/
├── app/
│   ├── main.py      # FastAPI app and endpoints
│   └── feed.py      # RSS feed fetching logic
├── tests/           # Test files (coming soon)
├── .gitignore
├── requirements.txt
└── README.md
```

## Sources

- [NASA Breaking News](https://www.nasa.gov/rss/dyn/breaking_news.rss)
- [Space.com](https://www.space.com/feeds/all)
- [Spaceflight Now](https://spaceflightnow.com/feed/)

## Learning Journey

This is my first Python API project, built as part of my journey from zero coding experience to technical founder. Follow my progress at [@thespacebrewster](https://github.com/thespacebrewster).

## License

MIT License - feel free to use this for learning!

---

**Built with 🚀 by thespacebrewster**
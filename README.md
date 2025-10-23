# Surf Watch

A notification service for surfers that delivers daily surf reports via WhatsApp. Never miss epic surf conditions at your favorite spots!

## Overview

Surf Watch monitors wave conditions at your preferred surf spots and sends you personalized daily surf reports every morning. Users can subscribe through a web interface, select their top 3 surf spots, and manage notification preferences.

## Features

- Daily surf condition reports via WhatsApp
- Support for multiple surf spots per user
- User-friendly web subscription interface
- Configurable notification preferences
- Real-time surf data from Open-Meteo API

## Tech Stack

- **Backend**: FastAPI (Python 3.10+)
- **Database**: PostgreSQL
- **Dependency Management**: Poetry
- **Containerization**: Docker & Docker Compose
- **Surf Data**: Open-Meteo Marine & Weather APIs

## Quick Start

### Prerequisites

- Python 3.10 or higher
- Poetry (for dependency management)
- Docker & Docker Compose (for containerized deployment)

### Local Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/surf-watch.git
   cd surf-watch
   ```

2. **Install dependencies with Poetry**
   ```bash
   poetry install
   ```

3. **Activate the virtual environment**
   ```bash
   poetry shell
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your database credentials
   ```

5. **Run the application locally**
   ```bash
   poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
   ```

6. **Access the API**
   - API: http://localhost:8000
   - Interactive API docs: http://localhost:8000/docs
   - Alternative API docs: http://localhost:8000/redoc

### Docker Development Setup

1. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

2. **Build and run with Docker Compose**
   ```bash
   docker-compose up --build
   ```

3. **Access the services**
   - API: http://localhost:8000
   - PostgreSQL: localhost:5432

4. **Stop the services**
   ```bash
   docker-compose down
   ```

## Project Structure

```
surf-watch/
├── app/
│   ├── api/
│   │   ├── endpoints/      # API endpoint modules
│   │   └── routes.py       # Route registration
│   ├── services/           # Business logic layer
│   ├── main.py            # FastAPI application
│   ├── models.py          # SQLAlchemy ORM models
│   ├── schemas.py         # Pydantic schemas
│   ├── crud.py            # Database operations
│   └── database.py        # Database configuration
├── tests/                 # Test suite (coming soon)
├── pyproject.toml         # Poetry dependencies
├── poetry.lock            # Locked dependencies
├── Dockerfile             # Container definition
├── docker-compose.yml     # Multi-container setup
└── .env.example          # Environment variables template
```

## Development Commands

### Using Poetry

```bash
# Install dependencies
poetry install

# Add a new dependency
poetry add package-name

# Add a dev dependency
poetry add --group dev package-name

# Update dependencies
poetry update

# Run tests (coming soon)
poetry run pytest

# Format code
poetry run black app/

# Lint code
poetry run ruff app/
```

### Using Docker

```bash
# Build the image
docker-compose build

# Start services
docker-compose up

# Start in detached mode
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down

# Remove volumes (database data)
docker-compose down -v
```

## API Endpoints

### Core Endpoints

- `GET /` - Welcome message
- `GET /docs` - Interactive API documentation

### Surf Spots

- `POST /surfspots/` - Create a new surf spot
- `GET /surfspots/` - List all surf spots
- `GET /surfspots/{id}` - Get specific surf spot

### Users

- `POST /users/` - Create a new user
- `GET /users/{id}` - Get user details

### Surf Reports

- `POST /surfspots/{id}/reports/` - Create surf report for a spot
- `GET /surfspots/{id}/reports/` - Get reports for a spot

## Contributing

This project follows a structured PR-based development approach. Please see our development roadmap for upcoming features and improvements.

## License

MIT

## Contact

For questions or suggestions, please open an issue on GitHub.


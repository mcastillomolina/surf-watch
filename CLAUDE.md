# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Surf-watch is a FastAPI-based notification service for surfers. It tracks surf spots, generates surf reports, and notifies users when conditions are favorable at their preferred locations via WhatsApp.

## Development Commands

### Using Poetry (Preferred)

```bash
# Install dependencies
poetry install

# Activate virtual environment
poetry shell

# Run the application locally
poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

# Run tests (when implemented)
poetry run pytest

# Format code
poetry run black app/

# Lint code
poetry run ruff app/

# Type checking
poetry run mypy app/
```

### Using Docker

```bash
# Start all services (web + database)
docker-compose up --build

# View logs
docker-compose logs -f

# Stop services
docker-compose down

# Remove volumes (database data)
docker-compose down -v
```

The API will be available at `http://localhost:8000`. FastAPI automatically generates interactive API documentation at `/docs` and `/redoc`.

### Database Migrations

The project uses Alembic for database migrations. Current migration state:
- Initial migration `895a520ca3b5` adds coordinates (latitude/longitude) and location details (country/continent) to SurfSpot model

```bash
# Create a new migration
poetry run alembic revision --autogenerate -m "description"

# Apply migrations
poetry run alembic upgrade head

# Rollback migration
poetry run alembic downgrade -1
```

Environment variable required:
- `DATABASE_URL`: PostgreSQL connection string (format: `postgresql://username:password@host/dbname`)

## Architecture

### Core Data Models (app/models.py)

The application centers around a many-to-many relationship between users and surf spots:

- **User**: Contact information (name, email, phone_number) with notifications_enabled flag
- **SurfSpot**: Geographic surf locations with:
  - Required: name, latitude, longitude
  - Optional: location (city/region), country, continent
  - Future fields commented in code: region, spot_type, bottom_type
- **SurfReport**: Time-series surf condition data linked to surf spots (wave_height, water_temperature, wind_speed, swell_direction, report_time)
- **UserSurfSpot**: Junction table linking users to their preferred surf spots (composite primary key on user_id, surf_spot_id)

Key relationships:
- Users can follow multiple surf spots (many-to-many via UserSurfSpot)
- Surf spots have multiple reports over time (one-to-many)
- Users access reports through their followed surf spots

### Application Structure

**FastAPI Application (app/main.py)**
- Main entry point defines the FastAPI app and primary surf spot/report endpoints
- Router registration via `app.api.routes.get_router()` adds modular endpoints under `/users`, `/preferences`, and `/notifications`
- Database initialization happens at startup via `init_db()`

**Data Layer**
- `app/database.py`: SQLAlchemy engine, session management, and `get_db()` dependency
- `app/crud.py`: Database operations (get_user, create_surf_spot, link_user_surf_spot, etc.)
- `app/schemas.py`: Pydantic models for request validation and response serialization

**API Layer**
- `app/api/routes.py`: Registers endpoint routers with prefixes and tags
- `app/api/endpoints/users.py`: User creation and retrieval
- `app/api/endpoints/preferences.py`: Placeholder for user preference management
- `app/api/endpoints/notifications.py`: Placeholder for notification endpoints

**Service Layer**
- `app/services/surf_reports.py`: Business logic for surf report processing (currently empty)
- `app/services/notifications.py`: Notification delivery logic (currently empty)

### Planned Architecture (Not Yet Implemented)

The commented-out sections of docker-compose.yml outline a future system that includes:
- Celery workers for async tasks (fetching surf data, sending notifications)
- Celery beat for scheduled tasks
- Redis for Celery broker and caching
- Security utilities in app/core/

These components are not yet implemented.

## Important Implementation Notes

### Database Access Pattern

Always use the `get_db()` dependency for database sessions:

```python
@app.post("/endpoint")
def endpoint(db: Session = Depends(get_db)):
    # db session is automatically managed
    return crud.operation(db=db, ...)
```

### Adding New Endpoints

1. Create endpoint functions in `app/api/endpoints/`
2. Define an APIRouter in the endpoint file
3. Register the router in `app/api/routes.py:get_router()`

### Schema-Model Separation

- **models.py**: SQLAlchemy ORM models (database tables)
- **schemas.py**: Pydantic models (API contracts)

Always create both a Base schema (shared fields), Create schema (for requests), and full schema (for responses with `orm_mode = True`).

Note: SurfSpotBase includes field validators for latitude (-90 to 90) and longitude (-180 to 180) bounds.

## Code Quality Tools

The project is configured with:
- **Black**: Code formatter (line-length: 100, target: Python 3.10)
- **Ruff**: Fast linter with pycodestyle, pyflakes, isort, comprehensions, and bugbear rules
- **MyPy**: Type checking (with lenient settings for incremental adoption)
- **Pytest**: Test runner with coverage (configured but tests not yet implemented)

## Docker Configuration

The Dockerfile uses Python 3.10-slim and runs uvicorn on port 8000. The docker-compose.yml defines:
- `db` service: PostgreSQL 15 on port 5432
- `web` service: FastAPI application on port 8000, depends on db

The web service mounts the current directory to `/code` for live code reloading during development.

## Data Sources

The application uses Open-Meteo APIs for surf data:
- Marine API: Wave and ocean conditions
- Weather API: Wind and atmospheric conditions

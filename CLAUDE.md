# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Surf-watch is a FastAPI-based notification service for surfers. It tracks surf spots, generates surf reports, and notifies users when conditions are favorable at their preferred locations.

## Development Commands

### Running the Application

```bash
# Start all services (web + database) with Docker Compose
docker-compose up --build

# Run locally (requires DATABASE_URL environment variable)
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

The API will be available at `http://localhost:8000`. FastAPI automatically generates interactive API documentation at `/docs`.

### Database Setup

The application uses PostgreSQL with SQLAlchemy ORM. Database tables are auto-created on startup via `init_db()` in app/main.py:14.

Environment variable required:
- `DATABASE_URL`: PostgreSQL connection string (format: `postgresql://username:password@host/dbname`)

## Architecture

### Core Data Models (app/models.py)

The application centers around a many-to-many relationship between users and surf spots:

- **User**: Stores user contact information (name, email, phone_number)
- **SurfSpot**: Represents surf locations (name, location)
- **SurfReport**: Time-series surf condition data linked to surf spots (wave_height, water_temperature, wind_speed, swell_direction, report_time)
- **UserSurfSpot**: Junction table linking users to their preferred surf spots

Key relationships:
- Users can follow multiple surf spots
- Surf spots have multiple reports over time
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

The architecture.md file describes a more complete system that includes:
- Celery workers for async tasks (fetching surf data, sending notifications)
- Redis for Celery broker and caching
- Alembic for database migrations
- Security utilities in app/core/

These components are referenced in the commented-out sections of docker-compose.yml but not yet implemented.

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

## Docker Configuration

The Dockerfile uses Python 3.10-slim and runs uvicorn on port 8000. The docker-compose.yml defines:
- `db` service: PostgreSQL 15 on port 5432
- `web` service: FastAPI application on port 8000, depends on db

The web service mounts the current directory to `/code` for live code reloading during development.

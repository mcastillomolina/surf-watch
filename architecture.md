surf-app/
├── app/
│   ├── __init__.py
│   ├── main.py        # FastAPI application entry point
│   ├── models.py      # SQLAlchemy models for PostgreSQL
│   ├── schemas.py     # Pydantic schemas for request/response validation
│   ├── crud.py        # Database operations
|   ├── database.py    # O
│   ├── dependencies.py # Dependency overrides (e.g., for testing)
│   ├── config.py      # Configuration settings (e.g., DB, Redis URLs)
│   ├── api/
│   │   ├── __init__.py
│   │   ├── endpoints/
│   │   │   ├── __init__.py
│   │   │   ├── preferences.py  # User preference endpoints
│   │   │   ├── notifications.py  # Notification endpoints
│   │   └── routes.py  # Route registration
│   ├── core/
│   │   ├── __init__.py
│   │   ├── security.py  # Security utilities (e.g., OAuth2)
│   │   ├── logging.py   # Logging setup
│   └── services/
│       ├── __init__.py
│       ├── surf_reports.py  # Business logic for handling surf reports
│       ├── notifications.py  # Notification logic (e.g., sending emails)
├── celery_app/
│   ├── __init__.py
│   ├── tasks.py    # Celery tasks
│   ├── worker.py   # Celery worker setup
│   ├── beat.py     # Celery beat scheduler setup
├── alembic/        # Alembic migration scripts (for database schema migrations)
│   ├── versions/   # Database version control
│   ├── env.py
│   ├── script.py.mako
│   └── alembic.ini
├── tests/
│   ├── __init__.py
│   ├── test_main.py  # Test cases for your application
│   ├── test_api.py   # Test cases for API endpoints
│   ├── test_tasks.py # Test cases for Celery tasks
├── scripts/
│   ├── init_db.py   # Script for initializing the database
│   └── start.sh     # Entry point script for Docker container
├── .env             # Environment variables
├── requirements.txt # Python dependencies
├── Dockerfile       # Dockerfile for building the image
├── docker-compose.yml # Docker Compose file
├── README.md        # Project documentation
└── .gitignore       # Git ignore file



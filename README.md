# Investment Portfolio Tracker

A Flask-based web application for tracking and managing investment portfolios with PostgreSQL database support.

## Features

- Portfolio management and tracking
- Database-backed persistence using PostgreSQL
- Flask web framework with SQLAlchemy ORM
- Database migrations with Alembic
- Docker support for easy deployment

## Tech Stack

- **Backend Framework**: Flask 3.1.0
- **Database**: PostgreSQL (via Docker)
- **ORM**: SQLAlchemy 2.0.36
- **Migrations**: Alembic 1.14.0 & Flask-Migrate 4.0. 7
- **Data Processing**: Pandas 2.2. 3, NumPy 2.1. 3
- **Template Engine**: Jinja2 3.1.4

## Prerequisites

- Python 3.x
- Docker and Docker Compose
- pip (Python package installer)

## Installation

### 1. Clone the repository

```bash
git clone https://github. com/FTFaruque/Investment_Portfolio_Tracker. git
cd Investment_Portfolio_Tracker
```

### 2.  Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the PostgreSQL database

```bash
docker-compose up -d
```

This will start a PostgreSQL database with the following default credentials:
- **Host**: localhost
- **Port**: 5432
- **Database**: app_db
- **Username**: admin
- **Password**: password

### 4. Run the application

```bash
python run.py
```

The application will be accessible at `http://localhost:5000`

## Project Structure

```
Investment_Portfolio_Tracker/
├── investportfolioapp/        # Main application package
│   ├── __init__.py           # App initialization
│   ├── routes.py             # Application routes
│   ├── database/             # Database models and configurations
│   ├── static/               # Static files (CSS, JS, images)
│   └── templates/            # HTML templates
├── docker-compose.yaml       # Docker configuration for PostgreSQL
├── requirements.txt          # Python dependencies
├── run.py                    # Application entry point
└── . gitignore               # Git ignore rules
```

## Configuration

The application uses PostgreSQL as its database. The database connection details can be configured in the application's configuration file.  Default settings are:

```
postgresql://admin:password@localhost:5432/app_db
```

## Development

To run the application in debug mode:

```bash
python run.py
```

Debug mode is enabled by default in `run.py` for development purposes.

## Database Migrations

To create a new migration:

```bash
flask db migrate -m "Description of changes"
```

To apply migrations:

```bash
flask db upgrade
```

## Docker Support

The project includes a `docker-compose.yaml` file for running PostgreSQL:

```bash
# Start the database
docker-compose up -d

# Stop the database
docker-compose down

# View logs
docker-compose logs -f
```

## Dependencies

Key dependencies include:
- Flask (Web framework)
- SQLAlchemy (Database ORM)
- psycopg2 (PostgreSQL adapter)
- Pandas & NumPy (Data processing)
- Flask-Migrate (Database migrations)
- Alembic (Database version control)

For a complete list, see `requirements.txt`.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

**FTFaruque**

## Support

For issues, questions, or contributions, please open an issue in the GitHub repository. 

# BloX Django Project

This project is a Django web application containerized using Docker and 
managed with Docker Compose. It includes a PostgreSQL database service and 
is designed to be reproducible and easy to set up for development.

## Requirements

  - Docker
  - Docker Compose
  - Bash-compatible shell (for the scripts)

## Project Setup

  1. Clone the repostiory:
  ```bash
  git clone https://github.com/AAEmara/BloX.git
  cd BloX
  ```

  2. Create a `.env` file in the root directory with the following variables:
  ```env
  # PostgreSQL container setup
  POSTGRES_DB=blox_db
  POSTGRES_USER=blox_admin
  POSTGRES_PASSWORD=blox_password

  # Django settings
  DEBUG=True
  SECRET_KEY=your-dev-secret-key

  # PostgreSQL for Django
  DB_NAME=blox_db
  DB_USER=blox_admin
  DB_PASSWORD=blox_password
  DB_HOST=db
  DB_PORT=5432
  ```

  3. Build and run the application:
  ```bash
  sudo docker compose up --build
  ```

  4. Access the Django development server at:
  `http://localhost:8000`

## Script

  - **Bootstrap a new Django project:**
  ```bash
  ./scripts/bootstrap_django.sh
  ```

  - **Freeze dependencies to `requirements.txt`:**
  ```bash
  ./scripts/freeze_dependencies.sh
  ```

## Updating Dependencies

  1. After installing or upgrading any Python packages in the container:
  ```bash
  sudo docker compose exec web pip install <package-name>
  ```

  2. Then update `requirements.txt`:
  ```bash
  sudo docker compose exec web pip freeze > requirements.txt
  ```

## File Structure

  ```bash
  .
  ├── blox_app/               # Django project source code
  ├── Dockerfile              # Defines Python image and dependencies
  ├── docker-compose.yml      # Defines services (web, db)
  ├── .env                    # Environment variables (not committed)
  ├── requirements.txt        # Python dependencies
  ├── scripts/
  │   ├── bootstrap_django.sh
  │   ├── entrypoint.sh
  │   └── freeze_dependencies.sh
  ```

## Database

This project uses PostgreSQL. The database is defined as a service in 
`docker-compose.yml` and is automatically created using the credential in 
`.env`.

## Notes

  - Use the scripts directory to automate routine setup tasks.
  - Do not commit the `.env` file. It should be kept local and secret.
  - This setup is intended for local development. For production, additional
    configuration will be required (e.g., static files, security settings).

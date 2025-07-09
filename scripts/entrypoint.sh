#!/usr/bin/env bash

# Waiting for PostgreSQL to be ready
echo "Waiting for PostgreSQL..."
while ! nc -z $DB_HOST $DB_HOST; do
  sleep 1
done


# Running database migrations
echo "Running migrations..."
python manage.py migrate


# Starting Django development server
echo "Starting Django server..."
exec python manage.py runserver 0.0.0.0:8000

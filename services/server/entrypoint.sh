#!/bin/sh

echo "Waiting for postgres database to be ready..."

while ! nc -z postgres 5432; do
  sleep 0.1
done

echo "Postgres is up - executing command"

gunicorn -b 0.0.0.0:5000 manage:app
#!/bin/bash

alembic upgrade head

cd src

#cat database_creation.sql | psql -U postgres

gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000
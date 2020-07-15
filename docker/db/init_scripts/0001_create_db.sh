#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER admin LOGIN PASSWORD 'admin';
    CREATE DATABASE app;
    GRANT ALL PRIVILEGES ON DATABASE app TO admin;
EOSQL

#!/usr/bin/env bash
set -e

psql -v ON_ERROR_STOP=1 -v user=$DJANGO_POSTGRES_USER -v pwd="$DJANGO_POSTGRES_PASSWORD" --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER :user WITH ENCRYPTED PASSWORD :'pwd';
    CREATE DATABASE comments OWNER :user;
    GRANT ALL PRIVILEGES ON DATABASE comments TO :user;
EOSQL

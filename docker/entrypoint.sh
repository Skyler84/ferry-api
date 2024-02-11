#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

postgres_ready() {
python3 << END
import sys

import psycopg

try:
    psycopg.connect(
        dbname="${SQL_DATABASE}",
        user="${SQL_USER}",
        password="${SQL_PASSWORD}",
        host="${SQL_HOST}",
        port="${SQL_PORT}",
    )
except psycopg.OperationalError:
    sys.exit(-1)
sys.exit(0)

END
}
until postgres_ready; do
  >&2 echo 'Waiting for PostgreSQL to become available...'
  sleep 1
done
>&2 echo 'PostgreSQL is available'

exec "$@"
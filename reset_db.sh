#!/bin/bash
psql -d transcribe_db -f db/schema.sql
psql -d transcribe_db -f db/seed.sql
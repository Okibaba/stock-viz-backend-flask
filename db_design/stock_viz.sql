-- kill other connections
SELECT pg_terminate_backend(pg_stat_activity.pid)
FROM pg_stat_activity
WHERE pg_stat_activity.datname = 'stock_viz' AND pid <> pg_backend_pid();
-- (re)create the database
DROP DATABASE IF EXISTS stock_viz;
CREATE DATABASE stock_viz;
-- connect via psql
\c stock_viz

-- database configuration
SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET default_tablespace = '';
SET default_with_oids = false;

---
--- CREATE tables
---

CREATE TABLE stocks (
    id SERIAL,
    stock_id TEXT UNIQUE NOT NULL,
    symbol TEXT UNIQUE NOT NULL,
    company_name TEXT,
    company_description TEXT,
    PRIMARY KEY (id)
    );


CREATE TABLE prices (
    id SERIAL PRIMARY KEY,
    time_stamp TIMESTAMP,
    current_price NUMERIC,
    opening_price NUMERIC, 
    closing_price NUMERIC ,
    price_id INT
    );
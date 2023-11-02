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


CREATE TABLE users (
    id SERIAL,
    name TEXT NOT NULL,
    discontinued BOOLEAN NOT NULL,
    supplier_id INT,
    category_id INT,
    PRIMARY KEY (id)
);


CREATE TABLE stocks (
    id SERIAL,
    name TEXT UNIQUE NOT NULL,
    description TEXT,
    picture TEXT,
    PRIMARY KEY (id)
);


CREATE TABLE prices(
id SERIAL,
name TEXT NOT NULL,
PRIMARY KEY(id)
);


CREATE TABLE orders (
id SERIAL,
date DATE,
customer_id INT NOT NULL,
employee_id INT,
PRIMARY KEY (id)
);
CREATE DATABASE "stock-viz";


-- -- Database configuration
-- SET statement_timeout = 0;
-- SET lock_timeout = 0;
-- SET client_encoding = 'UTF8';
-- SET standard_conforming_strings = on;
-- SET check_function_bodies = false;
-- SET client_min_messages = warning;
-- SET default_tablespace = '';
-- SET default_with_oids = false;

-- -- CREATE tables

-- CREATE TABLE stocks (
--     id SERIAL,    
--     stock_symbol TEXT UNIQUE NOT NULL,
--     company_name TEXT UNIQUE NOT NULL,
--     company_description TEXT,
--     PRIMARY KEY (id)
-- );

-- CREATE TABLE prices (
--     id SERIAL PRIMARY KEY,
--     time_stamp TIMESTAMP NOT NULL,
--     current_price NUMERIC,
--     stock_id INT NOT NULL   
-- );

-- -- Add foreign key constraints
-- ALTER TABLE prices
-- ADD CONSTRAINT fk_prices_stocks
-- FOREIGN KEY (stock_id) 
-- REFERENCES stocks (id);

CREATE DATABASE "stock-viz";


-- -- CREATE tables

CREATE TABLE stocks (
    id SERIAL,    
    stock_symbol TEXT UNIQUE NOT NULL,
    company_name TEXT UNIQUE NOT NULL,
    company_description TEXT,
    PRIMARY KEY (id)
);

CREATE TABLE prices (
    id SERIAL PRIMARY KEY,
    time_stamp TIMESTAMP NOT NULL,
    current_price NUMERIC,
    stock_id INT NOT NULL   
);

-- -- Add foreign key constraints
ALTER TABLE prices
ADD CONSTRAINT fk_prices_stocks
FOREIGN KEY (stock_id) 
REFERENCES stocks (id);

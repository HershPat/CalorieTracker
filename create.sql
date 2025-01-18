CREATE TABLE client (
    client_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    client_age INT NOT NULL,
    client_weight INT NOT NULL,
    email VARCHAR(50) NULL,
    phone_number VARCHAR(50) NULL,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE food (
    food_id SERIAL PRIMARY KEY,
    client_id INT REFERENCES client( client_id),
    food_name VARCHAR(50) NOT NULL,
    calories INT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE foodLog (
    foodlog_id SERIAL PRIMARY KEY,
    client_id INT REFERENCES client(client_id),
    food_id INT REFERENCES food(food_id),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

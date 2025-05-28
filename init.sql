CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR UNIQUE NOT NULL,
    password VARCHAR NOT NULL,
    type VARCHAR NOT NULL
);

CREATE TABLE IF NOT EXISTS users_admin (
    id INTEGER PRIMARY KEY REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS users_buyer (
    id INTEGER PRIMARY KEY REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS products (
    id VARCHAR PRIMARY KEY,
    title VARCHAR NOT NULL,
    price FLOAT NOT NULL,
    currency VARCHAR NOT NULL,
    url VARCHAR
);

CREATE TABLE IF NOT EXISTS favorites (
    id SERIAL PRIMARY KEY,
    score INTEGER NOT NULL,
    comment VARCHAR,
    product_id VARCHAR NOT NULL REFERENCES products(id),
    user_id INTEGER REFERENCES users_buyer(id)
);

CREATE TABLE IF NOT EXISTS shopped (
    id SERIAL PRIMARY KEY,
    amount INTEGER NOT NULL,
    price FLOAT NOT NULL,
    product_id VARCHAR NOT NULL REFERENCES products(id),
    user_id INTEGER REFERENCES users_buyer(id)
);

INSERT INTO users (username, password, type) VALUES
('admin1', 'admin1pass', 'admin'),
('admin2', 'admin2pass', 'admin'),
('admin3', 'admin3pass', 'admin');

INSERT INTO users_admin (id)
SELECT id FROM users WHERE username IN ('admin1', 'admin2', 'admin3');

INSERT INTO users (username, password, type) VALUES
('buyer1', 'buyer1pass', 'buyer'),
('buyer2', 'buyer2pass', 'buyer'),
('buyer3', 'buyer3pass', 'buyer'),
('buyer4', 'buyer4pass', 'buyer'),
('buyer5', 'buyer5pass', 'buyer'),
('buyer6', 'buyer6pass', 'buyer'),
('buyer7', 'buyer7pass', 'buyer'),
('buyer8', 'buyer8pass', 'buyer');

INSERT INTO users_buyer (id)
SELECT id FROM users WHERE username IN (
  'buyer1', 'buyer2', 'buyer3', 'buyer4',
  'buyer5', 'buyer6', 'buyer7', 'buyer8'
);

INSERT INTO products (id, title, price, currency, url) VALUES
('MLA1', 'Celular Samsung Galaxy', 799.99, 'ARS', 'URL1'),
('MLA2', 'Notebook HP 15"', 1500.00, 'ARS', 'URL2'),
('MLA3', 'Auriculares Bluetooth', 199.99, 'ARS', 'URL3'),
('MLA4', 'Smart TV 50 pulgadas', 3500.00, 'ARS', 'URL4'),
('MLA5', 'Mouse inalámbrico', 89.50, 'ARS', 'URL5'),
('MLA6', 'Teclado mecánico RGB', 250.00, 'ARS', 'URL6'),
('MLA7', 'Parlante portátil JBL', 599.00, 'ARS', 'URL7'),
('MLA8', 'Monitor LG 24"', 1200.00, 'ARS', 'URL8'),
('MLA9', 'Tablet Lenovo 10"', 999.99, 'ARS', 'URL9'),
('MLA10', 'Cámara web HD', 300.00, 'ARS', 'URL10');

INSERT INTO favorites (score, comment, product_id, user_id) VALUES
(9, 'Muy buen producto', 'MLA1', (SELECT id FROM users WHERE username = 'buyer1')),
(7, 'Buen producto', 'MLA3', (SELECT id FROM users WHERE username = 'buyer1')),

(7, 'Cumple con lo esperado', 'MLA2', (SELECT id FROM users WHERE username = 'buyer2')),
(10, 'Excelente producto', 'MLA1', (SELECT id FROM users WHERE username = 'buyer2')),
(9, 'Muy buen producto', 'MLA3', (SELECT id FROM users WHERE username = 'buyer2')),

(10, 'Excelente calidad', 'MLA3', (SELECT id FROM users WHERE username = 'buyer3')),

(7, NULL, 'MLA4', (SELECT id FROM users WHERE username = 'buyer4')),
(10, 'Excelente producto', 'MLA1', (SELECT id FROM users WHERE username = 'buyer4')),
(8, NULL, 'MLA5', (SELECT id FROM users WHERE username = 'buyer4')),

(8, NULL, 'MLA5', (SELECT id FROM users WHERE username = 'buyer5')),
(10, NULL, 'MLA9', (SELECT id FROM users WHERE username = 'buyer5')),
(6, NULL, 'MLA10', (SELECT id FROM users WHERE username = 'buyer5'));

INSERT INTO shopped (amount, price, product_id, user_id) VALUES
(2, 799.99, 'MLA1', (SELECT id FROM users WHERE username = 'buyer1')),
(1, 1500.00, 'MLA2', (SELECT id FROM users WHERE username = 'buyer1')),
(1, 199.99, 'MLA3', (SELECT id FROM users WHERE username = 'buyer1')),
(1, 3500.00, 'MLA4', (SELECT id FROM users WHERE username = 'buyer1')),

(1, 1500.00, 'MLA2', (SELECT id FROM users WHERE username = 'buyer2')),
(1, 599.00, 'MLA7', (SELECT id FROM users WHERE username = 'buyer2')),

(3, 199.99, 'MLA3', (SELECT id FROM users WHERE username = 'buyer3')),
(2, 599.00, 'MLA7', (SELECT id FROM users WHERE username = 'buyer3')),

(2, 199.99, 'MLA3', (SELECT id FROM users WHERE username = 'buyer4')),
(1, 3500.00, 'MLA4', (SELECT id FROM users WHERE username = 'buyer4')),

(4, 89.50, 'MLA5', (SELECT id FROM users WHERE username = 'buyer6')),
(2, 1200.00, 'MLA8', (SELECT id FROM users WHERE username = 'buyer6')),
(1, 300.00, 'MLA10', (SELECT id FROM users WHERE username = 'buyer6')),

(1, 250.00, 'MLA6', (SELECT id FROM users WHERE username = 'buyer8'));
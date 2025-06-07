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
    id SERIAL PRIMARY KEY,
    id_ml VARCHAR UNIQUE NOT NULL,
    title VARCHAR NOT NULL,
    url VARCHAR
);

CREATE TABLE IF NOT EXISTS favorites (
    id SERIAL PRIMARY KEY,
    score INTEGER NOT NULL,
    comment VARCHAR,
    product_id INTEGER NOT NULL REFERENCES products(id),
    user_id INTEGER REFERENCES users_buyer(id)
);

CREATE TABLE IF NOT EXISTS shopped (
    id SERIAL PRIMARY KEY,
    amount INTEGER NOT NULL,
    price FLOAT NOT NULL,
    product_id INTEGER NOT NULL REFERENCES products(id),
    user_id INTEGER REFERENCES users_buyer(id)
);

INSERT INTO users (username, password, type) VALUES
('admin1', '$2b$12$wVEHwWx/UaXrOASx9cC7xOH1lBPXMq4Urqi2qxfG6qBoT7YzXdx2G', 'admin'),
('admin2', '$2b$12$FA4ANebjRH4xMKuuiUcnp.K/Q.KN8upEUY0lPLrwZ4cBkPyzopWxy', 'admin'),
('admin3', '$2b$12$Mt.QBFOLcnuaQA0jCFGpMuEX7n3OyiPlb9CWtFM9CEfRJMzwab3Z2', 'admin');

INSERT INTO users_admin (id)
SELECT id FROM users WHERE username IN ('admin1', 'admin2', 'admin3');

INSERT INTO users (username, password, type) VALUES
('buyer1', '$2b$12$ql35CKQ7k/t57KSm1jroC.NHNBo3iKZzYqf0swykTJne488fOG5Sa', 'buyer'),
('buyer2', '$2b$12$pHLp7fZjufdHyJDEIrmHl.5tzfoiRPw0rSSZuLjfjA2D2mYxBrod2', 'buyer'),
('buyer3', '$2b$12$NYBFJv3LVUkARSdeO4d38eQHAfU9IHYmIO8KzjEVEXtxuoOOPqVcu', 'buyer'),
('buyer4', '$2b$12$Zk92UjkoCTb5OpW7E9zS8uRzeZxc7Yhc.UUheBZMs8Ruchgi8IODW', 'buyer'),
('buyer5', '$2b$12$idTJ3gIltQ.yd8BRS6QRieXWIpHUoneXMPgk2Y7JzUIsnd0uNJaE2', 'buyer'),
('buyer6', '$2b$12$ZMkj/s8w5PYIPcZpPSrXBeYMX6GB1IzTkkMMiE7taeJKL5Bv21/Ym', 'buyer'),
('buyer7', '$2b$12$BLzgI46yG/znDB6Dc7fZlOaXmh.5pF2AOggux0a5yodAGM4P/EI52', 'buyer'),
('buyer8', '$2b$12$rJwXq8uoqMRd2omIh1Y4xuZ1I78N0EMgqCNSqNOA8hXycfR4bXZSS', 'buyer');

INSERT INTO users_buyer (id)
SELECT id FROM users WHERE username IN (
  'buyer1', 'buyer2', 'buyer3', 'buyer4',
  'buyer5', 'buyer6', 'buyer7', 'buyer8'
);

INSERT INTO products (id,id_ml, title, url) VALUES
(51,'MLA1', 'Celular Samsung Galaxy', 'URL1'),
(52,'MLA2', 'Notebook HP 15"', 'URL2'),
(53,'MLA3', 'Auriculares Bluetooth', 'URL3'),
(54,'MLA4', 'Smart TV 50 pulgadas', 'URL4'),
(55,'MLA5', 'Mouse inalámbrico', 'URL5'),
(56,'MLA6', 'Teclado mecánico RGB', 'URL6'),
(57,'MLA7', 'Parlante portátil JBL', 'URL7'),
(58,'MLA8', 'Monitor LG 24"', 'URL8'),
(59,'MLA9', 'Tablet Lenovo 10"', 'URL9'),
(60,'MLA10', 'Cámara web HD', 'URL10');

INSERT INTO favorites (score, comment, product_id, user_id) VALUES
(9, 'Muy buen producto', 51, (SELECT id FROM users WHERE username = 'buyer1')),
(7, 'Buen producto', 53, (SELECT id FROM users WHERE username = 'buyer1')),

(7, 'Cumple con lo esperado', 52, (SELECT id FROM users WHERE username = 'buyer2')),
(10, 'Excelente producto', 51, (SELECT id FROM users WHERE username = 'buyer2')),
(9, 'Muy buen producto', 53, (SELECT id FROM users WHERE username = 'buyer2')),

(10, 'Excelente calidad', 53, (SELECT id FROM users WHERE username = 'buyer3')),

(7, NULL, 54, (SELECT id FROM users WHERE username = 'buyer4')),
(10, 'Excelente producto', 51, (SELECT id FROM users WHERE username = 'buyer4')),
(8, NULL, 55, (SELECT id FROM users WHERE username = 'buyer4')),

(8, NULL, 55, (SELECT id FROM users WHERE username = 'buyer5')),
(10, NULL, 59, (SELECT id FROM users WHERE username = 'buyer5')),
(6, NULL, 60, (SELECT id FROM users WHERE username = 'buyer5'));

INSERT INTO shopped (amount, price, product_id, user_id) VALUES
(2, 799.99, 51, (SELECT id FROM users WHERE username = 'buyer1')),
(1, 1500.00, 52, (SELECT id FROM users WHERE username = 'buyer1')),
(1, 199.99, 53, (SELECT id FROM users WHERE username = 'buyer1')),
(1, 3500.00, 54, (SELECT id FROM users WHERE username = 'buyer1')),

(1, 1500.00, 52, (SELECT id FROM users WHERE username = 'buyer2')),
(1, 599.00, 57, (SELECT id FROM users WHERE username = 'buyer2')),

(3, 199.99, 53, (SELECT id FROM users WHERE username = 'buyer3')),
(2, 599.00, 57, (SELECT id FROM users WHERE username = 'buyer3')),

(2, 199.99, 53, (SELECT id FROM users WHERE username = 'buyer4')),
(1, 3500.00, 54, (SELECT id FROM users WHERE username = 'buyer4')),

(4, 89.50, 55, (SELECT id FROM users WHERE username = 'buyer6')),
(2, 1200.00, 58, (SELECT id FROM users WHERE username = 'buyer6')),
(1, 300.00, 60, (SELECT id FROM users WHERE username = 'buyer6')),

(1, 250.00, 56, (SELECT id FROM users WHERE username = 'buyer8'));
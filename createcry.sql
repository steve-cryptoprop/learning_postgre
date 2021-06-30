CREATE TABLE crypto (
    symbol VARCHAR(50) NOT NULL PRIMARY KEY
);

CREATE TABLE min (
    price NUMERIC(7,3),
    symbol VARCHAR(50) PRIMARY KEY REFERENCES crypto(symbol)
);
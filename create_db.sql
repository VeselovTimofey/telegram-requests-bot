CREATE TABLE category(
    name VARCHAR(100) PRIMARY KEY NOT NULL,
    photo_name VARCHAR(100),
    photo_date VARBINARY
);

CREATE TABLE product(
    name VARCHAR(100) PRIMARY KEY NOT NULL,
    category VARCHAR(100),
    photo_name VARCHAR(100),
    photo_date VARBINARY,
    FOREIGN KEY(category) REFERENCES category(name)
);

CREATE TABLE customer(
    id_telegram INTEGER PRIMARY KEY NOT NULL,
    name VARCHAR(100)
);

CREATE TABLE status(
    name VARCHAR(100) PRIMARY KEY NOT NULL
);

CREATE TABLE appeal(
    id INTEGER PRIMARY KEY NOT NULL,
    status VARCHAR(100),
    customer INTEGER,
    product VARCHAR(100),
    chat VARCHAR(500),
    FOREIGN KEY(status) REFERENCES status(name),
    FOREIGN KEY(customer) REFERENCES customer(id_telegram),
    FOREIGN KEY(product) REFERENCES product(name)
);

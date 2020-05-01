"""
Write pseudo-SQL statements to create database tables to store the products of a basic webshop. 
Each product has a name, a price, a creation date and may belong to several categories. 
Categories have a name and a flag to indicate whether the category is private or public.

Write a SQL query to find the list of products that belong to more than 5 public categories.
"""

tables = (
    """
    CREATE TABLE products (
        product SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        price INT NOT NULL,
        create_date DATE NOT NULL,
        FOREIGN KEY(categoryId)
            REFERENCES categories(id)
    )
    """,
    """
    CREATE TABLE categories (
        id INTEGER PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        flag BOOLEAN NOT NULL
    )
    """
)

SQL_QUERY = "SELECT * FROM products INNER_JOIN products ON products.category == categories.id  WHERE categories.flag = 1"
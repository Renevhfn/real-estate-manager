import sqlite3

# Create database connection (file wird im Container gespeichert)
conn = sqlite3.connect('real_estate.db')
cursor = conn.cursor()

# Create Properties Table
cursor.execute('''
CREATE TABLE IF NOT EXISTS properties (
    id INTEGER PRIMARY KEY,
    name TEXT,
    address TEXT,
    purchase_date TEXT,
    currency TEXT,
    purchase_price REAL,
    status TEXT
)
''')

# Create Income Table
cursor.execute('''
CREATE TABLE IF NOT EXISTS income (
    id INTEGER PRIMARY KEY,
    property_id INTEGER,
    date TEXT,
    amount REAL,
    currency TEXT,
    FOREIGN KEY(property_id) REFERENCES properties(id)
)
''')

# Create Expenses Table
cursor.execute('''
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY,
    property_id INTEGER,
    date TEXT,
    amount REAL,
    currency TEXT,
    description TEXT,
    FOREIGN KEY(property_id) REFERENCES properties(id)
)
''')

# Create Exchange Rates Table
cursor.execute('''
CREATE TABLE IF NOT EXISTS exchange_rates (
    id INTEGER PRIMARY KEY,
    date TEXT,
    usd_to_cop REAL
)
''')

# Commit and close
conn.commit()
conn.close()

print("Database created successfully!")


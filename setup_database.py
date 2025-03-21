import sqlite3

def create_database():
    # Create database connection (file will be stored in the container)
    conn = sqlite3.connect('database/real_estate.db')
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
    
    conn.commit()
    conn.close()


import sqlite3

conn = sqlite3.connect('real_estate.db')
cursor = conn.cursor()

# Example property data
properties = [
    ('Medellín House 1', 'Medellín, Colombia', '2010-05-01', 'COP', 300000000, 'Rented'),
    ('Medellín Apartment 2', 'Medellín, Colombia', '2015-08-20', 'COP', 400000000, 'Rented'),
    ('Bogotá House 1', 'Bogotá, Colombia', '2012-11-14', 'COP', 500000000, 'Rented'),
    ('Miami House 1', 'Miami, USA', '2018-03-10', 'USD', 350000, 'Rented'),
    ('New York Apartment 1', 'New York, USA', '2020-06-15', 'USD', 700000, 'Rented'),
    ('San Francisco House', 'San Francisco, USA', '2016-05-20', 'USD', 950000, 'Rented'),
    ('Los Angeles House', 'Los Angeles, USA', '2017-01-30', 'USD', 650000, 'Rented')
]

cursor.executemany('''
INSERT INTO properties (name, address, purchase_date, currency, purchase_price, status)
VALUES (?, ?, ?, ?, ?, ?)
''', properties)

# Commit and close
conn.commit()
conn.close()

print("Test data inserted!")


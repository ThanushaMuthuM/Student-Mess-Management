import sqlite3

# Connect to (or create) the database
conn = sqlite3.connect('mess.db')
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS menu (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    day TEXT NOT NULL,
    breakfast TEXT,
    lunch TEXT,
    dinner TEXT
)
''')

# Insert sample data
cursor.execute('''
INSERT INTO menu (day, breakfast, lunch, dinner)
VALUES (?, ?, ?, ?)
''', ('Monday', 'Idli & Sambar', 'Rice & Curry', 'Chapati & Paneer'))

conn.commit()
conn.close()

print("Database and table created successfully!")

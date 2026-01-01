import sqlite3

conn = sqlite3.connect("chatbot.DB")
cursor = conn.cursor()

# List columns in the checkpoints table
cursor.execute("PRAGMA table_info(checkpoints)")
columns = cursor.fetchall()
for col in columns:
    print(col)

conn.close()


cursor.execute("SELECT data, meta FROM checkpoints")
rows = cursor.fetchall()


"""
    Databse instance created for historical context persistance
    for chatbot
"""
import sqlite3
import os

#Definitions for tables and database name
db = "jax_history.db"

#Constant for DB path placement, consistently place DB in jax_project sub directory
DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), db)

#Connect to database instance if no db exists, connect to it
def get_connection() -> sqlite3.Connection:
    return sqlite3.connect(DB_PATH)

#Create tables inside db
def init_db():
    with get_connection() as connection:
        cursor = connection.cursor()
        
        cursor.execute("CREATE TABLE Users(id, name, created_at)")
        cursor.execute("CREATE TABLE Sessions(id, user_id, created_at, model_name)")
        cursor.execute("CREATE TABLE Messages(id, session_id, content, timestamp, token_count)")
        cursor.execute("CREATE TABLE Responses(id, message_id, content, timestamp, token_count, latency_ms)")

if __name__ == "__main__":
    init_db()                                   
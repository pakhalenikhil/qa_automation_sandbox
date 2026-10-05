import os
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

load_dotenv()

DB_URL = os.getenv("DATABASE_URL")

def get_db_connection():
    """Establishes and returns a connection to PostgreSQL."""
    try:
        conn = psycopg2.connect(DB_URL)
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        raise e

def create_tables():
    """Creates the agent_master table if it doesn't exist."""
    create_table_query = """
    CREATE TABLE IF NOT EXISTS agent_master (
        agent_id SERIAL PRIMARY KEY,
        full_name VARCHAR(100) NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL,
        pan_number VARCHAR(10) UNIQUE NOT NULL,
        agent_type VARCHAR(20) NOT NULL,
        status VARCHAR(20) DEFAULT 'PENDING',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(create_table_query)
    conn.commit()
    cursor.close()
    conn.close()

def insert_agent(full_name, email, pan_number, agent_type, status='PENDING'):
    """Inserts a new agent record and returns the generated agent_id."""
    query = """
    INSERT INTO agent_master (full_name, email, pan_number, agent_type, status)
    VALUES (%s, %s, %s, %s, %s)
    RETURNING agent_id;
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, (full_name, email, pan_number, agent_type, status))
    agent_id = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    conn.close()
    return agent_id

def get_agent_by_email(email):
    """Fetches agent details by email address as a dictionary."""
    query = "SELECT * FROM agent_master WHERE email = %s;"
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute(query, (email,))
    agent = cursor.fetchone()
    cursor.close()
    conn.close()
    return dict(agent) if agent else None

def delete_agent_by_email(email):
    """Deletes an agent record by email (used for test cleanup)."""
    query = "DELETE FROM agent_master WHERE email = %s;"
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, (email,))
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    create_tables()
    print("Database helper script updated and ready!")
import mysql.connector
from mysql.connector import Error
import hashlib
import os
from dotenv import load_dotenv

load_dotenv()

# Database configuration
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'database': os.getenv('DB_NAME', 'dino_game'),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', '')  # Set your MySQL password here
}

def get_db_connection():
    """Establish and return a database connection"""
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
    return None

def close_connection(connection, cursor=None):
    """Close database connection and cursor"""
    if cursor:
        cursor.close()
    if connection and connection.is_connected():
        connection.close()

def hash_password(password):
    """Hash a password for storing"""
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, password, email=None):
    """Register a new user in the database"""
    connection = get_db_connection()
    if not connection:
        return False, "Database connection failed"

    cursor = None
    try:
        cursor = connection.cursor()

        # Check if username already exists
        cursor.execute("SELECT username FROM users WHERE username = %s", (username,))
        if cursor.fetchone():
            return False, "Username already exists"

        # Hash the password
        hashed_password = hash_password(password)

        # Insert new user
        if email:
            cursor.execute(
                "INSERT INTO users (username, password, email) VALUES (%s, %s, %s)",
                (username, hashed_password, email)
            )
        else:
            cursor.execute(
                "INSERT INTO users (username, password) VALUES (%s, %s)",
                (username, hashed_password)
            )

        connection.commit()
        return True, "Registration successful"
    except Error as e:
        return False, f"Registration error: {e}"
    finally:
        close_connection(connection, cursor)

def login_user(username, password):
    """Authenticate a user and return user_id if successful"""
    connection = get_db_connection()
    if not connection:
        return False, "Database connection failed"

    cursor = None
    try:
        cursor = connection.cursor(dictionary=True)

        # Hash the password
        hashed_password = hash_password(password)

        # Check credentials
        cursor.execute(
            "SELECT user_id, username FROM users WHERE username = %s AND password = %s",
            (username, hashed_password)
        )
        user = cursor.fetchone()

        if user:
            return True, user
        else:
            return False, "Invalid username or password"
    except Error as e:
        return False, f"Login error: {e}"
    finally:
        close_connection(connection, cursor)

def save_score(user_id, score):
    """Save a user's score to the database"""
    connection = get_db_connection()
    if not connection:
        return False, "Database connection failed"

    cursor = None
    try:
        cursor = connection.cursor()

        # Insert score
        cursor.execute(
            "INSERT INTO scores (user_id, score) VALUES (%s, %s)",
            (user_id, score)
        )

        connection.commit()
        return True, "Score saved successfully"
    except Error as e:
        return False, f"Error saving score: {e}"
    finally:
        close_connection(connection, cursor)

def get_user_high_score(user_id):
    """Get the highest score for a user"""
    connection = get_db_connection()
    if not connection:
        return None

    cursor = None
    try:
        cursor = connection.cursor(dictionary=True)

        cursor.execute(
            "SELECT MAX(score) as high_score FROM scores WHERE user_id = %s",
            (user_id,)
        )
        result = cursor.fetchone()

        if result and result['high_score'] is not None:
            return result['high_score']
        else:
            return 0
    except Error as e:
        print(f"Error retrieving high score: {e}")
        return 0
    finally:
        close_connection(connection, cursor)

def get_top_scores(limit=10):
    """Get the top scores from all users"""
    connection = get_db_connection()
    if not connection:
        return []

    cursor = None
    try:
        cursor = connection.cursor(dictionary=True)

        cursor.execute(
            """
            SELECT u.username, s.score, s.date_achieved 
            FROM scores s 
            JOIN users u ON s.user_id = u.user_id 
            ORDER BY s.score DESC 
            LIMIT %s
            """,
            (limit,)
        )

        return cursor.fetchall()
    except Error as e:
        print(f"Error retrieving top scores: {e}")
        return []
    finally:
        close_connection(connection, cursor)


def initialize_database():
    return None
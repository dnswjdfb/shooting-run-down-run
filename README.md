# Dino Game with MySQL User Management

This project is a Pygame-based dinosaur game with MySQL integration for user registration, login, and score tracking.

## Features

- User registration and login system
- Score tracking and persistence
- High score leaderboard
- Dinosaur game with jumping, sliding, and magic abilities

## Setup Instructions

### 1. Install Required Packages

```bash
pip install pygame mysql-connector-python
```

### 2. Set Up MySQL Database

1. Install MySQL if you haven't already
2. Create a new database and tables using the provided SQL script:

```bash
mysql -u root -p < db_schema.sql
```

Alternatively, you can run the SQL commands directly in MySQL Workbench or another MySQL client.

### 3. Configure Database Connection

Open the `db_utils.py` file and update the database configuration:

```python
# Database configuration
DB_CONFIG = {
    'host': 'localhost',
    'database': 'dino_game',
    'user': 'root',
    'password': 'your_password_here'  # Set your MySQL password here
}
```

### 4. Run the Game

```bash
python dinogame.py
```

## How to Play

1. **Main Menu**:
   - Click "Start" to begin the game
   - Click "Settings" to access game settings
   - Click "Login" to log in or register

2. **Login/Registration**:
   - Enter your username and password to log in
   - If you don't have an account, click "Need an account? Register here"
   - Fill in the registration form and click "Register"

3. **Game Controls**:
   - Press Space or Up Arrow to jump
   - Press Down Arrow to slide
   - Press C to cast magic (when on the ground)

4. **Scoring**:
   - Your score increases as you play
   - When logged in, your scores are saved to the database
   - Your highest score is displayed during gameplay

## Database Schema

The game uses two main tables:

1. **users**: Stores user account information
   - user_id: Unique identifier for each user
   - username: User's login name
   - password: Hashed password for security
   - email: Optional email address
   - created_at: Account creation timestamp

2. **scores**: Stores game scores
   - score_id: Unique identifier for each score entry
   - user_id: Foreign key linking to the users table
   - score: The player's score
   - date_achieved: When the score was achieved

## Troubleshooting

If you encounter database connection issues:

1. Verify that MySQL is running
2. Check that the database credentials in `db_utils.py` are correct
3. Ensure the 'dino_game' database exists
4. Make sure the required tables have been created

For other issues, please check the console output for error messages.

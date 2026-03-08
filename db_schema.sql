-- MySQL Database Schema for Dino Game

-- Create database
CREATE DATABASE IF NOT EXISTS dino_game;
USE dino_game;

-- Create users table
CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create scores table
CREATE TABLE IF NOT EXISTS scores (
    score_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    score INT NOT NULL,
    date_achieved TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Indexes for better performance
CREATE INDEX idx_username ON users(username);
CREATE INDEX idx_user_score ON scores(user_id, score);

-- Sample queries for user registration
-- INSERT INTO users (username, password, email) VALUES ('player1', 'hashed_password', 'player1@example.com');

-- Sample queries for login
-- SELECT user_id, username FROM users WHERE username = 'player1' AND password = 'hashed_password';

-- Sample queries for storing scores
-- INSERT INTO scores (user_id, score) VALUES (1, 100);

-- Sample queries for retrieving top scores
-- SELECT u.username, s.score, s.date_achieved FROM scores s JOIN users u ON s.user_id = u.user_id ORDER BY s.score DESC LIMIT 10;

-- Sample queries for retrieving user's highest score
-- SELECT MAX(score) as highest_score FROM scores WHERE user_id = 1;

-- Sample queries for updating user information
-- UPDATE users SET email = 'new_email@example.com' WHERE user_id = 1;
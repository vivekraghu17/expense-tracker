# Expense Tracker 😁

Expense Tracker is a simple Python application for tracking expenses. It allows users to register, log their expenses, and view their expense history.

## Features

- User registration: Users can register with a username and password.
- Expense logging: Users can log their expenses with details such as date, amount, category, and description.
- Expense viewing: Users can view their expense history.

## Installation

1. Clone the repository:

https://github.com/vivekraghu17/expense-tracker.git

2. Navigate to the project directory:

cd expense-tracker

3. Run the main.py file

   python3 main.py

Follow the on-screen instructions to register, log expenses, and view expense history.

## Dependencies

- Python 3.x
- SQLite3


Here's a basic architecture for the Expense Tracker project:

Main Script (main.py):

This is the main Python script that contains the expense tracker application.
It handles user interaction, such as registration, logging expenses, and viewing expense history.
The script interacts with the SQLite database to store and retrieve user information and expense records.
SQLite Database (expense_tracker.db):

The SQLite database stores user information and expense records.
It consists of two main tables:
users: Stores user details such as user ID, username, and hashed password.
expenses: Stores expense records including user ID, date, amount, category, and description.

I have created this project to get understanding of python and how it can be used to handle database clients 😉

Good luck ✌️

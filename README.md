# 2001
🎲 Dice Game - Flask Application

📌 Project Description

This project is a web application built with Flask that simulates a dice game between a player and the computer. The player can choose names, roll the dice, and compete against the computer based on a predefined winning score.

🔧 Installation

Install Python (version 3.8 or later)

Create a virtual environment (recommended):

python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate    # Windows

Install required packages:

pip install flask

🚀 Running the Application

Start the Flask server:

python app.py

Open a browser and go to:

http://127.0.0.1:5000/

🎮 Game Mechanics

The player enters their name and the opponent's name.

Each player starts with 0 points.

In their turn, a player rolls 2 dice (standard D6 dice).

The number of obtained pips is added to the total score.

Starting from the second turn:
    if a player rolls a 7, they divide their number of points by 7, disregarding the fractional part,
    if the player rolls an 11, they multiply the current number of points by 11.

The player who first reaches 2001 points wins.


📜 Project Structure

/project_folder
│── app.py                # Main Flask application
│── roll_cubes_finction.py # Helper functions for dice rolls
│── /templates             # HTML templates
│   │── index.html         # Main page
│   │── welcom_start.html  # Welcome screen
│   │── game.html          # Game screen
│   │── win.html           # Winner screen
│── /static               # CSS and static files
│   │── style.css          # Application styling
│── README.md              # This file

📌 Important Global Variables

you_score – player's score

computer_score – computer's score

roll_count – number of rolls

win_score – score required to win

messages_list – list of messages for the player

💡 Possible Enhancements

✔ Add roll statistics 📊
✔ Allow choosing the number of dice 🎲
✔ Implement visual dice roll animations ✨

Author: [Toufar Libor] 🚀


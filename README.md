# Monty Hall Problem Simulation and Interactive Game

This Python project implements a simulation and interactive version of the classic **Monty Hall problem**.  
Users can either run a large-scale simulation to observe probabilities or play the game interactively via the console.

---

## Features

- **Statistical simulation**: Runs thousands of trials to show winning probabilities when switching or staying with the initial choice.  
- **Interactive game**: Play Monty Hall in the console, choose doors, decide whether to switch, and see your results.  
- Tracks and displays win/loss statistics during interactive play.

---

## How to Use
After downloading the project files, run the main Python script to start the program. The program will prompt you to choose one of two modes:

1. Statistical simulation mode
   The program runs 100,000 simulations of the Monty Hall game twice — once assuming the player always switches their choice, and once assuming the player always stays with the original door. It then displays the winning percentages for both strategies, illustrating the well-known advantage of switching.

2. Interactive game mode
   You play the Monty Hall game in the console. First, you select one of three doors. The host then opens one of the other doors revealing a loss. You have the option to stick with your original door or switch to the remaining unopened door. After you make your choice, the program reveals if you won or lost. The program keeps track of how many times you win or lose and shows your overall winning percentage after each round. You can continue playing as many rounds as you want.

---

## Project Details
   - The game uses simple randomization to assign the prize behind one of the three doors.
   - The host always opens a door that is neither the player’s choice nor the prize door.
   - The simulation function runs many iterations automatically to generate statistical results.
   - The interactive game supports user input and error checking to ensure valid door choices and decisions.

## Requirements
   - Python 3.x (no additional libraries required).
   - The project is lightweight and runs in any standard Python environment.

---

## How to Run

1. Clone this repository:

   ```bash
   git clone https://github.com/Cay00/monty-hall-simulation.git
   cd monty-hall-simulation

2. Run the program:

   ```bash
   python MontyHallProblem/monty_hall.py

3. Follow the on-screen prompts to either:

   Run a large-scale simulation showing win probabilities, or
   Play the Monty Hall interactive game in the console.

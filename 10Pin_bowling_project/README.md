# Bowling Game Project

This repository contains the code for a 10-pin Bowling Game scoring system. The implementation is a backend without a GUI, designed as a prototype for an educational software system.

## Project Files

- `bowling_game.py`: Contains the `BowlingGame` class that implements the scoring logic
- `in_depth_usage.py`: Demonstrates the tests in more detail and how to use the `BowlingGame` class
- `test_bowling.py`: all the unit tests for the `BowlingGame` class
- `test project.pdf`: this has all the documentation for this project

## Game Rules

Each game of bowling consists of ten frames. In each frame, the bowler will have two chances to knock down as many pins as possible with their bowling ball.

### Scoring

- **Open Frame**: When a player fails to knock down all ten pins in a frame, they score the number of pins knocked down.
- **Spare**: When a player knocks down all ten pins using both balls of a frame, it is a spare. The player scores 10 plus the pins knocked down by the next roll.
- **Strike**: When a player knocks down all ten pins on the first roll, it is a strike. The player scores 10 plus the pins knocked down in the next two rolls.
- **10th Frame**: If the player rolls a strike or spare in the 10th frame, they get bonus rolls. The player can roll up to three balls in the 10th frame.

### Maximum Score

A perfect game (12 strikes in a row) scores 300 points.

## Task

this code is the finished version of what was given and has been tested debugged, refactored and fixed
It also has all of the documentation for this project

# 2D Crossy Road (Python + Pygame)

Originally Developed: Spring 2022
Refactored: Spring 2026

Team: Huan Zhang & Sam Cox

![Crossy Road Gameplay](media/example_gameplay.jpg)

A simple Crossy Road–style arcade game built with **Python** and **Pygame**, organized using an **MVC (Model-View-Controller)** architecture. The game includes lane hazards (cars), river hazards (logs + drowning), a start menu with color selection, score tracking, level progression, and a game-over restart flow.

---

## Features

- **MVC architecture**
  - `main.py` wires together `Game` (model), `View`, and `Controller`, then runs the game loop.
- **Start menu**
  - Play button, player color picker (green/red/blue), and movement instructions text.
- **Gameplay hazards**
  - Randomized obstacle zones per band: cars or logs/rivers, with moving entities and collision handling.
- **Scoring**
  - Score increases when moving up and decreases when moving down; shown both in-game and on game over.
- **Leveling**
  - Reach the top to advance to the next level, reinitializing game state with increased obstacle velocity via level-based speed logic in `Car` and `Log`.
- **Game-over + restart**
  - Dying (car collision or drowning) opens a game-over menu with “Play Again”.

---

## Requirements
- Python 3.x
- Pygame

## Run Instructions
```
cd src
python3 main.py
```

## Controls
- **Mouse**
  - Click Play to start.
  - Click one of the player-color options on the start menu.
- **Keyboard**
  - Arrow keys move the player in 4 directions.

# Snake
**Overview**

This is a simple implementation of the classic Snake game in Python. The game includes a snake, apples, and bombs. The player controls the snake's direction with arrow keys, and the goal is to eat apples while avoiding collisions with the snake itself and bombs.


https://github.com/libbyyosef/Snake/assets/36642026/31592de1-b16a-464b-84db-f7118fc9b189


**Game Controls**
- Use the arrow keys (Up, Down, Left, Right) to control the snake's direction.

**Code Structure**

The code is organized into several modules:

- **main.py**: Contains the main game loop and initializes the game display.
- **game_parameters.py**: Defines constants such as WIDTH and HEIGHT of the game board and provides functions to generate random data for apples and bombs.
- **game_display.py**: Handles the graphical representation of the game using the Tkinter library.
- **board.py**: Manages the game board, including the snake, apples, and bombs.
- **apple.py**: Defines the Apple class and its functionality.
- **bomb.py**: Defines the Bomb class and its functionality.
- **snake.py**: Defines the Snake class, which represents the player-controlled snake.


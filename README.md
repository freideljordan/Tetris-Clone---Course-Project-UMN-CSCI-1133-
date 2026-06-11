# Tetris Clone
Made as the final project for my into to Computer Science course

Features:

  Classic Tetris game with all 7 tetrominoes 
  Grid based movement system animated using the turtle module
  User based movement system with arrow keys allowing the player to move blocks left and right through grid
  Automatic falling block movement through the grid made with a ticking game timer 
  Hard drop function to instantly drop a block into the lowest aviliable space below using the down arrow key
  Programmed boundry and collision detection and handling

How it works:

  A random block of the 7 tetrominoe blocks will appear at the top of the grid.
  The game utilizes an in-game clock which ticks at a constant interval to move the blocks downward without user input. 
  The user can move the blocks to the left and to the right as to fit as many blocks as they can into a row.
  The user may also use the hard drop function to immediatly place blocks into the last available space beneath.
  The board will not allow blocks to be moved outside of the play grid space and blocks will stop at the bottom of the grid given there are no blocks in    the way.

How to run:

  Make sure you have python installed (python 3 reccommended)
  Clone the repo (git clone https://github.com/your-username/Tetris-Clone.git)
  Run the program (python3 main.py)

Extra Notes:

  This project was made as the final homework assignment in my Intro to Computer Science course (UMN CSCI1133)
  This assignment's purpose was to practice creating and ultilizing classes to produce a game.
  






# FP - Mini Project 3

### Objective of the Project:

Implement a game called Heavy Ordnance with graphic interface in pygame
## Developers

- [@Rafael-j-03](https://github.com/Rafael-j-03)
- [@rodgoe](https://github.com/rodgoe)
## How our project was organized

- The code production was mostly done by Rafael José, Rodrigo Gomes also contributed to it, helping to solve some problems and some logical systems. The README.md was mostly done by Rodrigo Gomes, in which Rafael José helped composed some more information.

- 1st commit - Start screen; - Rafael José - 22202078

- 2nd commit - Implemented the bullets code and added some changes in some zones; - Rafael José - 22202078

- 3rd commit - Shortened the code eliminating some unnecessary stuff; - Rafael José - 22202078

- 4th commit - Implementation of the enemy boats also adding necessary changes for them to work accordingly; - Rafael José - 22202078

- 5th commit - Added the collision system involving the bullets and the boats; - Rafael José - 22202078

- 6th commit - LeaderBoard implemented. Some physics added to the bullet; - Rafael José - 22202078

- 7th commit - Removal of some unnecessary stuff; - Rafael José - 22202078

- 8th commit - Leaderboard upgrade. Correction on some text; - Rafael José - 22202078

- 9th commit - Markdown implementation. - Rodrigo Gomes - 22201252

- [Git Repository](https://github.com/Rafael-j-03/mini-project-3-fudamentals-of-programming)
## Development of our work

### How we organized our code

- The code is split into 4 files, main, Bullet, Enemies, Player, each containing the respective code to perform their functions in game;

- We set game window with the caption and the image as well as the the color that are going to be used;

- We have set a clock, to after set the a locked FPS;

- We have set some colors, for being easier to use the same colors after on the code, and called some essential variables for being easier to use as well;

- Then we adjusted the start screen of the game with the description "CometHeavy Ordnance" and also the option to "start", that leads us to the game, and "exit" that closes the game;

- In the start screen we added the loop so it was possible to return to this step with the correct conditions, adding the "Start" and "Exit" options;

- For the game screen we had to specify the definitions for the speed as well as action timers and keys that are pressed when the game is executing;

- While the player is alive the player's score is increased by 1 every second, we also add to set this accordingly;

- Another component we had to include in the game screen is the score count for how many points the player is making for destroying the enemy boats, adding also the condition describe above;

- As the inputs must be working properly we had to execute this by specifying each option accordingly;

- In the inputs section we specified the option to quit the game and also when the player presses the mouse button it holds the bullet and when its released the bullet is also realized, the velocity of the bullet will also depend by how time the user pressed the mouse before realize it, we had to adjust this accordingly as well;

- We added the code for the enemy boats and here we add to determine the collision with the bullets so that when it connects the boat disappears, and also increasing the difficulty every time the player is able to eliminate 10 boats. Every time a boat reaches the danger zone the player's lives is subtracted by 1;

- We also had to determine a function for checking if the bullets so that if connects with the boats or if it is out of bounds it disappears;

- If the timer (the timer will depend by the current difficulty on the game) is up and there are less than 4 enemies on the screen a new enemy boat is spawned with a random rank or size and the depending on the difficulty that the player is at the spawned delay is adjusted accordingly;

- We have specified each individual and simpler function such as checking if the player is alive and/or with lives;

- We specified the respective colors for each object on the screen so we can differentiate the different assets in this game, this includes the bullets that appear periodically on screen as well as the score and the player's lives;

- We added the "Game Over" that shows up for 2 seconds after the player lose his 3 lives;

- We added the leaderboard which is displayed for 6 seconds, in order by each player achieved the best score that appears on top in the first position and so on, if the player beat one of the top 10 best scores he will be asked to put his 3 initials, the initials of each top 10 player will be displayed in upper cases in this screen.

- For the game loop, we established an order of the different stages of the game with their respective functions, startScreen, game_Screen, gameOverScreen, write_to_leaderboard, display_leaderboard,
  
## References

- We import tow external libraries, random and math.

- The "random" like the article about it says "This module implements pseudo-random number generators for various distributions.
For integers, there is a uniform selection from a range. For sequences, there is a uniform selection of a random element, a function to generate a random permutation of a list in-place, and a function for random sampling without replacement.". And we used it to get random numbers mostly for the dices system.

- The "math" like the article about it says "This module provides access to the mathematical functions defined by the C standard.
These functions cannot be used with complex numbers; use the functions of the same name from the cmath module if you require support for complex numbers. The distinction between functions which support complex numbers and those which don’t is made since most users do not want to learn quite as much mathematics as required to understand complex numbers. Receiving an exception instead of a complex result allows earlier detection of the unexpected complex number used as a parameter, so that the programmer can determine how and why it was generated in the first place."

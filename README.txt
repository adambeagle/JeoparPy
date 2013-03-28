#######################################################
    	              JEOPARPY!
               Written by Adam Beagle 
#######################################################


**********************
* ~~ GENERAL INFO ~~ *
**********************

~~~ WHAT JEOPARPY IS ~~~

JeoparPy allows users to customize and host a game 
that includes all the sights, sounds, and excitement
of a TV quiz show! (...that is legally distinguishable 
from any such show).

It is ideal for use in a classroom setting,
and has even been known to make a great wedding shower game.

~~ WHAT JEOPARPY IS NOT ~~

JeoparPy does NOT include any pre-made sets of categories and clues,
except for placeholders to aid in formatting your own.
It is instead only designed to be used to host a custom game that the user creates.
The user can, however, create and play as many games of Jeoparpy,
with as many different sets of categories, clues, and answers, as he or she would like!


~~~~~~ DESCRIPTION ~~~~~~

Three individuals or teams compete for the highest score,
attained by correctly answering questions.
Generally, the questions posed to the teams are phrased
as 'answers,' to which the team must provide the correct
'question,' using terminology such as "What is ___?" or "Who is ___?" 

Users can customize category names, clues, and dollar amounts.
A video can be used to comprise an entire clue (Windows only), 
or an image can be used to accompany a clue.

By mapping controllers to the buzz-in keys, teams can buzz-in themselves.
 For example, the author used Bluetooth to sync Wiimotes 
to the PC. Doing this is up to the user, as instructions to 
do so are beyond the scope of this document.


-------------------------------------------------------
Warning: 
  This program is provided as-is. It was 
  created for personal use, and thus has not 
  been extensively tested, nor was a large 
  focus placed on ease of setup, use, or customization.
  I have provided instructions to the best of
  my ability to explain its use.
-------------------------------------------------------



*********************
* ~~~~~ SETUP ~~~~~ *
*********************

The following are required to run JeoparPy:
  -Python (http://www.python.org/download/)
  -Pygame (http://www.pygame.org/download.shtml)

Please note that the game has only been tested with:
  Python 2.7.3 32-bit
  Pygame 1.9.2 32-bit

JeoparPy has been tested on the following platforms:
  Windows 7 64-bit
  Ubuntu 10.10



**********************
* ~~~~ CONTROLS ~~~~ *
**********************

For more detailed instructions on how/when to use these controls, 
see the Instructions section below.

LEFT-CLICK: Opens a clue if a clue box is clicked on the main game board.
1/2/3:      These keys are used to buzz in the corresponding team.
SPACEBAR:   Press when a clue is answered correctly
BACKSPACE:  Press when a clue is answered incorrectly
END:        Press when time runs out on a clue to close it
Q:          Press to trigger the end of the game and the credits, only while the game board is showing
SHIFT+Q:    Press to close the game immediately, only while the game board is showing



**********************
* ~~ INSTRUCTIONS ~~ *
**********************

----------------------------------------------------------------
HOW TO PLAY:
----------------------------------------------------------------

To start game, double-click 'Main.pyw' in '/src' folder

Upon starting, an introduction will be played. 
When the subtitle appears, press any key to display the rules screen.

To exit the rules screen, press any key.

The categories will now scroll by, requiring no input.

The main game screen will then be displayed, and an animation will play filling in the dollar amounts.

At any point while the game board is showing, Shift+Q can be pressed to quit the game. 
Pressing only 'Q' will trigger the end-of-game animations and credits.

You now have control of the mouse. Click a clue box to display it.

When a clue box is open, a team is buzzed in by pressing their corresponding number on the keyboard.
Example: To buzz-in team 2, press '2' on your keyboard.

When a team is buzzed in, you have 2 options:
  *Press spacebar if the team answers correctly. The clue will be closed and the game board will return.
  *Press 'Backspace' if the team answers incorrectly. Another team can now buzz in. The team that answered incorrectly can not buzz in again on the same question.

If no one answers correctly and time runs out, press 'End' to close a clue and return to the game board.
    -Please note there is no timer implemented in the game at this point. A clue will not close until one of the preceding keys is pressed.
    -'End' can also be pressed while a team is buzzed in. This will close a clue completely and award no points. There shouldn't be a reason to do this in normal gameplay, but it's mentioned here for completeness and as a warning.

If all teams answer incorrectly, the clue will close automatically.

Any clue previously opened can be reopened. 
So, if a clue is clicked by mistake, press 'End.' Its dollar amount will be cleared off the board, but it can be reopened and a team can win its amount as normal. This method can be used to correct mistakes in scoring, though money can not be subtracted from a team's total at this point.

When you wish to end the game (usually when all clues have been completed), press 'Q.'
This will trigger a 'Congratulations' message to the winner, and then display the game credits.
Alternatively, Shift+Q will quit the game immediately.

No input is necessary once the end-of-game animations are triggered.
The game will close automatically after the credits.




***********************
* ~~ CUSTOMIZATION ~~ *
***********************

Note: It is recommended that the game be run once as-is 
to view the example data, and ensure the game runs without issue. 

Clues:
  * The text for the clues is located in /res/misc/
  * There are two text files with sample data included in the above folder, choose the one applicable to your platform.
  * Clues must be separated in these files by one or more blank lines
  * To create your own clues, replace the sample data with your own text, taking note of the following:
      -Clues are written starting from the top left clue box, then by column.
         ~Example: On a 5x5 board, the first 5 clues will be the clues for the leftmost category, starting at the top. The next 5 will be for the column to the right, starting at the top.
      -The line breaks in the text file dictate where the line breaks will be when the clue is printed.
         ~So, a long clue written on a single line will not display properly.
         ~There is a long example clue in the file that serves as a guide for how to format multi-line clues.


All other customization:
  *A file in /src/ called Config.py contains detailed instructions for customizing the following:
    -Category names
    -Dollar amounts for each row
    -Images/video to accompany clues
    -Subtitle that appears under game title in intro sequence
    -Screen resolution/fullscreen vs. windowed

  *Manipulating this file requires changing/adding Python code, but I have tried to write the instructions in Config.py in such a way that knowledge of Python is not needed. 
   The example data is included so it can be replaced, and its format followed.
    


**********************
* ~~ KNOWN ISSUES ~~ *
**********************

  1. Until the main game board is shown, it is recommended not to press any keys or click the mouse unless prompted. 
     Doing so, during the category scroll for example, may freeze the display for a brief time.
     A similar problem may occur during the end-of-game animations.

  2. On the Linux machine tested (Ubuntu 10.10) attempting to open a video clue crashed the program, and occasionally the OS.



**************************
* ~ FUTURE DEVELOPMENT ~ *
**************************

This project is on hold, and is provided as-is. 
However, should development resume, I would like to implement the following, in no particular order:
  
  * Ability to choose to use a timer (with a customizable timeout) on clues

  * A better way to change team scores, in case of a mistake or disagreement.
    Currently money cannot be subtracted from a team.

  * Simpler customization of clues/categories/media

  * Better support for different display resolutions (at least a 4:3 mode)

  * Better support for in-game videos (may not be possible due to limitations of Pygame).

  * Easily customizable team/player names

  * General refactoring and optimization of code.
    (This was my first Pygame project, and it was made with a short deadline; There are no doubt some less than ideal coding practices at times)



**********************
* ~~~~~~ LEGAL ~~~~~ *
**********************

All code contained in this package
Copyright (C) 2013 Adam Beagle - All Rights Reserved

You may use, distribute, and modify this code under the 
terms of the GNU General Public License, 
viewable at http://opensource.org/licenses/GPL-3.0

No copyright infringement is intended with the use of any file contained within this package.
The use of any copyrighted works in this program was done under the Fair Use doctrine, however any infringing file will gladly be removed and replaced upon request.
This program is non-commercial and was created for educational purposes.


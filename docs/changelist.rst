==========================
VERSION HISTORY - JeoparPy
==========================

*************
Version 0.9.3
*************

* Bug fix: The fixed font-size issue has been resolved. Clues, player names, categories, amounts, and the rules can now be arbitrary lengths, and their font size will be scaled accordingly and their text properly fit.
* The line breaks in clues.txt no longer need to be manually entered. If a clue is written on a single line, it will automatically be fit when drawn; if manual line breaks are done, they will be honored, though the font size may be scaled to ensure the entire clue fits on the screen.
* Improvements to image clues. Images are now automatically scaled if too large, and are guaranteed at least the bottom third of the clue screen for display area. Like in other clues, text in image clues is scaled to fit as well.
* Bug fix: A crash could occur during the credits sequence if the global FPS limit was particularly low (less than approx. 30 FPS). This has been fixed.
* The category scroll sequence is now animated relative to the global FPS limit.


*************
Version 0.9.2
*************

* Refactored the state transition handling code in main.py. Transitions now broken explicitly into those triggered by events, those that are immediate and follow a linear flow, and those that branch to differing next states based on UI and GameData conditions. Maybe more importantly, the state transition functions in main now only set states; related code triggered by state changes, previously in main, refactored to controller and gamedata modules.


*************
Version 0.9.1
*************

* Customizable timeout on answers added. See /src/jeoparpy/config.py to set.
* Mouse pointer is now hidden while a clue is open.
* Images now allowed in credits; credits updated.
* Cleaned up a few sound clips (noise removal, EQ).


***********
Version 0.9
***********

* Audio can now be used as clue media. Pressing 'm' in an audio clue will trigger the audio and allow buzz-ins. See /src/jeoparpy/ui/resmaps.py for information on creating audio clues.
* An "audio reading," a recorded version of the clues text, can be assigned to clues. If an audio reading exists, it plays automatically when a clue is opened, and players are not allowed to buzz in until it has finished playing. See /src/jeoparpy/ui/resmaps.py for information on assigning audio readings.
* Bug fix: Case-sensitive filename issue was causing problems when running on Linux.
* Customization made simpler by removing MEDIA in /src/jeoparpy/ui/config.py. Vast majority of customization now done in three places: /res/text, /src/jeoparpy/config.py, and /src/jeoparpy/ui/resmaps.py.


*************
Version 0.8.1
*************

* New setting in root config.py that controls whether money is negated on incorrect answers. Negative scores are drawn as red in-game.
* Rules are now set in /res/text/rules.txt, and drawn as rendered text, rather than taken from an image. This allows customization of rules.
* Game can be quit during credits by pressing 'Q.'


***********
Version 0.8
***********

This version is the result of a complete and total rewrite of the game.
The only feature missing from the old version is the ability to play videos in clues. This was removed as it was an ordeal to convert videos to the proper format, and video use was not cross-platform.

At the typical user level, the major changes are:
* The game will function and look as intended at any widescreen (16:9 or 16:10) resolution, fullscreen or not. Resolutions up to 1920x1200 are tested and confirmed to look as intended..
* Visuals (especially timing of animations) will look much more consistent across systems.
* The placement of customizable game attributes has changed. All primary attributes (categories, clues, player names, clue amounts, subtitle) are now located in /res/text/ to reduce confusion.
* There is one file for clues, rather than the old system of unix-style and one windows-style file. The user is responsible for end-of-line characters being formatted for their platform.

Under the hood, major changes are:
* There is now a well-defined package/sub-package structure to the game, separating game logic and presentation.
* The game now operates as a finite state machine, so the UI modules update based on state and can operate independently of each other, main, and the game logic.
* All code is formatted using PEP8 standards.
* Small changes are too numerous to list here, as every module was rewritten.


***********
Version 0.1
***********

This was the original version of the game in its completed state.
The combination of it being my first attempt at writing a game with Pygame, 
as well as being made with a tight deadline resulted in a bit of a disaster of
poor coding practices, though it did function as intended.

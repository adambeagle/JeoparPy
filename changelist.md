CHANGELIST - JeoparPy
================

###Version 0.1###

This was the original version of the game in its completed state.
The combination of it being my first attempt at writing a game with Pygame, 
as well as being made with a tight deadline resulted in a bit of a disaster of
poor coding practices, though it did function as intended.

###Version 0.8###

The current version of the game in the master branch.

This version is the result of a complete and total rebuild of the game.
The only feature missing from the old version is the ability to play videos in clues. This was removed as it was an ordeal to convert videos to the proper format, and video use was not cross-platform.

At the typical user level, the major changes are:
* The game will function and look as intended at any 16:9 resolution, fullscreen or not. (Note that resolutions above 1920x1080 may not look ideal due to scaling).
* Visuals (especially timing of animations) will look much more consistent across systems.
* The placement of customizable game attributes has changed. All primary attributes (categories, clues, player names, clue amounts, subtitle) are now located in /res/text/ to reduce confusion.
* There is one file for clues, rather than the old system of unix-style and one windows-style file. The user is responsible for end-of-line characters being formatted for their platform.

Under the hood, major changes are:
* There is now a well-defined package/sub-package structure to the game, separating game logic and presentation.
* The game now operates as a finite state machine, so the UI modules update based on state and can operate independently of each other, main, and the game logic.
* All code is formatted using PEP8 standards.
* Small changes are too numerous to list here, as every module was rewritten.

###Future changes###
* See todo.md in the dev/ folder.
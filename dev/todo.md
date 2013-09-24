# Todo #

### Immediate ###

### High priority ###
* Fix fixed font-size issue.
    Font sizes are currently scaled for the resolution, but not scaled for length of text.
    Badly effects player names, category names, clues.
	Could, but not likely to, effect subtitle amounts, and rules.
* Refactor state transitions in main. Update methods in GameData and Controller should handle 
  state transitions of their respective attributes.

### Low priority ###
* Logging
* Write a generic fade_in_surface function (similar tasks done in intro and outro)
* Make categoryscroll honor global FPS limit

### Down the Road ###
* Make intro animation more interesting.
* Make outro animation (currently do_congrats) more interesting.
* Customizable timeout on clues
* 'Undo' key command to negate last points given, in case of mistake or disagreement.
* Accelerate/decelerate category scroll to make it smoother.
* Daily doubles
* Final JeoparPy

### Blue Sky ###
* 4:3 mode

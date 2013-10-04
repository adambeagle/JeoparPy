# Todo #

### Immediate ###

### High priority ###
* Fix fixed font-size issue.
    Font sizes are currently scaled for the resolution, but not scaled for length of text.
    Badly effects player names, category names, clues.
	Could, but not likely to, effect subtitle amounts, and rules.
	
	UPDATE:
	  Fixed in gameboard and categoryscroll, fixed for rules in intro.

### Low priority ###
* Logging
* Write a generic fade_in_surface function (similar tasks done in intro and outro)
* GameState arg should be kwargs-like-dict to clarify code that gets/sets the state args.

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

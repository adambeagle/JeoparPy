from sys import argv

from jeoparpy import config
from jeoparpy.constants import (DEBUG_FLAG, FULLSCREEN_FLAG, SKIP_INTRO_FLAG, 
    WINDOWED_FLAG)

optionsMap = {
    '-d'           : DEBUG_FLAG,
    '--debug'      : DEBUG_FLAG,
    '-f'           : FULLSCREEN_FLAG,
    '--fullscreen' : FULLSCREEN_FLAG,
    '-s'           : SKIP_INTRO_FLAG,
    '--skip-intro' : SKIP_INTRO_FLAG,
    '-w'           : WINDOWED_FLAG,
    '--windowed'   : WINDOWED_FLAG,
}

if __name__ == '__main__':
    flags = set(optionsMap[o] for o in argv if o in optionsMap)
    
    # Override config options if args provided
    if FULLSCREEN_FLAG in flags:
        config.FULLSCREEN = 1
    if WINDOWED_FLAG in flags:
        config.FULLSCREEN = 0
    if DEBUG_FLAG in flags:
        config.DEBUG = 1
    
    # main MUST be imported here, or config options may be imported
    # (via 'from config import X') prior to being overridden by argv 
    # options.
    from jeoparpy.main import main
    main(*flags)

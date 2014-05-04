from pygame import event as pgevent, time as pgtime

class Timer(object):
    """
    Defines a timer that can post a provided event when its time expires.
    
    Users of this class should call its update() method on every frame once
    the timer is started.
    
    Note this class is deigned to work only with pygame. 
    It uses pygame.time.get_ticks() to determine when to end and posts
    events to pygame's event queue.
    
    ATTRIBUTES:
      * endTime (read-only)
      * event
      * isOn (read-only)
      * length
      
    METHODS:
      * reset
      * start
      * update
    """
    def __init__(self, length, event=None):
        """
        'length' in miliseconds. If 'event' provided, it will be posted
        when the timer expires ('length' ms after start() is called).
        """
        self.length = length
        self.event = event
        self._endTime = None
        
    def reset(self):
        """Reset the timer."""
        self._endTime = None

    def start(self):
        """
        Starts the timer. Return the time (via pygame.time.get_ticks()) at which
        the timer started.
        """
        time = pgtime.get_ticks()
        self._endTime = time + self.length
        
        return time

    def update(self):
        """
        Updates the timer, ending it and rasing self.event if enough
        time has passed.
        
        Return current time (via pygame.time.get_ticks()) if timer running,
        else None.
        
        It is safe to call this method on every frame; It does nothing if
        the timer has not been started with start().
        """
        if self.isOn:
            time = pgtime.get_ticks()
            
            if time >= self._endTime:
                self._end()
                
            return time
            
        return None
                
    def _end(self):
        """
        Reset the timer and post self.event to the queue. Called when time reaches
        self._endTime.
        """
        self.reset()
        pgevent.post(pgevent.Event(self.event))

    @property
    def endTime(self):
        return self._endTime

    @property
    def isOn(self):
        return self._endTime is not None

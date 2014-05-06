"""
util.py

DESCRIPTION:
  General file, sequence, and type utility functions used throughout the
  application. These functions are from my custom library but are
  reproduced here to avoid an annoying dependency for anyone wishing to
  clone JeoparPy.


Copyright (C) 2013 Adam Beagle - All Rights Reserved
You may use, distribute, and modify this code under
the terms of the GNU General Public License,
viewable at http://opensource.org/licenses/GPL-3.0

This copyright notice must be retained with any use
of source code from this file.
"""
from decimal import Decimal


def chunker(sequence, size, overlap=False):
    """
    Generator; Yield chunks of a sequence of length 'size,' in order.
    If overlap is set, yield overlapping chunks (i.e. indices 0 and 1, 
    then 1 and 2), otherwise chunks do not overlap.
    
    If sequence length is not evenly divisible by size and overlap is False,
    ignore extra elements at the end of the sequence.
    """
    if size < 1:
        raise ValueError("'size' must exceed 0. Value passed was %r." % size)
    
    i = 0
    step = 1 if overlap else size
    len_ = len(sequence)

    while i + size <= len_:
        yield sequence[i:i+size]
        i += step

def get_stripped_nonempty_file_lines(path):
    """
    Return tuple of all nonempty lines in a file after they have been
    stripped of leading and trailing whitespace.
    """
    lines = []

    with open(path, 'r') as f:
        for line in f:
            stripped = line.strip()
            if len(stripped):
                lines.append(stripped)

    return tuple(lines)

def get_first_textline(path, ignore=None):
    """
    Return first line with any non-whitespace text from file in passed path,
    or an empty string if no line found.
    
    'ignore' can be a single string or sequence of strings (or None).
    If 'ignore' is passed, the first line not beginning with any of the
    elements of ignore will be returned.

    WARNING: If ignore contains an empty string, nothing will be returned. 
    This is normal behavior of builtin startswith().
    """
    retLine = ''

    if isinstance(ignore, basestring):
        ignore = (ignore,)

    if not ignore:
        ignore = ()

    with open(path, 'r') as f:
        for line in f:
            stripped = line.strip()
            
            if len(stripped) > 0 and not stripped.startswith(ignore):
                retLine = stripped
                break

    return retLine

def to_numeric(val):
    """
    Return 'val' as a numeric type, if possible.
    
    If 'val' already a numeric type, return it unchanged.
    Otherwise, if 'val' cannot be cast to int or float, raise TypeError
    or ValueError.
    """
    if type(val) in (int, float) or isinstance(val, Decimal):
        return val
    
    try:
        return int(val)
    except ValueError:
        return float(val)

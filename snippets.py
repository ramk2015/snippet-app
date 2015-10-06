import logging
#set the log output file and the log level
logging.basicConfig(filename="snippets.log", level=logging.DEBUG)

"""logging module splits log messages into one of 5 severity levels:
DEBUG:  Detailed info, for diagnosing
INFO:   Confirmation that things are working as expected
WARNING: Indication that something unexpected happened. The software is still working as expected
ERROR: Due to a more serious problem, the software has not been able to perform some function
CRITICAL: A serious error, indicating that the program itself may be unable to continue running.
"""

def put(name,snippet):
    """
    Store a snippet with an associated name
    Returns the name and snippet 
    """
    logging.error("FIXME: Unimplemented - put({!r}, {!r})".format(name,snippet))
    return name,snippet
    
"""Formattign the string with the !r modifier means that the repr() function will be run over the data
to provide the output. repr() returns a string containing a printable representation of an object"""

def get(name):
    """Retrieve the snippet with a given name
    If there is no such snippet ...
    Returns the snippet.
    """
    logging.error("FIXME: Unimplemented - get({!r})".format(name))
    return ""
    
    
    
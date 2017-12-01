#!/usr/bin/env python
from dcnmtoolkit import VTEP
from dcnmtoolkit import Session


try:
    from credentials import URL, LOGIN, PASSWORD
except ImportError:
    print
    print 'To run live tests, please create a credentials.py file with the following variables filled in:'
    print """
    URL = ''
    LOGIN = ''
    PASSWORD = ''
    """

def main():
   # put code here
    pass

if __name__ == "__main__":
    # execute only if run as a script
    main()
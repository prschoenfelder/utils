""" out_utils.py
A collection of universally applicable util functions concerning console 
outputs and print statements.
"""

import sys
from io import StringIO

# class to be used as context manager to silence any function
class SilencedStdOut:
    ''' to be used as a context manager to prevent any function from writing
    output to the console
    ( c.f. https://stackoverflow.com/questions/65608502/is-there-a-way-
    to-force-any-function-to-not-be-verbose-in-python/65608914#65608914 )
    '''

    def __enter__(self):
        self.old_stdout = sys.stdout
        self.result = StringIO()
        sys.stdout = self.result

    def __exit__(self, *args, **kwargs):
        sys.stdout = self.old_stdout
        # result_string = self.result.getvalue() # use if you want or discard

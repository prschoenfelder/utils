""" nlp_utils.py
A collection of universally applicable util functions concerning operation
system related tasks.
"""

import os

def make_dirs(list_of_paths):
    ''' Creates directories according to list of specified paths.
    '''

    # create all specified paths
    for path in list_of_paths:

        # check if path exists and if not, create it
        if not os.path.exists(path):
            os.makedirs(path) 

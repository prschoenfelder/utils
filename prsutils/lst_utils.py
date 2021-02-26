""" lst_utils.py
A collection of universally applicable util functions concerning list
manipulation.
"""


def flattenNestedList(nestedList):
    ''' Converts a nested list to a flat list
    c.f.
    https://thispointer.com/python-convert-list-of-lists-or-nested-list-to-flat-list/
    '''

    flatList = []
    # Iterate over all the elements in given list
    for elem in nestedList:
        # Check if type of element is list
        if isinstance(elem, list):
            # Extend the flat list by adding contents of this element (list)
            flatList.extend(flattenNestedList(elem))
        else:
            # Append the elemengt to the list
            flatList.append(elem)
    return flatList

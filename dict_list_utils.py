#-------------------------------------------------------------------------------
# Name:        dict_list_utils
# Purpose:
#
# Author:      elle.migeon
#
# -*- coding: UTF-8 -*-
#
# Created:     11-11-2019
# Copyright:   (c) elle.migeon 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

def get_missing_keys (dict_ref, dict_to_compare):
    """Create a function called get_missing_keys that has two
    Dictionary parameters:  dict_ref and dict_to_compare where dict_to_compare
    is the dictionary that may have missing keys and dict_ref is the dictionary
    you want to compare it to. The get_missing_keys function returns a list of
    missing keys or an empty list if no keys are missing. Make sure you add a
    test for the case where there are no keys missing. """

    if dict_to_compare.has_key(2):
        return
    else:
        return []

def get_missing_keys_with_count (dict_ref, dict_to_compare):
    """return a tuple containing the number of missing keys and the list of
    missing keys. This function can call get_missing_keys to get the list so
    you don't duplicate its code."""

    get_missing_keys()
    return value1, value2

def get_unique (in_list):
    """May have duplicate values and returns a list of only unique values."""
    return list(dict.fromkeys(in_list))
    mylist = get_unique([1, 2, 2, 3, 4, 5])
    print(mylist)

def flatten_list (in_list):
    """in_list refers to a list that may contain other lists and/or tuples.
    This function will return a list that contains the items of the list that are
    not lists or tuples as well as the items of the list(s) or tuples(s).  The lists
    and tuples of in_list will be removed.
    For example, if in_list = [1, (2,3), [4,5]], the returned list would be
    [1, 2, 3, 4, 5]"""

    flatten_list = [item for sublist in l for item in sublist]
    return flatten_list

if __name__ == '__main__':
    main()
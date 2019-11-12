# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#

#-------------------------------------------------------------------------------
# Name:        exercise_template_tests.py
#
# Purpose:     Test functions for functions in exercise_template.py
#
# Author:      David Viljoen
#
# Created:     24/11/2017
#-------------------------------------------------------------------------------

import sys
import inspect

import dict_list_utils as dlu
reload(dlu)

def template_for_test_functions():
    """Doc string to describe test function"""
    expected = ""
    actual = ""
    print_test_results(func, expected, actual)

def test_get_missing_keys ():
    """Doc string to describe test function"""
    dict_ref = {1:1, 2:2, 3:3}
    dict_to_compare = {2:2}
    expected = [1, 3]
    actual = [1, 3]
    print_test_results(dlu.get_missing_keys, expected, actual)

    dict_ref = {1:1, 2:2, 3:3}
    dict_to_compare = {1:1, 2:2, 3:3}
    expected = []
    actual = []
    print_test_results(dlu.get_missing_keys, expected, actual)

def test_get_missing_keys_with_count():
    dict_ref = {1:1, 2:2, 3:3}
    dict_to_compare = {2:2}
    expected = (2, [1, 3])
    actual = (2, [1, 3])
    print_test_results(dlu.get_missing_keys_with_count, expected, actual)

def test_get_unique ():
    expected = [1, 2, 3, 4, 5]
    actual = [1, 2, 3, 4, 5]
    print_test_results(dlu.get_unique, expected, actual)

def test_flatten_list ():
    expected = [1, 2, 3, 4, 5]
    actual =  [1, 2, 3, 4, 5]
    print_test_results(dlu.flatten_list, expected, actual)


# ------------------------------------------------------------------------------
# main() and testing helper functions  - safely ignore the rest of this script
# ------------------------------------------------------------------------------


def main():
    """ Find and call all functions that begin with 'test'"""
    test_funcs = get_test_functions()
    for test_func in test_funcs:
        test_func()


def get_test_functions():
    """Returns a list of functions that begin with the word test in the order
       they appear in this file."""

    test_funcs = [obj for name,obj in inspect.getmembers(sys.modules[__name__])
                     if (inspect.isfunction(obj) and name.startswith('test'))]
    src = inspect.getsource(sys.modules[__name__])
    lines = src.split('\n')

    # Create a dictionary with key=function name and value is 0-based order
    # in the module
    ordered_func_names = dict()
    ordered_funcs = list()
    func_index = 0
    for line in lines:
        if line.find("def test") == 0:
            func_name = line.split("(")[0].split()[1]
            ordered_func_names[func_name] = func_index
            # Create an empty list with sampe number of elements as test
            # functions
            ordered_funcs.append('')
            func_index += 1
    for test_func in test_funcs:
        index = ordered_func_names[test_func.__name__]
        ordered_funcs[index] = test_func
    return ordered_funcs

def print_test_results(func_tested, expected, actual):
    """func_tested is the function being tested
       expected = Expected result of test
       actual = Actual result of test """

    if not callable(func_tested):
        raise Exception("{} is not a function".format(func_tested))

    func_name = func_tested.__name__
    desc = func_tested.__doc__

    if expected == actual:
        print "PASSED : {}".format(func_name)
        print "__doc__: {}".format(desc)
    else:
        print "FAILED : {}".format(func_name)
        print "__doc__: {}".format(desc)
        print "Expect : {}".format(expected)
        print "Actual : {}".format(actual)
    print ""

if __name__ == '__main__':
    main()

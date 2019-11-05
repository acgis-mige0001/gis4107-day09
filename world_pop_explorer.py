# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------------
# Name:        world_pop_explorer.py
#
# Purpose:     Provide some functions to analyze the data in
#              world_pop_by_country.py
#
# Author:      David Viljoen
#
# Created:     24/11/2017
#-------------------------------------------------------------------------------

from world_pop_by_country import data as country_pop

# Key = country and value is number (i.e. not text containing commas)
#
country_pop_dict = {}

def main():
    lines = country_pop.split('\n')
    print "country_populations has the following columns:"
    print lines[0]
    print repr(lines[0])
    ci = lines[162]
    print "\nData is UTF-8 encoded.  That is, printed as is:"
    print ci
    print "\nData prined with .decode('utf-8'):"
    print ci.decode('utf-8')

def get_country_count():
    """Return the number of countries in country_populations.  Create a list
	   where each element of the list contains a line of data from
	   country_populations and return the length of this list"""
    lines = country_pop.split('\n')
    return len(lines) - 1

def conv_num_with_commas(number_text):
    """Convert a number with commas (str) to a number.
       e.g. '1,000' would be converted to 1000"""




def get_top_five_countries():
    """Return a list of names of the top five countries in terms of population"""

    pass

def set_country_populations_dict():
    """Sets the country_populations_dict dictionary where key is country name
         and value is a tuple containing two elements:
            1. A numeric version of the comma separated number in the
               Pop 01Jul2017 column
            2. The % change as a positive or negative number
    """

    pass


def get_population(country_name):
    """Given the name of the country, return the population as of 01Jul2017
       from country_populations_dict.  If the country_populations_dict is
       empty (i.e. no keys or values), then run set_country_populations_dict
       to initialize it."""

    pass

def get_continents():
    """Return the list of continents"""
    return ['Asia']


def get_continent_populations():
    """Returns a dict where the key is the name of the continent and
       the value is the total of all countries on that continent"""

    pass

if __name__ == '__main__':
    main()

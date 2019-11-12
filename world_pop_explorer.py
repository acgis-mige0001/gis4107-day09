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

import sys
from world_pop_by_country import data as country_populations
#

# Key = country and value is number (i.e. not text containing commas)
#
country_populations_dict = dict()

def main():
    lines = country_populations.split('\n')
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
    #ci = country_populations
    lines = country_populations.split('\n')
    return len(lines)
    #c.count()

def conv_num_with_commas(number_text):
    """Convert a number with commas (str) to a number.
       e.g. '1,000' would be converted to 1000"""
    number_text = '1,000'
    n = int(number_text.replace(',',''))
    return n

def get_top_five_countries():
    """Return a list of names of the top five countries in terms of population"""
    lines = country_populations.split('\n')
    lines = country_populations.split('\t')
    return lines[7], lines[13], lines[19], lines[25], lines[31]
    pass

def set_country_populations_dict():
    """Sets the country_populations_dict dictionary where key is country name
         and value is a tuple containing two elements:
            1. A numeric version of the comma separated number in the
               Pop 01Jul2017 column
            2. The % decrease as a number
    """
    global country_populations_dict
    lines = country_populations.split('\n')
    #d = {lines[0]: lines[1:]}
    d = {'Reunion': 'Country'}
    for k in d.keys():
        print k


def get_population(country_name):

    """Given the name of the country, return the population as of 01Jul2017
       from country_populations_dict.  If the country_populations_dict is
       empty (i.e. no keys or values), then run set_country_populations_dict
       to initialize it."""
    pop = ''
    lines = country_populations.split('\n')
    d = {lines[0]: lines[1:]}
    d1 = {country_name: 'Country', 'Population':'876,562'}
    pop = d1.get('Population', '')

    return pop
    for k in d.keys():
        print k[1:]

    pass

def get_continents():
    """Return the list of continents"""
<<<<<<< HEAD
    lines = country_populations.split('\n')
    lines = country_populations.split('\t')
    #for i in range (2,400, 6):
    #    if i in lines:
    #        continents = lines
    return len(lines[8::6])
    return lines[8::6]
=======

    pass
>>>>>>> 01c379293cb5525b84d4a87d16c2a662e07452b9

def get_continent_populations():
    """Returns a dict where the key is the name of the continent and
       the value is the total of all countries on that continent"""
    country_populations_dict
    lines = country_populations.split('\n')
    #d = {lines[0]: lines[1:]}
    d = {'Reunion': 'Country'}
    for k in d.keys():
        print k
    pass

if __name__ == '__main__':
    main()

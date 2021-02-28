#! /bin/python3
#  Spring 2020 (PJW)

import csv
import json 

#
#  Some example data that could appear in a file.
#  It has four fields, an ID, a group letter, an income
#  level and a number of household members. The ID and 
#  group letters are intended to be strings and the others
#  are numeric.
#

lines = [ 
    'id,group,inc,n\n',
    '1,a,35162,1\n',
    '2,c,104750,3\n',
    '3,b,56410,2\n'
    ]

#
#  Create a DictReader object to read the data. It will
#  use the first line as a list of dictionary keys and 
#  will return a corresponding dictionary for each subsequent
#  line.
#

reader = csv.DictReader(lines)

#%%
#  Now make a list of the data items by walking through the 
#  lines one at a time using DictReader. Change some to 
#  numerical values along the way
#

household_list = []
for hh in reader:
    hh['inc'] = float( hh['inc'] )
    hh['n'] = int( hh['n'] )
    household_list.append(hh)

#%%
#  Print what we found
#

print("\nHousehold information:")
print( json.dumps(household_list,indent=4) )
          
#%%
#
#  Now use it to build a list of the per capita income of 
#  individuals (one entry for each person in each household)
#

person_list = []

for hh in household_list:
    
    # Extract the income and number of household members
    
    inc = hh['inc']
    n = hh['n']
    
    # compute per capita income
    
    pc = round(inc/n)

    # Make an entry for each member of the household. When called
    # with one argument range() returns a list of integers starting
    # at 0 and ending just before the value of the argument. 
    
    for i in range(n):
        person_list.append(pc)

#%%
#
#  Print the result
#

print("\nIndividual information:")
print( json.dumps(person_list,indent=4) )

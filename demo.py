"""
demo.py
Spring 2022 PJW

Demonstrate using csv.DictReader() to read a CSV file.
"""

import csv
import json

#
#  Name of the input data file
#

input_data = "demo.csv"

#%% Open file
#
#  Open the input file and create a DictReader object to
#  read the data.
#
#  It will use the first line as a list of dictionary keys and
#  will return a corresponding dictionary for each subsequent
#  line.
#

fh = open(input_data)
reader = csv.DictReader(fh)

#%% Read data
#
#  Now make a list of the data items by walking through the
#  lines one at a time using DictReader. Change some to
#  numerical values along the way, and remove extra whitespace
#  from the others
#

household_list = []
for hh in reader:
    hh['id'] = hh['id'].strip()
    hh['name'] = hh['name'].strip()
    hh['inc'] = float( hh['inc'] )
    hh['n'] = int( hh['n'] )
    household_list.append(hh)

#%% Print data
#
#  Print what we found
#

print("\nHousehold information:")
print( json.dumps(household_list,indent=4) )

#
#  Compute the average household income
#

num_hh = len(household_list)

incomes =[hh['inc'] for hh in household_list]
tot_inc = sum(incomes)

avg_hh_income = round(tot_inc/num_hh)

print(f"\nTotal households: {num_hh}")
print(f"Average household income: {avg_hh_income}")

#
#  Compute the average per capita income
#

individuals =[hh['n'] for hh in household_list]
num_ind = sum(individuals)

avg_pc_inc = round(tot_inc/num_ind)

print(f"\nTotal individuals: {num_ind}")
print(f"Average per capita income: {avg_pc_inc}")

#%%
#
#  Now use it to build a list of the per capita income of
#  individuals (one entry for each person in each household)
#

person_list = []

for hh in household_list:

    #
    #  Extract the income and number of household members
    #

    inc = hh['inc']
    n = hh['n']

    #
    #  Compute per capita income
    #

    pc = round(inc/n)

    #
    #  Make an entry for each member of the household. When called
    #  with one argument range() returns a list of integers starting
    #  at 0 and ending just before the value of the argument.
    #
    #  In effect, this expands the data from one record per household
    #  to one record per individual. Each individual gets the household's
    #  average per capita income.
    #

    for i in range(n):
        person_list.append( {'name':hh['name'], 'n':i+1, 'pc_inc':pc} )

#%%
#
#  Print the result
#

print("\nContents of person_list:\n")

for person in person_list:
    print( person['name'], person['n'], person['pc_inc'] )

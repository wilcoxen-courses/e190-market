#! /bin/python3
#  Spring 2020 (PJW)

import json 

#
#  Some example data that could appear in a file.
#  It has four fields, an ID, a group letter, and two 
#  parameters, a and b. The ID and group letters are 
#  strings and the remaining three items are numeric.
#

lines = [ 
    '1 a 12345 0.2 100\n',
    '2 c 54321 0.3 150\n',
    '3 b 23231 0.1 200\n'
    ]

#
#  Make a list of the data items by walking through the 
#  lines one at a time.
#

item_list = []
for line in lines:

    #
    #  A nice way to split up a line in pieces is to use 
    #  a tuple as the left side. It saves having to pull the
    #  elements out using something like parts = line.split() 
    #  and then num = parts[0], group = parts[1], etc
    #

    (num,group,inc,a,b) = line.split()

    #  
    #  Make a new item from the pieces and append it to the 
    #  list. Note the use of float() to convert the three 
    #  items to numeric values.
    #

    new_item = {
        'num':num,
        'group':group,
        'inc':float(inc),
        'a':float(a),
        'b':float(b)
        }
    item_list.append(new_item)

#
#  Now print what we found
#

print( json.dumps(item_list,indent=4) )
          

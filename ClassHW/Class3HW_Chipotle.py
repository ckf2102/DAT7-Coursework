'''
Python Homework with Chipotle data
https://github.com/TheUpshot/chipotle
'''

'''
BASIC LEVEL
PART 1: Read in the data with csv.reader() and store it in a list of lists called 'data'.
Hint: This is a TSV file, and csv.reader() needs to be told how to handle it.
      https://docs.python.org/2/library/csv.html
'''

import csv
with open('chipotle.tsv', 'rU') as f:
    data = [row for row in csv.reader(f, delimiter="\t")]


'''
BASIC LEVEL
PART 2: Separate the header and data into two different lists.
'''

header = data[0]
data = data[1:]



'''
INTERMEDIATE LEVEL
PART 3: Calculate the average price of an order.
Hint: Examine the data to see if the 'quantity' column is relevant to this calculation.
Hint: Think carefully about the simplest way to do this!
'''

total_order = []
sum_items = float(data[0][4].strip("$"))

# for all rows
#   if the order number of row x is equal to the order number of the previous row
#       add the $$ of the item to the running sum of $$ (for a specific order)
#   else add the sum of $$ to the total_order list and re-initialize the sum of $$
#   for the next order
#       basically, if the current row's order number is not the same as the previous
#       row's order number, then record what you've got as the $$ (which is for the 
#       previous order) and then start a new running sum for the new order number

for x in range(1, len(data)):
    if data[x][0] == data[x-1][0]:
        sum_items = sum_items + float(data[x][4].strip("$"))
    else:
        total_order.append(sum_items)
        sum_items = float(data[x][4].strip("$"))

# add the last order. because of the way the code is written, it skips out
# on the last order since orders are recorded AFTER it flags that there's a new
# order
total_order.append(sum_items)

print "the average price of an order is $" + str(round(sum(total_order)/len(total_order),2))

# this was the hardest one for me. i have a feeling this is not the simplest way.

'''
INTERMEDIATE LEVEL
PART 4: Create a list (or set) of all unique sodas and soft drinks that they sell.
Note: Just look for 'Canned Soda' and 'Canned Soft Drink', and ignore other drinks like 'Izze'.
'''
search_str1 = "Canned Soda"
search_str2 = "Canned Soft Drink"

soda_list = []

# for each row in the data
#   if the search strings show up under item_name then add the choice_description
#   to the soda list

for x in data:
    if (search_str1 in x[2]) or (search_str2 in x[2]):
        soda_list.append(x[3])
        
set(soda_list)

'''
ADVANCED LEVEL
PART 5: Calculate the average number of toppings per burrito.
Note: Let's ignore the 'quantity' column to simplify this task.
Hint: Think carefully about the easiest way to count the number of toppings!
'''

burrito_str = "Burrito"

sum_toppings = 0
sum_burritos = 0

# for each row in the data
#   if burrito shows up in item_name then
#       running total of sum of toppings = previous total + the number of commas
#           + 1 (since it's listed like A, B, C)
#       running total of # of burrito orders = previous total + 1

for x in data:
    if burrito_str in x[2]:
        sum_toppings = sum_toppings + x[3].count(",") + 1
        sum_burritos = sum_burritos + 1

print "the average number of toppings is " + str(float(sum_toppings)/sum_burritos)


'''
ADVANCED LEVEL
PART 6: Create a dictionary in which the keys represent chip orders and
  the values represent the total number of orders.
Expected output: {'Chips and Roasted Chili-Corn Salsa': 18, ... }
Note: Please take the 'quantity' column into account!
Optional: Learn how to use 'defaultdict' to simplify your code.
'''

chips_str = "Chips"
chips = []

# adding all chip orders to a single list
# for each row in the data
#   if the search string shows up in item_name
#       add to the chips list depending on the quantity of chip orders

for x in data:
    if chips_str in x[2]:
        for y in range(0,int(x[1])):
            chips.append(x[2])

from collections import defaultdict

# use defaultdict to count the number of occurrences of the key (chip orders)
# and return as the value

chip_count = defaultdict(int)
for chip in chips:
    chip_count[chip] += 1
    
'''
BONUS: Think of a question about this data that interests you, and then answer it!

For all chips ordered (any kind), how many of those were part of multi-item orders?
'''

orders = [x[0] for x in data]

order_count = defaultdict(int)
for order in orders:
    order_count[order] += 1

chip_orders = []

for x in data:
    if chips_str in x[2]:
        chip_orders.append(x[0])
        
multi_orders = []

for x in chip_orders:
    if order_count[x] > 1:
        multi_orders.append(x)

len(multi_orders)

# turns out no one orders just chips at chipotle

"""
let's try the same but with Canned Soft Drinks, Canned Soda, or 6 pack
"""

search_str3 = "6 Pack Soft Drink"

soda_orders = []

for x in data:
    if (search_str1 in x[2]) or (search_str2 in x[2]) or (search_str3 in x[2]):
        soda_orders.append(x[0])

multi_soda_orders = []

for x in soda_orders:
    if order_count[x] > 1:
        multi_soda_orders.append(x)

len(soda_orders)
len(multi_soda_orders)

# again, turns out no one orders just soft drinks at chipotle

"""
better question? how often do people add chips to their entree
"""

meal_orders = []

# assuming all entrees have either "Bowl", "Burrito", "Tacos", or "Salad" in them
# probably easier way to do this by making that a list

meal_str1 = "Bowl"
meal_str2 = "Burrito"
meal_str3 = "Tacos"
meal_str4 = "Salad"

for x in data:
    if (meal_str1 in x[2]) or (meal_str2 in x[2]) or (meal_str3 in x[2]) or (meal_str4 in x[2]):
        meal_orders.append(x[0])

meal_orders = list(set(meal_orders))
chip_orders = list(set(chip_orders))

# now i have a list of meal order numbers (meal_orders)
# and a list of all chip order numbers (chip_orders)

# i don't like nested for loops

sum_chips_meals = 0

for x in meal_orders:
    for y in chip_orders:
        if x == y:
            sum_chips_meals += 1

print str(round((float(sum_chips_meals)/len(meal_orders) * 100),2)) + "% of entree orders also included chips"




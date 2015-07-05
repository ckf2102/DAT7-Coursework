## Class 2 Homework - Chipotle
### due 8 June 2015

**Question 1: Using chipotle.tsv in the data subdirectory...**

*Look at the head and the tail, and think for a minute about how the data is structured. What do you think each column means? What do you think each row means? Tell me! (If you're unsure, look at more of the file contents.)*

Each row is a specific item that was ordered.

order_id = the ID number of an order. An order can contain multiple items, thus there may be multiple rows with the same order_id

quantity = the amount of the item that was ordered

item_name = the name of the item ordered, including the meat if it's an entree.

choice_description = for drinks, this can indicate a particular flavor. For entrees, this is a list of the toppings in the order [type of salsa [other toppings]].

item_price = the price of the item

*How many orders do there appear to be?*

```
$ sort chipotle.tsv
$ tail chipotle.tsv
```

There appears to be 1834 orders

*How many lines are in the file?*

```
$ wc -l chipotle.tsv
```

4623 lines

*Which burrito is more popular, steak or chicken?*

```
$ grep -i "chicken burrito" chipotle.tsv | wc -l
$ grep -i "steak burrito" chipotle.tsv | wc -l
```

There are 553 lines of chicken burrito and 368 lines of steak burrito; chicken burrito is more popular.

*Do chicken burritos more often have black beans or pinto beans?*

```
$ grep -i "chicken burrito" chipotle.tsv > chickenburritos.txt
$ grep -i "black beans" chickenburritos.txt | wc -l
$ grep -i "pinto beans" chickenburritos.txt | wc -l
```

Chicken burritos more often have black beans (282) than pinto beans (105).

**Question 2: Make a list of all of the CSV or TSV files in the DAT7 repo (using a single command). Think about how wildcard characters can help you with this task.**

```
# when in the DAT7 repo
$ find . -name "*.?sv"
# in the directory containing the DAT7 repo
$ find DAT7 -name "*.?sv"
```

- airlines.csv
- chipotle.tsv
- drinks.csv
- imdb_1000.csv
- sms.tsv
- ufo.csv

**Question 3: Count the number of occurrences of the word 'dictionary' (regardless of case) across all files in the DAT7 repo.**
```
$ grep -r -i "dictionary" . | wc -l
```

16 occurences of dictionary

**Question 4: Optional: Use the the command line to discover something "interesting" about the Chipotle data. The advanced commands below may be helpful to you!**


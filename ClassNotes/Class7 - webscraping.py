# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 19:37:21 2015

@author: Corinne
"""

'''
CLASS: Web Scraping with Beautiful Soup

What is web scraping?
- Extracting information from websites (simulates a human copying and pasting)
- Based on finding patterns in website code (usually HTML)

What are best practices for web scraping?
- Scraping too many pages too fast can get your IP address blocked
- Pay attention to the robots exclusion standard (robots.txt)
    - a text file at the root of most websites
    - purpose: tell bots/scrapers what they can and cannot do
    - structured way to tell the bot what to do
    - communicating rules
    - look for user agent *, and what is disallowed (directories)
- Let's look at http://www.imdb.com/robots.txt

What is HTML?
- Code interpreted by a web browser to produce ("render") a web page
- Let's look at example.html
- Tags are opened and closed
- Tags have optional attributes

How to view HTML code:
- To view the entire page: "View Source" or "View Page Source" or "Show Page Source"
- To view a specific part: "Inspect Element"
    - will highlight the code of the section that you clicked on

- Safari users: Safari menu, Preferences, Advanced, Show Develop menu in menu bar
- Let's inspect example.html
'''

# read the HTML code for a web page and save as a string
# anytime you are not reading something into a dataframe, can't use pandas

with open('example.html', 'rU') as f:
    html = f.read()
    # return as single strand, which is what we want

# convert HTML into a structured Soup object
# beware of different versions
from bs4 import BeautifulSoup
b = BeautifulSoup(html)
    # kind of a function where you pass html and returns a soup object

print b.prettify()  # shows nesting

# 'find' method returns the first matching Tag (and everything inside of it)
b.find(name='body')
b.find(name = 'h1')         # type is element tag
b.find(name = 'h1').text    # pulls out the text in the tag
b.find(name = 'h1')['id']   # puts the name of the attribute of the tag
                            # and returns the value of that attribute
b.find(name = 'p')          # returns a tag, and only the first one
b.find_all(name = 'p')      # returns all matches
                            # returns a result set, which is like a LIST of tags

# ResultSets are a lot like lists
len(b.find_all(name = 'p'))
b.find_all(name = 'p')[0]
b.find_all(name = 'p')[1].text
b.find_all(name = 'p')[1]['id']     # pull out the value of the attribute

# iterate over a ResultSet
# allows you to pull out the text only (which is good for the scraping!)
results = b.find_all(name = 'p')
for tag in results:
    print tag.text

# limit search by Tag attribute
b.find(name = 'p', attrs={'id':'scraping'})
    # this is where finding patterns in webscraping comes into play
    # look for the characteristics of the thing you're looking for
b.find_all(name = 'p', attrs={'class':'topic'})
    # REMEMBER: ResultSet does not have TEXT attribute

# limit search to specific sections
# chaining find statements
b.find(name = 'body').find(name = 'h1')
    # nest things together to narrow your scope
b.find(name = 'ul', attrs={'id':'scraping'}).find_all(name = 'li')

"""
Exercise
"""

# find the h2 tag and print its text

b.find(name = 'h2').text

# find the 'p' tag with the 'id' value of 'reproducibility' and print its text

b.find(name = 'p', attrs={'id':'reproducibility'}).text

# find the first 'p' tag and print out value of 'id' attribute

b.find(name ='p')['id']

# print text of all 4 resources

resources =  b.find_all(name = 'li')
for tag in resources:
    print tag.text
    
resources =  b.find_all(name = 'ul')
for tag in resources:
    print tag.text


# print text of only API resources

api = b.find(name = 'ul').find_all(name = 'li')
for tag in api:
    print tag.text

"""
Scraping the IMDB website
"""

# get the html of shawshank redemption page
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import requests
r = requests.get('http://www.imdb.com/title/tt0111161/')
    # requests.get is useful to talking to any website

# convert HTML into Soup
b = BeautifulSoup(r.text)

b.find(name='span', attrs={'itemprop':'name', 'class':'itemprop'}).text
b.find_all(name='span', attrs={'itemprop':'name', 'class':'itemprop'})
    # examine all of the occurrences
b.find(name='h1').find(name='span', attrs={'itemprop':'name', 'class':'itemprop'})

# getting the star rating
b.find(name = 'span', attrs={'itemprop':'ratingValue'}).text
float(b.find(name = 'div', attrs={'class':'titlePageSprite star-box-giga-star'}).text)

"""
Exercise Two
"""

# get the description

b.find_all(name = 'p', attrs={'itemprop':'description'})

# get the content rating

b.find(name = 'meta', attrs={'itemprop':'contentRating'})['content']

# get duration

int(b.find(name = 'time', attrs={'itemprop':'duration'})['datetime'][2:-1])






























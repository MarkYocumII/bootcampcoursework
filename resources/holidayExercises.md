# Holiday Exercises

This group of exercises is meant for you all to review material during the winter break so that we may hit the ground running! It is broken up by topic, so feel free to jump around as you see fit. My personal recommendation is that you work top to bottom, and if there is something you feel like you can't do off of the top of your head, go ahead and complete the exercise. You do not have to do the bonus exercises, but I think some will pose a useful challenge to keep your skills sharp.

## Terminal Commands

For these exercises, you may ONLY use the terminal.

- `cd` into your Documents folder, and create a new folder. Call it "holiday_exercises"
- in /holiday_exercises, create another folder called "terminal_exercises"
- in /terminal_exercises, create a file called newFile.py
- rename newFile.py to main.py 
- create a folder called "data"
- in /data, create a file called data.csv (DIFFICULT BONUS: use vim or emacs to write data in data.csv)
- copy the contents of /terminal_exercises into a new folder at the same level called "copy_folder"
- in /copy_folder, create a folder called "libs"
- in /libs, create a file called schrodinger.py
- copy the contents of /copy_folder/libs into a new libs folder under /terminal_exercises
- delete copy_folder


## Git - High Priority

- create a new project on github called git_holiday_exercises. You may initialize it with a README.md if you so choose.
- create a folder in your Documents folder, and call it "holiday_exercises"
- in /holiday_exercises, clone git_holiday_exercises
- in /git_holiday_exercises, if you did not create it with a README.md, create that file now using `touch`, then make a commit.
- create a .gitignore file using `touch`
- in .gitignore, ignore config.py, \_\_pycache__, and dirac.ipynb. Make a commit.
- create a config.py using terminal commands, then edit it; add a variable called `favorite` and set its value to be your favorite movie. Make a commit.
- create a new jupyter notebook file using jupyter, and name it dirac.ipynb. 
- in dirac.ipynb, import the contents of config.py, then `print()` it. Save, then make a commit.
- push your commits to github.
- (Bonus: move your config into a new folder called "libs", change your .gitignore, and modify your dirac.ipynb to instead import "libs" instead of config.py directly)

## Python Fundamentals

These exercises may be completed in _either_ a python script (.py) or a jupyter notebook (.ipynb).

- create a new folder in your Documents, and call it "holiday_exercises"
- in /holiday_exercises, create a new python script or jupyter notebook
- create a dictionary called "faves", and give it keys and values for your favorite_movie, favorite_song, and favorite_food
- create a for-loop to iterate over the dictionary and print each of the keys *and* values. 
- create a second dictionary called "unfaves", and give it keys and values for your least_favorite_movie, least_favorite_song, and least_favorite_food
- create a list, and place both the faves and unfaves dictionaries in it.
- write a function that prints each of the values in each of the dictionaries in the list
- write a function that accepts two numbers, and returns the product.
- write a function that accepts two strings, and returns the concatenation of the two strings
- write a function that accepts accepts a string, and returns the original string without the last two letters
- BONUS: write a function that accepts a string, and returns the original string without vowels. High five someone when you finish this.


## Pandas

For these exercises, you may use this data set: 
```python
[{
    "shelf": 3,
    "rack": 1,
    "item": "sketchy banana",
    "inventory":1,
    "price": 1
},{
    "shelf": 2,
    "rack": 4,
    "item": "lone bacon slice",
    "inventory":1,
    "price":2
},{
    "shelf": 5,
    "rack": 3,
    "item": "holiday cheer",
    "inventory":20,
    "price":5.10
},{
    "shelf": 2,
    "rack": 1,
    "item": "empirical pineapple",
    "inventory":11,
    "price":3
},{
    "shelf": 2,
    "rack": 2,
    "item": "lone bacon slice",
    "inventory":1,
    "price":2  
},{
    "shelf": 3,
    "rack": 1,
    "item": "kosher pepper",
    "inventory":2,
    "price": 2.30
},{
    "shelf": 3,
    "rack": 2,
    "item": "kosher pepper",
    "inventory":2,
    "price": "ducky"
}]
```

- create a new dataframe using this data.
- replace the price "ducky" with the appropriate price for a kosher pepper
- select *only* the shelf column. identify which shelves (1-5) are not in use. 
- select *only* the rack column. identify which racks (1-5) are not in use.
- select rows with low inventory (below five items).
- create a groupby dataframe on the item column, find the total inventory for each item. **Note, do NOT sum the rack and the shelf columns. This would be considered an error**  
- calculate the total number of items in inventory
- calculate the total value of items in inventory



## Matplotlib

For these exercises, please use the dataset in the [#Pandas](#pandas) section. You may need to clean the data.

- create a bar plot of the number of items on each shelf
- create a bar plot of the number of items on each rack
- create a bar plot of the inventory for each item
- create a scatter plot of the price vs inventory of the items in the store
- modify the scatter plot such that the size of the points is relative to the amount of inventory for each item.
- create a pie plot for the percentage of inventory each item takes up

## API's

For these exercises, we will use the [pplapi](http://pplapi.com). You will need to [utilize the documentation](http://pplapi.com/docs/learn/api_by_example.html).

- use the  `requests` library to make a GET request to the API on the batch route to get a group of 5 american users
- determine the most prevalent religion for your group of users
- determine the average agreeableness for your set of users
- calculate the range of neuroticism for your set of users
- (DIFFICULT BONUS: calculate the ages of your users, and determine the range of ages)
- write a function to make your request, and carry out the above calculations.
- write a loop to run the function 5 times, then calculate the aggregate statistics of _all 25_ users. 
- high five someone for finishing this section


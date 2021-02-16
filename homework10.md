# Advanced Topics in Computer Science
## Homework 10::  Lookout Spotify! Part 2 (20 pts)
### Due: February 15, 2021
#### SUBMISSION FILE: lastname\_hw10.py OR lastname\_hw10.ipynb OR lastname\_hw10.zip
__!! submit with the correct file name !!__

---

#### Note On Group Work

For this assignment you __may__ get assistance from your classmates. You __may not__ use resources online. If you have any questions or doubts defintely ask.

__DO NOT MAKE ANY ASSUMPTIONS ON WHAT IS OR IS NOT A VALID SOURCE!__. 

__ASK ME!__ 

---

## On Code Quality 


### Code Readability
The readability of your code __will__ matter this time. Make sure that you are using variable, class, function, and method names that are descriptive. Make sure that you are not being _too_ clever with your code, or that if you are you use comments to explain non-obvious statements and expressions. Use document strings to summarize the output of function and method calls. The purpose of this is __NOT__ busy work. The purpose of this is to make your code more readable for others, even if others is _Future You_.

### Testing
You are expected to use tests when developing your code. We have not covered this in class, but this is an excellent habit of professional coders. This does not have to be an onerous exercise. Simply using ```assert``` statements liberally will get you a lot of mileage.

### Logging
To help with your development and debugging consider using the Python ```logging``` module. Read here, [Python Logging](https://realpython.com/python-logging/) for a quick overview of how to use it. Below is an example usage.

```
import logging


def setup_logging(level=logging.DEBUG):
  logging.basicConfig(level=level, format='%(asctime)s{%(levelname)s} %(message)s',datefmt='%H:%M:%S')
  
  # shorthand convenience methods for using logger
  global debug, warn, info, error, crash
  
  debug = logging.debug
  warn = logging.warning
  info = logging.info
  error = logging.error
  crash = logging.critical

# initialize logger
# debug and warn messages will be skipped
setup_logging(logging.WARNING)

```
---

# Problem Set

## Song Types
If we assume that people have fairly consistent tastes then we would expect to see songs in the same genres to cluster to getter. Let's see if this is in fact true in our dataset.

### Part 1 Database Creation

To do this you will need to first transpose the database. Currently the database is indexed by ```student_id``` and contains a dictionary of ```song_name```, ```rating``` pairs as values per student. You need to transpose the dictionary so that it is indexed by ```song_name``` and contains a dictionary of ```student_id```, ```rating``` pairs as values per song.  

Create a transposed database called ```song_key_db```. Write 5 assertions, of your own design, to verify that you correctly transposed the database.

### Part 2 A Crude Evaluation Dataset

To test the predictions that you will make in part 3 listen to the songs on Spotify and YouTube. Come up with your own classification system for the song genres and group the songs into categories. Create a spreadsheet in Google Docs that has the song_name and the genres for each song. Make sure that you use a consistent genre name for your songs so that the data can be filtered consistently.

### Part 3 Similarity Test

Run your similarity code on the ```song_key_db``` and use the results to group the most similar songs into categories. You should run your anlysis with bot similarity functions and use the one that gives you the best results. Report the song groupings in a Google spreadsheet. For each of the songs record its group, and its average similarity to the other songs in the group. For the entire group record the average similarity score.

### Part 4 Bonus

Google _Tanimoto Coefficient_ and implement it as a similarity score for the dataset. Note, you will have to use the version of the metric for continuous variables.

Once you have implemented it compare the similarity results to a previous problem that used _Pearson's Correlation Coefficient_ and _euclidean distance_ to the results using the _Tanimoto Coefficient_.


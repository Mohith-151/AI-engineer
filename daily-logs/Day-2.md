# Day 2: OOPS, HTTP(GET,status code and JSON) 

**Date:** 2005-10-06
**Hours studied:** 3
**Energy (1-5):** 2

## What I learned (3-5 bullets, own words)
- Learned About the .get() to request a server for some content.. but didn't used yet
- Built a class on my Own, which had some errors which is later fixed by claude
- There will be always shortway or the robust way in the python coding
- We can't use .str.title() directly on the df['str type columns'], so use lambda funtion inside df['column].apply()
- __init__ funtion should only be used for assign variable,dataframs etc.. Not used to call the Function(which is bad habit in future)
## What I built or coded today
- Built a data cleaner class, which takes a datafram, strip downs the whitespaces, drops NULL entries and duplicate entries and also handles the impossible age like -5 and 250.
- The [Notebook](../notebooks/Day-2.ipynb) where I did initial check on the dataset
- The [Python file](../projects/data_cleaning_class.py) where The data_cleaner class is coded.

## What broke, and how I fixed it
- Problem: DataFram does not contain str
- Cause: we can perform .str funtions on dataFrame
- Fix: used .apply() and Lambda funtion to tackle this issue

## One thing I still don't understand
- how to Shorten the Code Length Using some pro ways to robust the process

## Self-test (answer without looking at notes)
1. Q: How call a function which inside a class
   A: using a Object or directly,
      - Object:
      ``` 
      object = class_name() 
      object.fucntion_name()
      ```
      - Directly:
      ```
      class_name.function_name()
      ```
## Tomorrow's first task
- Should Complete the API request Task 1st thing in the Morning

---
---
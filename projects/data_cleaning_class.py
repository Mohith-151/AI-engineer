import pandas as pd
import numpy as np

dataset=  pd.read_csv('datasets/data_cleaner_class.csv')

class data_cleaner:
  def __init__(self, dataset):
    self.db = dataset
    self.strip_text()
    self.normal_text()
    self.drop_nulls()
    self.remove_duplicated()
    self.handling_age()

  def strip_text(self):
    # self.db['name'] = self.db['name'].str.strip()
    # self.db['email'] = self.db['email'].str.strip()
    # self.db['city'] = self.db['city'].str.strip()
    # OR we can USE
    trg_cols = ['name','email','city','salary']
    self.db[trg_cols] = self.db[trg_cols].apply(lambda x: x.str.strip())
    self.db[trg_cols] = self.db[trg_cols].replace('',np.nan) # replaces the just spaces entry to nan so it can removed while dropna()

  def normal_text(self):
    title_cols = ['name','city']
    self.db[title_cols] = self.db[title_cols].apply(lambda x:x.str.title())
    self.db['email'] = self.db['email'].str.lower()

  def print_delete_rows(self,step,rows):
    print(f'The Number of Rows deleted in process {step} is {rows}')

  def drop_nulls(self):
    initial_rows = len(self.db)
    self.db = self.db.dropna()
    deleted_rows = initial_rows - len(self.db)
    self.print_delete_rows('Dropping NULL',deleted_rows)

  def remove_duplicated(self):
    initial_rows = len(self.db)
    self.db = self.db.drop_duplicates(subset = ['email'])
    
    deleted_rows = initial_rows - len(self.db)
    self.print_delete_rows('Dropping Duplicates ',deleted_rows)

  def handling_age(self):
    initial_rows = len(self.db)
    self.db = self.db[self.db['age'].between(0,120)]
    deleted_rows = initial_rows - len(self.db)
    self.print_delete_rows('Removing ages which are in range of 0 - 120',deleted_rows)

  def final_dataset(self):
    print("THE Cleaned DATASET : \n")
    print(self.db)
    print("\n")
    print("DATASET information \n")
    print(self.db.info())
    print("\n")
    print("NULL entry Info :\n")
    print(self.db.isnull().sum())
    print("\n")

cleaner = data_cleaner(dataset)
cleaner.final_dataset()
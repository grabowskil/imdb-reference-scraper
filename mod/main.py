import csv
import sys
from ast import literal_eval
from crawler import acc_csv
from analyzer import functions
csv.field_size_limit(sys.maxsize)

def getYear(link):
  row = acc_csv.getRow(link)
  title = row[0]
  titleNestOpenPos = title.index('(') if '(' in title else None
  titleNestClosePos = title.index(')') if ')' in title else None
  if titleNestOpenPos == None and titleNestClosePos == None:
    #get year from imdb
  elif titleNestClosPos == None:
    year = title[titleOpenPos :]
  else:
    year = title[titleOpenPos : titleClosePos]
  return int(year)
  
def getMaxYear():
  maxTitle = functions.getTop(1)
  maxYear = getYear(maxTitle[0][0])
  return int(maxYear)
  
def getWeight(link):
  year = getYear(link)
  maxYear = getMaxYear()
  dif = maxYear - year
  #develope weight

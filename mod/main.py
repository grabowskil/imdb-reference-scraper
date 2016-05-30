import csv
import sys
import sqlite3
from ast import literal_eval
from crawler import acc_csv
from analyzer import functions
csv.field_size_limit(sys.maxsize)

def getYear(link):
  row = acc_csv.getRow(link)
  if row != None:
    title = row[0]
    titleNestOpenPos = title.index('(') if '(' in title else None
    titleNestClosePos = title.index(')') if ')' in title else None
    if titleNestOpenPos == None and titleNestClosePos == None:
      year = 0
      #get year from imdb
    elif titleNestClosePos == None:
      year = title[titleNestOpenPos + 1 :]
    else:
      year = title[titleNestOpenPos + 1 : titleNestClosePos]
    try:
      iyear = int(year)
    except:
      iyear = 0
    return iyear
  else:
    return 0
  
def getMaxYear():
  maxTitle = functions.getTop(1)
  maxYear = getYear(maxTitle[0][0])
  return int(maxYear)
  
def getWeight(link):
  year = getYear(link)
  maxYear = getMaxYear()
  dif = maxYear - year
  #develope weight

def updateDB():
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS reference;")
    cur.execute("CREATE TABLE reference (name, connections, count, link, weight);")
    
    with open('data.csv', 'rt') as fileData:
      dr = csv.reader(fileData, delimiter=';')
      
      to_db = [(i[0], i[1], i[2], i[3], getWeight(i[3])) for i in dr]
    
    cur.executemany("INSERT INTO reference (name, connections, count, link, weight) VALUES (?, ?, ?, ?, ?);", to_db)
    con.commit()

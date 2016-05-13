import csv
import sys
from ast import literal_eval
csv.field_size_limit(sys.maxsize)

def getRows():
    rows = sum(1 for row in csv.reader(open('data.csv'))) + 1
    return rows

def getRow(link:
    reader = csv.reader(open('data.csv'), delimiter=';')
    for row in reader:
        if row[3] == title:
            return row
            
def getDivList(link):
    div_list = literal_eval(getRow(title)[1])
    return div_list   
    
def titleInList(title):
    reader = csv.reader(open('data.csv'), delimiter=';')
    title_list = []
    for row in reader:
        title_list.append(row[0])
    if title in title_list:
        return True
    else:
        return False
        
def linkInList(link):
    reader = csv.reader(open('data.csv'), delimiter=';')
    link_list = []
    for row in reader:
        link_list.append(row[3])
    if link in link_list:
        return True
    else:
        return False
    
def writeCsv(title, div_list, link):
    trgtFile = open('data.csv', 'a', newline='')
    writer = csv.writer(trgtFile, delimiter = ';')
    data = [title, div_list, len(div_list), link]
    writer.writerow(data)
    trgtFile.close()
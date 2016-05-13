import csv
import sys
csv.field_size_limit(sys.maxsize)

def getRows():
    rows = sum(1 for row in csv.reader(open('data.csv'))) + 1
    return rows

def getRow(title):
    reader = csv.reader(open('data.csv'), delimiter=';')
    for row in reader:
        if row[0] == title:
            return row
            
def getDivList(title):
    div_list = getRow(title)[1]
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
        
#def linkInList(link):
#    link_list = []
#    for row in reader:
#        for link in row[1][1]
#            link_list.append(link)
#    if link in link_list:
#        return True
#    else:
#        return False
    
def writeCsv(title, div_list):
    trgtFile = open('data.csv', 'a', newline='')
    writer = csv.writer(trgtFile, delimiter = ';')
    data = [title, div_list, len(div_list)]
    writer.writerow(data)
    trgtFile.close()
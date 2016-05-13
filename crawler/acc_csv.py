import csv

def getRow():
    rows = sum(1 for row in csv.reader(open('data.csv'))) + 1
    return rows
    
def inList(title):
    included_cols = [3]
    reader = csv.reader(open('data.csv'), delimiter=';')
    title_list = []
    for row in reader:
        title_list.append(row[0])
    if title in title_list:
        return True
    else:
        return False
    
def writeCsv(title, div_list):
    trgtFile = open('data.csv', 'a', newline='')
    writer = csv.writer(trgtFile, delimiter = ';')
    data = [title, div_list, len(div_list)]
    writer.writerow(data)
    trgtFile.close()
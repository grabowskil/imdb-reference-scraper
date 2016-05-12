import csv

def getRow():
    rows = sum(1 for row in csv.reader(open('data.csv'))) + 1
    return rows

def writeCsv(title, div_list):
    trgtFile = open('data.csv', 'a', newline='')
    writer = csv.writer(trgtFile, delimiter = ';')
    data = [title, div_list, len(div_list)]
    writer.writerow(data)
    trgtFile.close()
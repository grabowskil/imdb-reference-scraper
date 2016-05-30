import argparse
from analyzer import main as anal
from mod import main as modi

parser = argparse.ArgumentParser(description='analyze scraped references from imdb')
parser.add_argument('-p', '--print', type=int, help="prints the defined number of movies")
parser.add_argument('-r', '--refresh', action='store_true', help="refreshes the 'data.db' database from the 'data.csv'")

args = parser.parse_args()

if args.print != None:
    anal.printTop(args.print)
elif args.refresh != None:
    modi.updateDB()
else:
    parser.parse_args(['-h'])

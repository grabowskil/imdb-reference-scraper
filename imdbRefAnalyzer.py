import argparse
from analyzer import main

parser = argparse.ArgumentParser(description='analyze scraped references from imdb')
parser.add_argument('-p', '--print', action='store_true', help="if parsed 'true', the top 10 movies from data.csv get printed")

args = parser.parse_args()

if args.print == True:
    main.printTopTen()
else:
    parser.parse_args(['-h'])
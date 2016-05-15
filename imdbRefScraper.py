import argparse
from crawler import main

parser = argparse.ArgumentParser(description='scrape references from imdb')
parser.add_argument('-d', '--levelDepth', type=int, help='depth, the crawler should go. Watch out: depth >0 will take a long time, which increases exponentially!')
parser.add_argument('-iL', '--initialLink', type=str, help="parses the initial title-link, format: 'title/tt0000000', make sure the title exists on imdb! Default: 'The Matrix'")
parser.add_argument('-t', '--time', type=int, help='specify amount of seconds, the scraper waits at least between every call. Default: 5')
parser.add_argument('-a', '--all', action='store_true', help="if parsed 'true', videos, tv shows and games will be crawled. Default: false")
parser.add_argument('-r', '--recursive', action='store_true', help="if parsed 'true', the crawler will try to restart the scraper in case of urllib Error -3 (can have unintended consequences!")

args = parser.parse_args()

if args.levelDepth == None:
    parser.parse_args(['-h'])
else:
    print("crawler will be launched with '-a' " + str(args.all))
    print("crawler will be launched with '-r' " + str(args.recursive))
    main.imdbCrawler(args.levelDepth, args.initialLink, args.time, args.all, args.recursive)

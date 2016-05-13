from . import scraper

def imdbCrawler(levelDepth=0, init_titleLink='/title/tt0133093', wait_time=5, all=False):
    if levelDepth == None: levelDepth = 0
    if init_titleLink == None: init_titleLink = '/title/tt0133093'
    if wait_time == None: wait_time = 5
    if all == None: all = False
    #print("level of Depth: " + str(levelDepth) + " initial title Link: " + str(init_titleLink) + " wait time: " + str(wait_time))
    print("crawler: start on level: " + str(levelDepth))
    div_list = scraper.imdbScraper(init_titleLink, wait_time, all)
    c = 0
    for _ in range(levelDepth):
        if div_list != '404' and div_list != None:
            for div in div_list:
                next_link = div[1]
                imdbCrawler(levelDepth-1, next_link, wait_time, all)
    c = len(div_list)
    print("crawler: " + str(c) + "done on level " + str(levelDepth))
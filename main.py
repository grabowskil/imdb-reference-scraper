import requests
import time
from bs4 import BeautifulSoup
import acc_csv

def imdbScraper(titleLink, wait_time=5):
    r = requests.get('http://www.imdb.com' + titleLink + '/movieconnections')
    
    start_time = time.time()
    
    print("open new title")
    if r.status_code != 404:
        print("no 404")
        soup = BeautifulSoup(r.text, 'lxml')
        
        title_tag = soup.head.title.contents
        title_str = stripTitle(str(title_tag))
        
        print("new title = " + title_str)
        
        ref_heading = soup.find('a', attrs={'name':'referenced_in'})
        
        div_list = []
        
        if ref_heading != None:
        
            ref_divs = ref_heading.find_next_siblings('div')
            ref_divsCount = len(ref_divs)

            c = False
            cntr = 0
            
            for div in ref_divs:
                cntr += 1
                print("{:.1%}".format(cntr/ref_divsCount), end='\r')
                if c == False:
                    div_list.append([div.a.contents, div.a['href']])
                if div.next_sibling.next_sibling == soup.find('a', attrs={'name':'spoofed_in'}): c = True
                
        print("writing in csv")
        acc_csv.writeCsv(title_str, div_list)
        
        elapsed_time = time.time() - start_time
        if elapsed_time < wait_time:
            sleep_time = wait_time - elapsed_time
            print("need to wait {:.0} seconds".format(sleep_time))
            time.sleep(sleep_time)
        
        return div_list
    else:
        print('404d :-(')
        return '404'
    
def stripTitle(title):
    titleQuotPos = title.index("'") if "'" in title else None
    titleHypPos = title.index('-') if '-' in title else None
    if titleQuotPos == None and titleHypPos ==None:
        return title
    elif titleQuotPos == None:
        return title[: titleHypPos - 1]
    else:
        return title[titleQuotPos + 1 : titleHypPos - 1]
    
def imdbCrawler(levelDepth=0, init_titleLink='/title/tt0133093', wait_time=5):
    if levelDepth == None: levelDepth = 0
    if init_titleLink == None: init_titleLink = '/title/tt0133093'
    if wait_time == None: wait_time = 5
    div_list = imdbScraper(init_titleLink, wait_time)
    for _ in range(levelDepth):
        if div_list != '404':
            for div in div_list:
                next_link = div[1]
                imdbCrawler(levelDepth-1, next_link, wait_time)
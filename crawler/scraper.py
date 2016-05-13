import requests
import time
from bs4 import BeautifulSoup
from . import acc_csv

def imdbScraper(titleLink, wait_time=5, all=False):
    div_list = []
    if acc_csv.linkInList(titleLink) == False:
        r = requests.get('http://www.imdb.com' + titleLink + '/movieconnections')
        start_time = time.time()
        title_str = 'not retrieved yet'
        print("scraper: open new title", end='\r')
        if r.status_code != 404:
            print("request: new title opened")
            soup = BeautifulSoup(r.text, 'lxml')
            title_tag = soup.head.title.contents
            title_str = stripTitle(str(title_tag))
            if contExcluded(title_str) == False or all == True:
                print("scraper: next title '" + title_str + "'")
                ref_heading = soup.find('a', attrs={'name':'referenced_in'})
                if ref_heading != None:
                    ref_divs = ref_heading.find_next_siblings('div')
                    ref_divsCount = len(ref_divs)
                    c = False
                    cntr = 0
                    for div in ref_divs:
                        cntr += 1
                        print("loading: {:.1%}".format(cntr/ref_divsCount), end='\r')
                        if c == False:
                            div_content = div.a.contents
                            div_href = div.a['href']
                            div_list.append([div_content, div_href])
                        if div.next_sibling.next_sibling == soup.find('a', attrs={'name':'spoofed_in'}): c = True
                    print("scraper: writing in csv")
                else:
                    print('scraper: skipped, not referenced')
            else:
                print('scraper: skipped, exclude')
                
        else:
            print('request: 404')
            return '404'
        elapsed_time = time.time() - start_time
        if elapsed_time < wait_time:
            sleep_time = wait_time - elapsed_time
            print("request: need to wait {:.1} seconds".format(sleep_time))
            time.sleep(sleep_time)
        acc_csv.writeCsv(title_str, div_list, titleLink)
        return div_list
    else:
        print("scraper: known link, just parsing div_list")
        div_list = acc_csv.getDivList(titleLink)
        return div_list
    
def stripTitle(title):
    titleHypPos = title.index('-') if '-' in title else None
    titleNestPos = title.index('[') if '[' in title else None
    if titleNestPos == None and titleHypPos == None:
        return title
    elif titleNestPos == None:
        return title[: titleHypPos - 1]
    else:
        return title[titleNestPos + 2 : titleHypPos - 1]
        
def contExcluded(div_content):
    ex_list = ['(TV Episode', '(Video', '(TV Movie']
    c = False
    for ex in ex_list:
        if ex in div_content:
            c = True
            break
    return c
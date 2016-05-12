from bs4 import BeautifulSoup
import requests
import time

def test_none():
    r = requests.get('https://www.google.com')
    soup = BeautifulSoup(r.text, 'lxml')
    ref_heading = soup.find('a', attrs={'class':'utter nonsense'})
    
    print(type(ref_heading))
    if ref_heading == None:
        print('you got it!')

def test_strStripper():
    testval = "['Matrix (1999) - Connections - IMDb']"

    tv_nestPos = testval.index('(')
    tv_dotPos = testval.index("'")

    tv = testval[tv_dotPos + 1:tv_nestPos - 1]

    print(tv)
    print(len(tv), len('Matrix'))
    
def test_time():
    start_time = time.time()
    print(start_time)
    elapsed_time = time.time()-start_time
    print(elapsed_time)
    if elapsed_time < 4:
        sleep_time = 4 - elapsed_time
        print(sleep_time)
        print("need to wait {:.0} seconds".format(sleep_time))
        time.sleep(sleep_time)
    print('done')
    
def test_slashR():
    print("something, something\r", end='\r')
    print("another, another\r")
    print("different")
    
test_time()
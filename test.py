from bs4 import BeautifulSoup
import requests

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
    
test_none()
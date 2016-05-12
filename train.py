import requests
import re
from bs4 import BeautifulSoup

r = requests.get("http://newyork.craigslist.org/search/aap")

r.raise_for_status()

#html = r.text
soup = BeautifulSoup(r.text, 'lxml')

price_spans = soup.select('span.price')

#matches = re.findall(r"\$(\d+)",html)
#prices = list(map(int,matches))
prices = [int(span.text[1:]) for span in price_spans]

print("Highest price: ${}".format(max(prices)))
print("Lowest price: ${}".format(min(prices)))
print("Average price: ${}".format(sum(prices)/len(prices)))
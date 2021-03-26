import requests
import re

web_sites = [
    "https://finance.yahoo.com/quote/GME?p=GME&.tsrc=fin-srch"
]

r = re.compile(r'data-reactid="50">(.*?)</span>', re.MULTILINE)

for web_site in web_sites:

    response = requests.get(web_site)
    content = response.text
    match = r.search(content)
    gme_price = match.groups()[0]

    with open("gme_price.txt", "a") as price_file:
        price_file.write(gme_price + "\n")

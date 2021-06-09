
import requests, sys, webbrowser, bs4

keywords = sys.argv[1]

for x in sys.argv[2:]:
    keywords = keywords + "+"+ x

print(keywords)

req = requests.get("https://www.google.com/search?q="+keywords)
soup = bs4.BeautifulSoup(req.text, 'html.parser')
linkelems = soup.select('.package-snippet')

numOpen = min(5, len(linkelems))
for link in range(numOpen):
    urlToOpen = 'https://pypi.org'+ linkElems[i].get('href')
    print('OPening', urlToOpen)
    webbrowser.open(urlToOpen)


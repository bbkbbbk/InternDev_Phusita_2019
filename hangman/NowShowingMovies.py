from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

try:
    url = 'https://www.imdb.com/movies-in-theaters/?ref_=cs_inth'
    uTitle = urlopen(url)
    page_html = uTitle.read()
    uTitle.close()
except:
    print('Cannot load the url.')

page_soup = soup(page_html, 'html.parser')

titles = page_soup.findAll('td', {'class':'overview-top'})
summaries = page_soup.findAll('div', {'class':'outline'})

movies = []

for item in range(len(titles)):
    name = str(titles[item].a.text.strip())
    summary = str(summaries[item].text.strip())
    movie = {'name':name, 'hint':summary}
    movies.append(movie)




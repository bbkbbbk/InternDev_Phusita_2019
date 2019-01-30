from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

try:
    url = 'https://open.spotify.com/playlist/37i9dQZEVXbMDoHDwVN2tF'
    uSpotify = urlopen(url)
    spotify_html = uSpotify.read()
    uSpotify.close()
except:
    print('Cannot load the url.')

spotify_soup = soup(spotify_html, 'html.parser')

raw_songs = spotify_soup.findAll('span', {'class':'track-name'})
raw_artist = spotify_soup.findAll('span', {'class':'artists-albums'})

songs = []
artists = []
for song in raw_songs:
    songs.append(song.text)
for artist in raw_artist:
    temp = artist.text.split('•')
    people = []
    for item in range(len(temp))[:len(temp)-1]: #exclude album
        if ',' in temp[item]:
            person = temp[item].split(',')
            for i in range(len(person)):
                person[i] = person[i].strip()
        else:
            person = temp[item].strip()
            artists.append(person)
            break
        people.append(person)
        artists.append(person)

words = []
for i in range(len(songs)):
    word = {'name':songs[i], 'hint':artists[i]}
    words.append(word)


import requests
from bs4 import BeautifulSoup

# Scrapping transfermarket functions

# Variables
#headers_tf = {'User-Agent': 
#           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
#url_tf = "https://www.transfermarkt.co.uk/transfers/transferrekorde/statistik/top/plus/0/galerie/0?saison_id=2019"

# Defining request and parsing
def getAndParseURL(url, headers=None):
    if headers==None:
        urlRequest = requests.get(url)
    else:
        urlRequest = requests.get(url, headers=headers)
    soup = BeautifulSoup(urlRequest.content, 'html.parser')
    return soup

# Obtaining Players Names
def gettingPlayersNames(urlSoup):
    players_lst = []
    Players = urlSoup.find_all("a", {'class' : 'spielprofil_tooltip'})
    for player in Players:
        players_lst.append(player.text)
    return players_lst[:25]

# Obtaining Players Positions
def gettingPlayersPositions(urlSoup):
    positions_lst = []
    count=0
    positions = urlSoup.find_all('td')

    nums = [3]
    for i in range(40):
        nums.append(nums[-1]+6)
    for pos in positions:
        if str(pos.find('table'))!='None':
            x = (pos.find('table').find_all('td'))

            for e in x:
                count+=1
                if count in nums:
                    positions_lst.append(e.text)
    return positions_lst[:25]

# Obtaining players prices
def gettingPlayersValue(urlSoup):
    values_lst = []
    Values = urlSoup.find_all("td", {"class": "rechts hauptlink"})
    for val in Values:
        values_lst.append(val.text)
    return values_lst
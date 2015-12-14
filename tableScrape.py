import requests
from bs4 import BeautifulSoup
import pandas

r = requests.get("http://www.premiershiprugby.com/matchcentre/tables/index.php#TpJkmKwpAh0ESUHA.97")

# print(r.content)

soup = BeautifulSoup(r.content, "lxml")

#print([soup.prettify], "lxml")

#print(soup.find_all("td"))

# for link in soup.find_all("td"):
#     classList = link.get("class")
#     print(classList)

# for link in soup.find_all("td"):
#     classList = link.text
#     print(classList)

# for link in soup.find_all("td"):
#     #classList = link.text, link.get("field_TeamDisplay")
#     classList = link.text, link.get("field_Win")
#     print(classList)

# teamNames = soup.find_all("td", {"class":"field_TeamDisplay"})
#
# for team in teamNames:
#     print(team.text)

leagueTable = soup.find_all("tr", {"class":["champion", "playoffs", "normal"]})

#print(leagueTable)

for item in leagueTable:
    #print(item.contents[0].find_all("td", {"class": "src"}))
    # print(item.contents[0]).find_all("td")
    # Team Name
    print(item.contents[3].text)
    # Games Played
    print(item.contents[5].text)
    # Wins
    print(item.contents[6].text)
    # Draw
    print(item.contents[7].text)

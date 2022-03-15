import random, json, requests

url = "https://raw.githubusercontent.com/dr5hn/countries-states-cities-database/master/countries.json"

resp = requests.get(url)
data = json.loads(resp.text)

paises=[]
for obj in data:
    if obj["subregion"] == "South America":
        paises.append(obj["translations"]["es"].lower())


def pais():
  return random.choice(paises)
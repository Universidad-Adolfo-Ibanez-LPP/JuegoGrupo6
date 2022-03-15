import random, json, requests

url = "https://raw.githubusercontent.com/dr5hn/countries-states-cities-database/master/countries.json"

resp = requests.get(url)
data = json.loads(resp.text)

paises=[]
for obj in data:
    if obj["subregion"] == "South America":
        paises.append(obj["translations"]["es"].lower())

paises.remove("islas malvinas")
paises.remove("guayana francesa")
paises.remove("islas georgias del sur y sandwich del sur") #los borramos porque el espacio da problemas

def pais():
  return random.choice(paises)

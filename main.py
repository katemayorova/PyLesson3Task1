import requests


def find_hero(hero_name):
    response = requests.get(f"https://superheroapi.com/api/2619421814940190/search/{hero_name}").json()
    return response


names = ["Hulk", "Captain America", "Thanos"]
responses = []
for name in names:
    responses.append(find_hero(name)["results"][0])
responses.sort(reverse=True, key=lambda key: int(key["powerstats"]["intelligence"]))
print(f"Самый умный суергерой - {responses[0]['name']}")




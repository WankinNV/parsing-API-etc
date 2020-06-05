import requests
import json
from pprint import pprint

# 1ое задание
user = "WankinNV"
link = f"http://api.github.com/users/{user}"
response = requests.get(link)
data = response.json()
print(f"У пользователя {user} имеется {data['public_repos']} репозиториев")

# можно посмотреть более подробную информацию по репозиториям
# another_link = f"http://api.github.com/users/{user}/repos"
# another_response = requests.get(another_link)
# another_data = another_response.json()
# pprint(another_data)

# 2ое задание
key = "cObYTvxQOFOz3FDb4rOlisW5qNLH7oBQViuvdc9F"
sol = "1200"
example = f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol={sol}&api_key={key}"
response_from_nasa = requests.get(example)
data_from_nasa = response_from_nasa.json()
martian_sand = data_from_nasa["photos"][120]["img_src"]
print(martian_sand)

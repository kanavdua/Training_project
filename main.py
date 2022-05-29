import requests
import json
mykey = "a5bb37543aa9459eb6d1a1654c716c6e"

city = input("Enter country:")
city2 = city[0:2]
dict = {
    1:"Business",
    2:"Health",
    3:"Trending",
    4:"Entertainment",
    5:"Sports",
    6:"Technology"
}

list_of_categories = list(dict.values())
print("News categories are:")
for values in list_of_categories:
    print(values)
print()

category = input("Which category news you wish to see?")
result = category.split(" ")

for categories in list_of_categories:
    if categories in result:
        url = "https://newsapi.org/v2/top-headlines?country={}&category={}&apiKey={}".format( city2,categories, mykey)
        break
    else:
        url = "https://newsapi.org/v2/top-headlines?country={}&apiKey={}".format(city2, mykey)

print(url)

response = requests.get(url)

data = json.loads(response.text)   # converts the string into dictionary so we can extract relevant data
print("Total Results:",data["totalResults"])
data_articles= data['articles']

for articles in data_articles:
    print(articles["author"])
    print(articles["title"])
    print(articles["description"])
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
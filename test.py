import requests

BASE = "http://127.0.0.1:5000/"

data = [
        {"country": "SGP", "brand": "Brand B", "type": "Curry Ramen", "package": "Cup", "rating": 2.3},
        {"country": "MYS", "brand": "Brand C", "type": "Pork Ramen", "package": "Pack", "rating": 3.3},
        {"country": "USA", "brand": "Brand C"}
      ]

# Create ramen review with its data in dictionary form
# E.g adding 3 ramen reviews to the database with the first id continuing from 2602 
# start = 2602
# for i in range(len(data)):
#  response = requests.put(BASE + "ramen/" + str(start + i), data[i])
#  print(response.json())

# Modify ramen by id with its new data in dict form
# E.g Update the brand of ramen with id 2604 to "Brand A"
# response = requests.patch(BASE + "ramen/2604", {"brand": "Brand A"})
# print(response.json())

# DELETE ramen review by id
# E.g Delete the ramen review with id 2603
# response = requests.delete(BASE + "ramen/2603")
# print(response)

# GET ramen reviews by country
# E.g Get the list of ramen reviews with country "SGP"
# response = requests.get(BASE + "ramens?country=SGP&search=")
# print(response.json())

# GET ramen reviews by partial text
# E.g Get the list of ramen reviews with text "Seaweed" in any column data (case insensitive)
# response = requests.get(BASE + "ramens?country=&search=seaweed")
# print(response.json())






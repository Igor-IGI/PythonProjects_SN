import random


countries_cities = {"Austria": "Vienna", "Croatia": "Zagreb", "Spain": "Madrid", "Slovenia": "Ljubljana"}

random_country = random.choice(list(countries_cities))


capital_city = input(f"What is the capital city of: {random_country}: ")

while True:
    if capital_city == countries_cities[random_country]:
        print("Congratulation!")
        break
    else:
        capital_city = input("Maybe you need try again: ")




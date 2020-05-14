import random


def random_city():
    countries_cities = {"Austria": "Vienna", "Croatia": "Zagreb", "Spain": "Madrid", "Slovenia": "Ljubljana"}
    random_country = random.choice(list(countries_cities))
    city = countries_cities[random_country]
    return random_country, city


def play_the_game():
    random_country, _ = random_city()
    _, city = random_city()
    print(city)

    capital_city = input(f"What is the capital city of: {random_country}: ")

    while True:
        if capital_city == city:
            print("Congratulation!")
            break
        else:
            capital_city = input("Maybe you need try again: ")


play_the_game()

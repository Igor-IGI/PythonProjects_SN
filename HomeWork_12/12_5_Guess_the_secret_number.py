import datetime
import random
import json


# function to get 3 top scores
def get_top_scores():
    score_list = get_score_list()

    score_list = sorted(score_list, key=lambda k: k["attempts"])[:3]
    return score_list


# function to get score list
def get_score_list():
    with open("score_list.txt", "r") as score_list_file:
        score_list = json.loads(score_list_file.read())
        return score_list


# function for playing game
def play_game():
    secret = random.randint(1, 30)
    min_secret = 1
    max_secret = 30
    attempts = 0
    wrong_guesses = []

    score_list = get_score_list()

    player = input("What is your name: ")

    while True:
        attempts += 1
        guess = int(input(f"Guess the secret number between {min_secret} and {max_secret}: "))

        if guess == secret:
            print(f"You guessed it - congratulation! It is number {secret}.")
            print("Attempts needed: " + str(attempts))

            current_time = datetime.datetime.now()

            score = {
                "attempts": attempts,
                "time": str(current_time),
                "player name": player,
                "wrong guesses": wrong_guesses,
                "secret number": secret
            }
            score_list.append(score)

            with open("score_list.txt", "w") as score_list_file:
                score_list_file.write(json.dumps(score_list))

            break

        if guess > secret:
            print("Sorry your guess is not correct... try something smaller")

            wrong_guesses.append(guess)

            continue

        print("Sorry your guess is not correct... try something bigger")

        wrong_guesses.append(guess)


while True:
    selection = input("What would you like A) play a game, B) see the best score, C) quit ")

    if selection.lower() == "a":
        play_game()

    elif selection.lower() == "b":
        get_top_scores()

        for list_of_scores in get_top_scores():
            attempts_of_game = list_of_scores["attempts"]
            time_of_game = list_of_scores["time"]
            player_of_game = list_of_scores["player name"]
            wrong_guesses_of_game = list_of_scores["wrong guesses"]
            secret_num_of_game = list_of_scores["secret number"]

            print(f"Player name: {player_of_game}; "
                  f"Attempts: {attempts_of_game}; "
                  f"Time: {time_of_game}; "
                  f"Wrong guesses: {wrong_guesses_of_game}; "
                  f"The secret number was: {secret_num_of_game}")

    elif selection.lower() == "c":
        break

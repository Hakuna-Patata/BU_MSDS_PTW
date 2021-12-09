# Program: API Integration into Python
# Purpose: This program connects to
# Developer: Patrick Weatherford
# Week 2 - Assignment 9.1
# DSC 510 T301 - Intro to Programming
# Bellevue University - Professor Michael Eller

import requests

nl = '\n'
tab = '\t'
dash = '-'


def get_json_response(url):
    response = requests.request("GET", url).json()
    return response


def get_joke(url):
    response_data = get_json_response(url)
    joke = ''
    while True:
        try:
            joke = response_data['value']
        except KeyError:
            no_joke_try = input(f"Chuck Norris Code 404: No Joke Found. Try again? (Y/N): ")
            if no_joke_try.upper() == 'Y':
                continue
            elif no_joke_try.upper() == 'N':
                joke = "Chuck Norris would be sad to see you go but lacks the emotion of sadness."
                break
            else:
                while no_joke_try.upper() not in ['Y', 'N']:
                    no_joke_try = input(f"You dunce! Wrong input! Do you want to try to get another Chuck Norris Joke? (Y/N): ")
        else:
            joke = response_data['value']
            break
    return nl+"Joke: "+joke+nl


def main():
    url = 'https://api.chucknorris.io/jokes/random'
    print(f"{98*dash}{nl}Hello and thanks for using the Chuck Norris joke generator! Let's get you started off with a joke.{nl}{98*dash}")
    print(f'{get_joke(url)}')
    while True:
        get_another = input(f'Hahahaha! ROFL! Want to get another Chuck Norris joke? (Y/N): ')
        while get_another.upper() not in ['Y', 'N']:
            get_another = input("You dunce! Wrong input! Do you want to try to get another Chuck Norris Joke? (Y/N):")
        if get_another.upper() == 'Y':
            print(get_joke(url))
            continue
        else:
            print("Chuck Norris would be sad to see you go but lacks the emotion of sadness.")
            break


if __name__ == '__main__':
    main()

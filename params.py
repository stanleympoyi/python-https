from email import header
from nis import cat
import requests
import random
import pyfiglet
from termcolor import colored


header = pyfiglet.figlet_format("DAD JOKES")
color_header = colored(header, color='blue')
print(color_header)


def get_joke():
    search_term = input('Let me tell you a joke! Give me a topic: ')
    url = "https://icanhazdadjoke.com/search"
    response = requests.get(
        url,
        headers={"Accept": "application/json"},
        params={"term": f"{search_term}"}
    )
    data = response.json()
    num = 0
    for i in data['results']:
        num += 1
    if num == 1:
        print(
            f"I've got one joke about {search_term}. Here it is: \n {data['results'][0]['joke']}")
    elif num < 1:
        print(
            f"Sorry, I don't have any jokes about {search_term}! Please try again.")
    else:
        rand_joke = random.randint(0, int(f'{num}'))
        print(f" I've got {num} jokes about {search_term}. Here's one: \n",
              data['results'][rand_joke]['joke'])


get_joke()

import requests


def joke_fun(num=5):
    '''
    function will print jokes in a python dictionary with numbers as
     keys and jokes as values. The function as a default parameter of 5
    '''
    jokes = {}
    for i in range(1, num + 1):
        if i <= num:
            url = "https://icanhazdadjoke.com/"
            response = requests.get(
                url, headers={"Accept": "application/json"})
            data = response.json()
            jokes[f'{i}'] = data["joke"]
    print(jokes)


joke_fun(10)

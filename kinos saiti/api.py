import requests
import json

class Film:
    api_key = "b39ede14"

    def __init__(self, film):
        self.film = film

    def request(self):
        # მეთოდი request-ის გასაკეთებლად.
        url = f"http://www.omdbapi.com/?apikey={Film.api_key}&t={self.film}&plot=full"
        r = requests.get(url)
        return r

    @property
    def response(self):
        # აბრუნებს JSON მონაცემებს რექუესთის შემდგომ.
        data = self.request().json()
        return data

    @property
    def rating(self):
        # აბრუნებს ფილმის IMDB რეიტინგს. თუ ფილმს არ აქვს რეიტინგი, მაშინ დააბრუნებს "N/A"-ს.
        rating = self.response["imdbRating"]
        return rating

    @property
    def title(self):
        # JSON მონაცემებიდან გამოაქვს მხოლოდ ფილმის დასახელება იმ შემთხვევაში, თუ ეს ფილმი არსებობს.
        title = self.response["Title"]
        return title

    @property
    def genres(self):
        genres = self.response["Genre"]
        return genres

    @property
    def poster(self):
        poster = self.response["Poster"]
        return poster

    def plot(self):
        try:
            plot = self.response["Plot"]
            return plot
        except KeyError:
            print("The summary of the plot is not in the provided data.")
from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
response.encoding = "utf-8"
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")

link_text = soup.find_all(name="h3", class_="title")
movie_list = []
for text in link_text:
    movie_list.append(text.getText())
movie_list.reverse()


for movie in movie_list:
    try:
        with open("movies.text", "a") as file:
            file.write(movie + '\n')
    except FileNotFoundError:
        with open("movies.txt", "w") as file:
            file.write(movie + '\n')











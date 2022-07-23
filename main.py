from bs4 import BeautifulSoup
import requests


response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
eo_web_page = response.text

soup = BeautifulSoup(eo_web_page, "html.parser")
soup.encode("utf-8")
titles = [title.getText() for title in soup.find_all(name="h3", class_="title")]
titles.reverse()

with open("movies.txt", mode="w", encoding="utf-8") as file:
    for i in titles:
        print(i)
        file.write(f"{i}\n")

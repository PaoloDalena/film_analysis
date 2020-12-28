from urllib.request import urlopen
from bs4 import BeautifulSoup
import sys


def scrape_film_info(imdb_url):
    html = urlopen(imdb_url)
    film = BeautifulSoup(html, "html.parser")

    title = film.find("div", {"class": "title_wrapper"})
    title = title.find("h1").get_text()

    rating = film.find("div", {"class": "ratingValue"}).get_text()
    rating = int(rating[1])*10 + int(rating[3])

    genres = film.find("div", {"class": "subtext"})
    genre1 = genres.findAll("a")[0].get_text().lower()

    try:
        genre2 = genres.findAll("a")[1].get_text().lower()
    except Exception:
        pass

    year = film.find("span", {"id": "titleYear"}).get_text().replace("(", "").replace(")", "")

    director = film.find("div", {"class": "credit_summary_item"})
    director = director.find("a").get_text()

    country = film.find("h4", {"class", "inline"}, text="Country:")
    country = country.find_parent("div").get_text()
    country = country.split()[1]

    try:
        budget = film.find("span", {"class", "attribute"}, text="(estimated)")
        budget = budget.find_parent("div")
        budget = budget.get_text().replace("$", " ").replace(",", "").replace("GBP", " ").replace("EUR", " ")
        budget = [int(s) for s in budget.split() if s.isdigit()]
        budget = int(budget[0]) // 1000000

        boxoffice = film.find("h4", {"class", "inline"}, text="Cumulative Worldwide Gross:")
        boxoffice = boxoffice.find_parent("div")
        boxoffice = boxoffice.get_text().replace("$", " ").replace(",", "")
        boxoffice = [int(s) for s in boxoffice.split() if s.isdigit()]
        boxoffice = int(boxoffice[0]) // 1000000
    except Exception:
        pass

    print("TITLE -> ", title)

    infos = (director, year, country, rating, genre1, genre2, budget, boxoffice)
    labels = ("director", "year", "country", "rating", "genre1", "genre2", "budget", "boxoffice")

    for info in infos:
        try:
            print(labels[infos.index(info)], ": ", info)
        except Exception:
            pass

    print("")


films_1 = [
    "https://www.imdb.com/title/tt0119217/",  # willhunting
    "https://www.imdb.com/title/tt0118715",   # bigleb
    "https://www.imdb.com/title/tt0993846/",  # wolfofwallstreet
    "https://www.imdb.com/title/tt1219289/",  # limitless
    "https://www.imdb.com/title/tt7349662/",  # blackkk
    "https://www.imdb.com/title/tt0268978/",  # beautifulmind
    "https://www.imdb.com/title/tt2465578/",  # capitaleumano
    "https://www.imdb.com/title/tt0180093/",  # requiemforadream
    "https://www.imdb.com/title/tt5027774/",  # 3billboards
    "https://www.imdb.com/title/tt0117951/",  # trainspotting
    "https://www.imdb.com/title/tt0434409/",  # VforV
    "https://www.imdb.com/title/tt0120601/",  # beingjm
    "https://www.imdb.com/title/tt2278388/",  # grandbudapest
    "https://www.imdb.com/title/tt1068680/",  # yesman
    "https://www.imdb.com/title/tt1670345/",  # nowyouseeme
    "https://www.imdb.com/title/tt0133093/",  # matrix
    "https://www.imdb.com/title/tt0427152/",  # dinnerfor
    "https://www.imdb.com/title/tt1675434/",  # intouchables
    "https://www.imdb.com/title/tt0118799/",  # lavitaebella
    "https://www.imdb.com/title/tt0119654/",  # meninblack
]

# films from willhunting to meninblack

sys.stdout = open("scraping_output_1.txt", "w")

for i in films_1:
    scrape_film_info(i)

sys.stdout.close()

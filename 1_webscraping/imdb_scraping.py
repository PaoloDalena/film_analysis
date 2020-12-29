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

    if len(genre2.split()) > 2:
        genre2 = genre1

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

# films from willhunting to meninblack:

sys.stdout = open("scraping_output_1.txt", "w")

for i in films_1:
    scrape_film_info(i)

sys.stdout.close()

films_2 = [
    "https://www.imdb.com/title/tt2911666/",  # johnwick
    "https://www.imdb.com/title/tt1131729/",  # boatrock
    "https://www.imdb.com/title/tt2096673/",  # insideout
    "https://www.imdb.com/title/tt0478087/",  # 21
    "https://www.imdb.com/title/tt0480249/",  # iamlegend
    "https://www.imdb.com/title/tt1596363/",  # thebigshort
    "https://www.imdb.com/title/tt0322802/",  # jackass
    "https://www.imdb.com/title/tt1637725/",  # ted
    "https://www.imdb.com/title/tt0330373/",  # harrypotter
    "https://www.imdb.com/title/tt1645170/",  # thedictator
    "https://www.imdb.com/title/tt0435705/",  # next
    "https://www.imdb.com/title/tt0389860/",  # click
    "https://www.imdb.com/title/tt0421715/",  # benjaminbutton
    "https://www.imdb.com/title/tt0368891/",  # nationaltreasure
    "https://www.imdb.com/title/tt0396171/",  # perfume
    "https://www.imdb.com/title/tt7286456/",  # joker
    "https://www.imdb.com/title/tt0454848/",  # insideman
    "https://www.imdb.com/title/tt4682786/",  # collateralb
    "https://www.imdb.com/title/tt0386588/",  # hitch
    "https://www.imdb.com/title/tt0485947/",  # mrnobody
    "https://www.imdb.com/title/tt1010048/",  # themill
    "https://www.imdb.com/title/tt0359950/",  # waltermitty
    "https://www.imdb.com/title/tt0119282/",  # hercules
    "https://www.imdb.com/title/tt3890160/",  # baby driver
    "https://www.imdb.com/title/tt0351283/"   # madagascar
]

# films from johnwick to madagascar:

sys.stdout = open("scraping_output_2.txt", "w")

for i in films_2:
    scrape_film_info(i)

sys.stdout.close()

films_3 = [
    "https://www.imdb.com/title/tt0416320/",  # matchpoint
    "https://www.imdb.com/title/tt2179136/",  # americansniper
    "https://www.imdb.com/title/tt0245429/",  # spiritedaway
    "https://www.imdb.com/title/tt2381941/",  # focus
    "https://www.imdb.com/title/tt0416449/",  # 300
    "https://www.imdb.com/title/tt1119646/",  # hangover
    "https://www.imdb.com/title/tt0145487/",  # spiderman
    "https://www.imdb.com/title/tt0808279/",  # funnygames
    "https://www.imdb.com/title/tt0335266/",  # lostintransl
    "https://www.imdb.com/title/tt1156398/",  # zombieland
    "https://www.imdb.com/title/tt0499549/",  # avatar
    "https://www.imdb.com/title/tt0371746/",  # ironman
    "https://www.imdb.com/title/tt0306047/",  # scarymovie
    "https://www.imdb.com/title/tt0169547/",  # americanbeauty
    "https://www.imdb.com/title/tt7131622/",  # onceupon
    "https://www.imdb.com/title/tt1386697/",  # suicidesquad
    "https://www.imdb.com/title/tt0120663/",  # eyeswideshut
    "https://www.imdb.com/title/tt8579674/",  # 1917
    "https://www.imdb.com/title/tt1099212/",  # twilight
    "https://www.imdb.com/title/tt1700841/",  # sausageparty
    "https://www.imdb.com/title/tt2562232/"   # birdman
]

# films from matchpoint to birdman:

sys.stdout = open("scraping_output_3.txt", "w")

for i in films_3:
    scrape_film_info(i)

sys.stdout.close()

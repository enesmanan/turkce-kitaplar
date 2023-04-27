import csv
import requests
from bs4 import BeautifulSoup

# Top 250 filmi cek
def scrape_top_250_movies():
    url = 'https://www.imdb.com/chart/top/'
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html, 'html.parser') # parse islemi

    movies = []
    for idx, tr in enumerate(soup.select('.lister-list tr')):
        title = tr.find('td', {'class': 'titleColumn'}).find('a').text
        year = tr.find('td', {'class': 'titleColumn'}).find('span').text.strip('()')
        rating = tr.find('td', {'class': 'ratingColumn imdbRating'}).find('strong').text

        movie = {'Index': idx + 1, 'Title': title, 'Year': year, 'Rating': rating}
        movies.append(movie)

    return movies

# CSV dosyasina yaz
def write_to_csv(movies):
    with open('top_250_movies.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Index', 'Title', 'Year', 'Rating']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for movie in movies:
            writer.writerow(movie)


if __name__ == '__main__':
    movies = scrape_top_250_movies()
    write_to_csv(movies)
    print('Veriler cekildi!')
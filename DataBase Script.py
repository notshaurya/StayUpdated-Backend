import gspread
import requests
import time
from threading import Timer

topHeadlinesURL = 'https://newsapi.org/v2/top-headlines?country=in&pageSize=100&apiKey=3d0174f321ba406daf5daa0f48d5c724'
businessURL = 'https://newsapi.org/v2/top-headlines?country=in&pageSize=100&category=business&apiKey=3d0174f321ba406daf5daa0f48d5c724'
entertainmentURL = 'https://newsapi.org/v2/top-headlines?country=in&pageSize=100&category=entertainment&apiKey=3d0174f321ba406daf5daa0f48d5c724'
healthURL = 'https://newsapi.org/v2/top-headlines?country=in&pageSize=100&category=health&apiKey=3d0174f321ba406daf5daa0f48d5c724'
scienceURL = 'https://newsapi.org/v2/top-headlines?country=in&pageSize=100&category=science&apiKey=3d0174f321ba406daf5daa0f48d5c724'
sportsURL = 'https://newsapi.org/v2/top-headlines?country=in&pageSize=100&category=sports&apiKey=3d0174f321ba406daf5daa0f48d5c724'
technologyURL = 'https://newsapi.org/v2/top-headlines?country=in&pageSize=100&category=technology&apiKey=3d0174f321ba406daf5daa0f48d5c724'


def dataInput(sheetName, url):
    gc = gspread.service_account(filename='credentials.json')
    sh = gc.open_by_key('1cJrwFP4VQ6DdQqsfntauj_DqspVGtxYu-iVLx8OYw6s')
    db = sh.worksheet(sheetName)
    topHeadlines = requests.get(url).json()
    final = []
    header = ['title', 'description', 'author',
              'urlToImage', 'url', 'publishedAt']
    final.append(header)
    for item in topHeadlines['articles']:
        tl = []
        tl.append(item['title'])
        tl.append(item['description'])
        tl.append(item['source']['name'])
        tl.append(item['urlToImage'])
        tl.append(item['url'])
        tl.append(item['publishedAt'])
        final.append(tl)
    db.clear()
    db.append_rows(final)


def mainCall():
    dataInput('topHeadlines', topHeadlinesURL)
    dataInput('business', businessURL)
    dataInput('entertainment', entertainmentURL)
    dataInput('health', healthURL)
    dataInput('science', scienceURL)
    dataInput('sports', sportsURL)
    dataInput('technology', technologyURL)

for x in range(72):
    mainCall()
    time.sleep(1260)

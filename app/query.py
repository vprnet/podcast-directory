#!/usr/bin/python
from sheet import get_google_sheet
from slugify import slugify
import requests
from BeautifulSoup import BeautifulSoup

def get_podcasts():
    sheet = get_google_sheet()
    podcast_list = []

    for i, podcast in enumerate(sheet):
        if podcast['Category']:
            podcast['slug'] = slugify(podcast['Name'])
            podcast_list.append(podcast)

        if podcast['RSS']:
            feed_url = podcast['RSS']
            response = requests.get(feed_url)
            html = response.content
            soup = BeautifulSoup(html)

            podcast['recent_one'] = soup.enclosure['url']
            podcast['title_one'] = soup.item.title.string

    return podcast_list

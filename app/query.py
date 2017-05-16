#!/usr/bin/python
from sheet import get_google_sheet, get_staff_sheet
from slugify import slugify
from BeautifulSoup import BeautifulSoup
import requests
import re
import datetime

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

            all_enclosure_urls = soup.findAll(re.compile('^enclosure'))
            recent_episodes = [tag['url'] for tag in all_enclosure_urls]

            recent_titles = soup.findAll('title')

            if podcast['Featured_VPR'] == "Yes":
                podcast['Teaser'] = soup.find('itunes:subtitle').string

            try:
                podcast['recent_zero'] = recent_episodes[0]
                podcast['title_zero'] = recent_titles[2].string

                podcast['recent_one'] = recent_episodes[1]
                podcast['title_one'] = recent_titles[3].string

                podcast['recent_two'] = recent_episodes[2]
                podcast['title_two'] = recent_titles[4].string

            except IndexError:
                podcast['recent_zero'] = False
                podcast['recent_one'] = False
                podcast['recent_two'] = False
                podcast['title_zero'] = False
                podcast['title_one'] = False
                podcast['title_two'] = False

    return podcast_list

def get_staff_picks():
    sheet = get_staff_sheet()
    staff_podcasts = []

    for i, pick in enumerate(sheet):
        if pick['Episode']:
            staff_podcasts.append(pick)

    return staff_podcasts

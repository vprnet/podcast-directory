#!/usr/bin/python
from sheet import get_google_sheet
from slugify import slugify

def get_podcasts():
    sheet = get_google_sheet()
    podcast_list = []

    for i, podcast in enumerate(sheet):
        if podcast['Category']:
            podcast['slug'] = slugify(podcast['Name'])
            podcast_list.append(podcast)

    return podcast_list

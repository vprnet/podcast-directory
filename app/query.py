#!/usr/bin/python
from sheet import get_google_sheet
from slugify import slugify

def get_podcasts():
    sheet = get_google_sheet()
    podcast_list = []

    for i, podcast in enumerate(sheet):
        if podcast['Category']:
            podcast['Slug'] = slugify(podcast['Name'])
            podcast_list.insert(0, podcast)
        else:
            podcast_list.append(podcast)

    return podcast_list

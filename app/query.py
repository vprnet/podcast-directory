#!/usr/bin/python
from sheet import get_google_sheet
from slugify import slugify

def get_podcasts():
    sheet = get_google_sheet()
    podcast_list = []

    for i, podcast in enumerate(sheet):
        podcast_list.append(podcast)

    return podcast_list

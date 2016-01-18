from index import app
from flask import render_template, request
from query import get_podcasts, get_staff_picks
from config import BASE_URL

staff_picks = get_staff_picks()
podcasts = get_podcasts()

project_social = {
    'url': BASE_URL,
    'title': "VPR's Podcast Directory",
    'subtitle': "",
    'img': "http://mediad.publicbroadcasting.net/p/vpr/files/vpr-podcast-directory-2015.png",
    'description': "VPR's Podcast Directory",
    'twitter_text': "I'm using VPR's Podcast Directory.",
    'twitter_hashtag': ""
}


@app.route('/')
def index():
    page_url = BASE_URL + request.path
    page_title = "VPR's Podcast Directory"
    landing = True

    social = project_social

    return render_template('content.html',
        page_title=page_title,
        social=social,
        podcasts=podcasts,
        staff_picks=staff_picks,
        landing=landing,
        project_social=project_social,
        page_url=page_url)


@app.route('/<Name>')
def podcast_page(Name):
    for podcast in podcasts:
        if 'slug' in podcast and Name == podcast['slug']:
            podcasts.remove(podcast)
            podcasts.insert(0, podcast)

    page_url = BASE_URL + request.path
    page_title = 'Podcast Directory: ' + podcasts[0]['Name']

    social = {
        'title': page_title,
        'subtitle': "VPR's Podcast Directory",
        'img': podcasts[0]['Image'],
        'description': "From VPR's Podcast Directory",
        'twitter_text': podcasts[0]['Name'],
        'twitter_hashtag': ""
    }

    return render_template('content.html',
        page_title=page_title,
        social=social,
        podcasts=podcasts,
        staff_picks=staff_picks,
        project_social=project_social,
        page_url=page_url)

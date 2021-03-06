# VPR's Podcast Directory

This is iteration one of VPR's podcast directory. We're thinking about this project as both a resource and a discovery tool. We know there are tons of podcasts Vermonters enjoy. We want to showcase them and share them.


## Get Involved

We also want your help. If you're a Vermonter and you host a podcast, get in touch. If you're a Vermonter and you have a favorite local podcast, get in touch. If you're a developer and you think you can do this much better than we can, pull request accepted. This is public media, folks.


## Notes on the Project

This project started with VPR's [Live From the Fort](http://www.vpr.net/apps/live-from-the-fort/) as a template. Vermonters love to recycle.


## Notes on Rumble Strip

As you can see in `templates/_all_podcasts.html`, `templates/_podcast_spotlight.html`, and `templates/_podcast_view.html`, the Rumble Strip podcast works a bit differently than the others listed in the directory. This is because once a month, VPR airs an old episode of Rumble Strip and we've wanted the directory to feature that episode, so we don't want it to just pull and highlight the three most recent episodes from the RSS feed.

That all said, the code is set up so that everything's automated from the Google Spreadsheet. When Franny sends a ticket with a new Rumble Strip episode, all that needs to happen is an update to the spreadsheet. The code will run on the cron and update automatically.


## One-time set-up work:

1. Make sure you have Python 2.7 installed.
1. Clone the repo locally. `git clone git@github.com:vprnet/podcast-directory.git`
1. [Install `pip`](https://pip.pypa.io/en/latest/installing.html)
1. Install virtualenv. `pip install virtualenv`
1. Create a virtual environment for the app. `virtualenv venv`
1. Install the app requirements. `pip install -r requirements.txt`
1. Duplicate `_config.py` as `config.py`, which will be your private, git-ignored file of keys.
1. Grab the secret `podcast-access.json` file from someone on the VPR team.


## Regular Updates, start here:

1. Change into the project directory. `cd podcast-directory`
1. Enter the virtual environment. `source venv/bin/activate`
1. To run locally, just hit a quick	`python app/index.py` and head to `127.0.0.1:5000`


## Pushing to production:

This project runs on a cron job in Webfaction. The cron is currently set to run three times a day, pushing up to Amazon S3. To update the production code, SSH into our Webfaction server and update changes to the production code.


## Notes on Interacting with Google Spreadsheets

The project is hooked up to a Google Spreadsheet that VPR producers and editors can populate. If you're interested in cloning this project, you'll need your own Google Spreadsheet to get started.

We use [gspread](https://github.com/burnash/gspread) with the Drive API to connect our spreadsheet to the app. Here are a few things to know about the implementation:

1. To start a new project, head to the [Google Developer's Console](https://console.developers.google.com/project).
1. Click `create a project`. Give it a name.
1. Click `Enable and manage APIs`.
1. Under `Google Apps APIs` click `Drive API` and `Enable`.
1. Click `Go to Credentials`.
1. `Create Credentials`.
1. `Create service account key`, and select `New service account`. Give it a name.
1. When you `create`, you'll see a JSON file incoming. Save that file to your project directory. Add it to your gitignore if your code is going anywhere public.
1. The json file is what gets loaded and opened in `sheet.py`. Make sure the names match!
1. Create a Google Spreadsheet through your Google Drive. Make sure your spreadsheet title is exactly what's trying to be opened in `sheet.py`'s `authorization.open("")` line. To match our project, you'll need two worksheets within the same spreadsheet: `Podcasts` and `Staff Picks`. In the first, we've named our columns: `Name`, `Category`, `Spotlight`, `Image`, `Link`, `Audio`, `Feature`, `RSS`, `iTunes`, `Other`, and `Description`. In the second, we have: `Recommender`, `Title`, `Twitter`, `Episode`, `Podcast`, `Link`, `Description`, and `Image`. We split these up into two separate worksheets in order to keep a clear history of VPR Staff Pick Podcasts.
1. You may need to *share your Google Spreadsheet* with the email provided in `client_email`.

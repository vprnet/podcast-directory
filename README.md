#VPR's Podcast Directory

This is iteration zero of VPR's podcast directory. We're thinking about this project as both a resource and a discovery tool. We know there are tons of podcasts Vermonters enjoy. We want to showcase them and share them.

##Get Involved

We also want your help. If you're a Vermonter and you host a podcast, get in touch. If you're a Vermonter and you have a favorite local podcast, get in touch. If you're a developer and you think you can do this much better than I can, pull request accepted. This is public media, folks.

My name is Sara, and I'm in charge of all things code on this project. Chances are that if you're finding out about it through the GitHub repo, I'm the person you'll want to get in touch with.

So, reach out! I'm at [@sarambsimon](http://twitter.com/sarambsimon).  

##Notes on the project

This project started with VPR's [Live From the Fort](http://www.vpr.net/apps/live-from-the-fort/) as a template. Vermonters love to recycle.

The steps to get set up are here:

1. Make sure you have Python 2.7 installed.
1. Clone the repo locally. `git clone git@github.com:vprnet/podcast-directory.git`
1. [Install `pip`](https://pip.pypa.io/en/latest/installing.html)
1. Install virtualenv. `pip install virtualenv`
1. Change into the project directory. `cd podcast-directory`
1. Create a virtual environment for the app. `virtualenv venv`
1. Enter the virtual environment. `source venv/bin/activate`
1. Install the app requirements. `pip install -r requirements.txt`
1. To run locally, just hit a quick	`python app/index.py` and head to `127.0.0.1:5000`, but know that it will all be broken until you follow the Google Spreadsheet steps below.

##Notes on Interacting with Google Spreadsheets

The project is hooked up to a Google Spreadsheet that VPR producers and editors can populate. If you're interested in cloning this project, you'll need your own Google Spreadsheet to get started.

We use [gspread](https://github.com/burnash/gspread) with the Drive API to connect our spreadsheet to the app. Here are a few things to know about the implementation:

1. To start a new project, head to the [Google Developer's Console](https://console.developers.google.com/project).
1. Click `create project`.
1. Under `APIs`, enable the Google Drive API.
1. In `Credentials` under `OAuth`, create a new Client ID.
1. Select `Service Account`. You'll see a json file incoming with a `private_key_id`, `private_key`, `client_email`, `client_id`, and `type`.
1. Save the json file in your project. Be a decent person and add it to your gitignore, too.
1. The json file is what gets loaded and opened in sheet.py. Make sure the names match!
1. Create a Google Spreadsheet through your Google Drive. Make sure your spreadsheet title is exactly what's trying to be opened in sheet.py's `authorization.open("")` line. To match our project, you'll need to call the columns of your spreadsheet `Name`, `Image`, `Link`, `Audio`, `RSS`, and `Description`. This might change, though, so keep an eye out for updates.
1. Finally, *share your Google Spreadsheet* with the email provided in `client_email`. This is important. Don't forget this.
1. If you have problems running the project locally, you'll likely need to need to `pip install gspread` and `pip install oauth2client` and maybe even `pip install pycrypto` just for kicks.


##Copyright and License

Copyright 2015 Vermont Public Radio

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this work except in compliance with the License.
You may obtain a copy of the License in the LICENSE file, or at:

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language
governing permissions under the License.

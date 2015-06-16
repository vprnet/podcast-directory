#Podcast Directory

This is iteration zero of VPR's podcast directory.

## Notes on Interacting with Google Spreadsheets

In May 2015, Google stopped supporting the Google Spreadsheets API, which Live From the Fort used to connect a spreadsheet to the page. We found a good replacement in [gspread](https://github.com/burnash/gspread). Here are a few things to know about our new implementation:

1. To start a new project, head to the [Google Developer's Console](https://console.developers.google.com/project).
1. Click `create project`.
1. Under `APIs`, enable the Google Drive API.
1. In `Credentials` under `OAuth`, create a new Client ID.
1. Select `Service Account`. You'll see a json file incoming with a private_key_id, private_key, client_email, client_id, and type.
1. Save the json file in your project. Be a good person and add it to your gitignore, too.
1. The json file is what gets loaded and opened in sheet.py. Make sure the names match!
1. Finally, *share your google spreadsheet* with the email provided in client_email.
1. You'll also need to `pip install gspread` and `pip install oauth2client`.


##Copyright and License

Copyright 2013 Vermont Public Radio

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this work except in compliance with the License.
You may obtain a copy of the License in the LICENSE file, or at:

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language
governing permissions under the License.

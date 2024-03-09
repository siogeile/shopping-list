# Command Line Shopping List App

    Insert image :  Screenshot of terminal

## Live Site

[Visit deployed app on Heroku](https://shopping-list-project-pp3-7520c0c885a6.herokuapp.com)

## Repository

[Visit repository on GitHub](https://github.com/siogeile/shopping-list)

<br 
/>

# Contents

[Markdown Content Generator](https://ecotrust-canada.github.io/markdown-toc/)

<br 
/>

# User Experience Design (UX)

## Project Purpose

Provide a simple way for the user to manage their shopping list that stores
data using a Command Line Interface developed using Python

### Developer's Goals

Develop an application using Python that functions as intended, passes through
a linter without significant issues and write code that handles empty or invalid
input data. The app should have consistent logic flow with standard programming
constructs implemented. The developer should identify and repair any coding
errors. The app should provide a solution to a real-world problem and should 
handle, store and manipulates user data. The development process should be
well documented through a version control system and the final version deployed 
to a cloud-based platform.

### External User's Goal

Manage items in a list for purchase at a later time.

#### First Time User

> *"I would like something that is quick to learn and straightforward"*

#### Returning User

> *"I tend to lose any handwritten lists that I write so I would like somethingthat saves my data where it can't be lost."*
>
> *"A shopping list helps me remember what I need, but sometimes I need help remembering what I need to remind myself about! A seperate list where items are stored after they have been cleared from the shopping list that I can look at for reminders would be helpful"*

## Program Flowchart

[lucid flowchart app](https://lucid.app/documents#/documents?folder_id=recent)

    Insert image :  Flowchart

## Constraints

The Code Institute deployment terminal is set to 80 columns by 24 rows. 
That means that each line of text needs to be 80 characters or less otherwise 
it will be wrapped onto a second line.

I added the following code to apply a ruler to mark the 80 character limit in
my code editor:

```
"editor.rulers": [
    80
]
```

<br 
/>

# Features

## Existing Features

### The Main Menu

### View Shopping List

### Add Item

* Collect user input
* Validate user data
* Update Google Sheets with user data

### Remove Item

* Collect user input
* Validate user request
* Remove appropriate values from Google Sheets

### Exit

### Repeat or Return and Clear Terminal

<br 
/>

## Future Features

* Add validation to ensure there is no empty space at the start of an entry
<i><b>or</b></i> a function that clears blank spaces that are entered as the
first character of an entry

* Store items removed from the shopping list in a new list for futre use

* Add more options:

    * Clear entire shopping list (move all items to items list)

    * View all items (on shopping list and items list)

    * Check if item is on the shopping list, items list or neither

    * Delete items
        * would function the same as remove currently does
        * remove would instead move items to the items list

* Add different user accounts functionality

* Allow users to create and name multiple lists

* I would add colours using a module such as [this](https://www.grepper.com/answers/356905/colored+text+python) to enhance readability and
user experience

<br 
/>

# Testing

## CI Python Linter

link to linter [here](https://pep8ci.herokuapp.com/)

Code passes with no errors

## Manual Testing

Does the app handle invalid inputs to effectively manage data, create
a positive user experience and ensure the app functions as expected?

Yes

Does the project have logic that flow without unexpected interuption or 
error messages?

Yes

Does the deployed app run as expected on the heroku app?

Yes

## Browser Compatibility

Browser        | App Version / OS     | Compatibility
---------------|----------------------|---------------
Chrome         | for windows          | ✅
|              | for MacOS            | ✅
Firefox        | for windows          | ✅
|              | for MacOS            | ✅
DuckDuckGo     | for windows          | ✅
|              | for MacOS            | ✅
Edge           | for Windows          | ✅
Safari         | for MacOS            | ❌

The Code Institute mock termincal does  <b>not</b> work on mobile devices or 
the Safari browser. I was unable to test the linux browser compatability but I believe there are no reported issues.

<br 
/>

# Technologies Used

## Data Storage

The data for the application is stored in google sheets which is available
to view [here](https://docs.google.com/spreadsheets/d/1Cx9JBL5leWkGEfrdIX3eBIJBtIoJtdgia2ubThSCp_Y/edit?usp=sharing).

The creds.json file retrieved from the Google Cloud API on Heroku is contains
a unique email for the Heroku project that is shared with the Google Sheets
workbook and stored in the repository root. These credentials are hidden to 
ensure data remains secure.

Sensitive data is not requested or stored.

## Other Tech

* [Heroku](https://dashboard.heroku.com/) for app deployment

*  [Git](https://git-scm.com/) for version control through the Gitpod
terminal to commit Git and Push to GitHub

* [GitHub ](https://github.com/) to store project code and version control

* [Gitpod](https://gitpod.io/) workspace for code editing

* [Diffchecker](https://www.diffchecker.com/) to compare code with previous 
versions for debuggings

* [Grammarly](https://www.grammarly.com/) for spell-checks and character counts

* [Google Sheets](https://www.google.com/sheets/) for data storage

* [Google Cloud Console](https://cloud.google.com/) for credential verification

* [Gemini](https://gemini.google.com/chat) and
[ChatGPT](https://chat.openai.com/) for troubleshooting

* LucidChart to generate flowcharts

* xyz for image optimisation

* PEP * to validate python code

### Python Packages

### GitPod/VS Code Extensions

<br 
/>

# Development and Deployment

This project is deployed using Code Institute's mock terminal for Heroku.

### Inital Development

1. Create a new project on the Google Cloud Platform
2. Add Google Drive API and create service account credentials
3. Download credentials json file
4. Add Google Sheets API
5. Create GitHub repository from Code Institute's Python
Essentials template
6. Create workspace on Gitpod from repo
7. Drag and drop json credentials file to workspace root, 
rename it creds.json
8. Create a new Google Sheets document
9. Copy the email from the creds.json file and share it with the google sheet, do not select "notify people"
10. Add creds.json to the .gitignorefile
11. Enter the following command into the terminal:

    `pip3 install gspread google-auth`

12. Place this code at the beginning of the run.py file:
``` 
import gspread
from google.oauth2.service_account import Credentials
# live deployments should not contain pprint, for testing only
from pprint import pprint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('workbook_name')
#access specific sheet
sheet_one = SHEET.worksheet('sheet_name')
```
### Deployment

1. Log in or register for a Heroku account
2. From the dashboard select "Create a new app"
3. Give your app a unique name and choose your region
4. Create app
5. When app is created, go to settings
6. Add the following two Config Vars:

    Key        | Value
    ---------- | -------------
    CREDS      | Paste creds.json content here
    PORT       | 8000

7. Add these two Buildpacks in this order:
    * Python
    * Nodejs

8. Click "Deploy" at the top of the page
9. Connect to relevant GitHub repository
10. Turn on Auto-deploys or just manually deploy
11. Click on "view" to go to the [deployed app](https://shopping-list-project-pp3-7520c0c885a6.herokuapp.com)

### Local Development

#### How to Fork

1. Log in (or sign up) to Github.
2. Go to the repository for this project, shopping-list.
3. Click the Fork button in the top right corner.

#### How to Clone

1. Log in (or sign up) to GitHub.
2. Go to the repository for this project, shopping-list.
3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
5. Type 'git clone' into the terminal and then paste the link you copied in step 3.
6. Press enter.

<br 
/>

# Credits

### Code Institite:

#### Love Sandwiches Code Along Project by the Code Institute

* Used code from the love-sandwiches walkthrough project closely up until
commits 390bc5d and 1963a99.
* Here I was still using code from that project but only relevant sections from
the project that I changed to work for my app

#### Python Essentials Template

* GitHub Repository [Template](https://github.com/Code-Institute-Org/python-essentials-template) for setting up the initial workspace

### Other Devs' Code

#### [Geek Tutorials](https://www.youtube.com/watch?v=0m7csmqWAgI) on YouTube

*  Used code from "Python - Code a Shopping List App (Part 1/3) to get me
started in commit f1d5751
* Started to write my own code within this code in commit eacf398 when adding
functions to menu items 1 and 2

* Deployment steps copied from adamsburge on GitHub's Command Line Budget
App [Repo](https://github.com/adamsburge/commandline-budgetapp)

### Resources, guidance and inspiration

* I created a functinon to clear the terminal after reading about ANSI VT100 
codes from [an answer on Quora.com](https://qr.ae/pshJBT)
```
def clear_screen():
    """
    Clears the screen using ANSI VT100 codes
    """
    print('\033[H\033[J')
    return
```

* Code Institute's Slack Workspace Channels

* Code Institute's Python Essentials Coureswork

* Command Line Budget [App](https://commandline-budgetapp.herokuapp.com/) on Heroku by [adamsburge](https://github.com/adamsburge/commandline-budgetapp) on GitHub

* I referred to a README [template](https://github.com/kera-cudmore/readme-examples/blob/main/milestone1-readme.md) developed by [kera-cudmore](https://github.com/kera-cudmore) for the general strucure of my README

* I referred to a [README](https://github.com/oks-erm/booking/blob/main/README.md) developed by [oks-erm](https://github.com/oks-erm) for a better understanding of a README for a python project

* I referred to a [README](https://github.com/BobWritesCode/ci-Project3/blob/main/README.md) developed by [BobWritesCode](https://github.com/BobWritesCode)

* I used the headings for my "User Stories" section from the README of another [project](https://github.com/kera-cudmore/Bully-Book-Club#bully-book-club-website) by [kera-cudmore](https://github.com/kera-cudmore).

* I referred to the Python 3 [documentation](https://docs.python.org/3/) and [Real Python](https://realpython.com/) for syntax and general Python knowledge

* I referred to the gspread [documentation](https://docs.gspread.org/en/latest/index.html) while writing code that called or
updated my google sheet

## Journal

* Realised some of my early commit messages were too long, took note to keep
commit message length in mind going forward

<br 
/>

# Acknowledgements

This web application was developed for the Python Essentials Portfolio
Project in the Full Stack Software Development Diploma with Code Institute.

Le gach dea-ghuí,
<br />
Sióg
<br />
'24

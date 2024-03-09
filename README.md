# Command Line Shopping List App

    Insert image :  Screenshot of terminal

## Live Site

[Visit deployed app on Heroku](https://shopping-list-project-pp3-7520c0c885a6.herokuapp.com)

## Repository

[Visit repository on GitHub](https://github.com/siogeile/shopping-list)

# Contents

[Markdown Content Generator](https://ecotrust-canada.github.io/markdown-toc/)

# User Experience Design (UX)

## Project Purpose

Provide a simple way for the user to manage their shopping list that stores data using a Command Line Interface developed using Python

### Developer's Goals

Develop an application using Python that functions as intended, passes through
a linter without significant issues and write code that handles empty or invalid
input data. The app should have consistent logic flow with standard programming
constructs implemented. The developer should identify and repair any coding
errors. The app should provide a solution to a real-world problem and should handle, store and manipulates user data. The development process should be
well documented through a version control system and the final version deployed to a cloud-based platform.

### External User's Goal

Manage items in a list for purchase at a later time.

#### First Time User

> *"I would like something that is quick to learn and straightforward"*

#### Returning User

> *"I tend to lose any handwritten lists that I write so I would like something that saves my data where it can't be lost."*
>
> *"A shopping list helps me remember what I need, but sometimes I need help remembering what I need to remind myself about! A seperate list where items are stored after they have been cleared from the shopping list that I can look at for reminders would be helpful"*

## Program Flowchart

    Insert image :  Flowchart


## Data Storage

The data for the application with be stored in google sheets which is available
to view [here](https://docs.google.com/spreadsheets/d/1Cx9JBL5leWkGEfrdIX3eBIJBtIoJtdgia2ubThSCp_Y/edit?usp=sharing)

## Existing Features

### The Main Menu

### View Shopping List

### Add Item

#### Collect user input
#### Validate user data
#### Update Google Sheets with user data

### Remove Item

#### Collect user input
#### Validate user request
#### Remove appropriate values from Google Sheets

### Exit

### Repeat or Return and Clear Terminal

## Future Features

* Add validation to ensure there is no empty space at the start of an entry
<i><b>or</b></i> a function that clears blank spaces that are entered as the first character
of an entry

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


_______________________________________________________________

## Deployment

This project is deployed using Code Institute's mock terminal for Heroku.

Steps for Deployment:

1. Fork or Clone this Depository
2. Set up Google Sheets and Google Drive APIs
3. Download the Key json file from Google, upload it to the project. Change the name to creds.json
4. Create a new Google Sheet named 'commandline-budgetapp'
5. Add label one worksheet 'users'
6. Create new Heroku app
7. Set the buildpacks to python and node.js (in that order)
8. Link the Heroku app to the repository
9. Click Deploy

## Credits

#### Love Sandwiches Code Along Project by the Code Institute

* Used code from the love-sandwiches walkthrough project closely up until
commits 390bc5d and 1963a99.
* Here I was still using code from that project but only relevant sections from
the project that I changed to work for my app

#### [Geek Tutorials](https://www.youtube.com/watch?v=0m7csmqWAgI) on YouTube

*  Used code from "Python - Code a Shopping List App (Part 1/3) to get me
started in commit f1d5751
* Started to write my own code within this code in commit eacf398 when adding
functions to menu items 1 and 2

* Deployment steps copied from adamsburge on GitHub's Command Line Budget App [Repo](https://github.com/adamsburge/commandline-budgetapp)

## Journal

* Realised some of my early commit messages were too long, took note to keep
commit message length in mind going forward

* List will not update unless I exit the app and re-enter - attempting to fix
this issue (fixed it by calling "shopping_list = shopping_list_items()" into
the print_shopping_list())
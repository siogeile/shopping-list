![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome Sióg Davin Murphy,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!

--------------------

## Credits

#### Love Sandwiches Code Along Project by the Code Institute

* Used code from the love-sandwiches walkthrough project closely up until commits 390bc5d and 1963a99.
* Here I was still using code from that project but only relevant sections from the project that I changed to work for my app

#### [Geek Tutorials](https://www.youtube.com/watch?v=0m7csmqWAgI) on YouTube

*  Used code from "Python - Code a Shopping List App (Part 1/3) to get me started in commit f1d5751
* Started to write my own code within this code in commit eacf398 when adding functions to menu items 1 and 2


## Journal

* Realised some of my early commit messages were too long, took note to keep commit message length in mind going forward

* List will not update unless I exit the app and re-enter - attempting to fix this issue (fixed it by calling "shopping_list = shopping_list_items()" into the print_shopping_list())

## Future Features

* Validate to ensure there is no empty space at the start of an entry
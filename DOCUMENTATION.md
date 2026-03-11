# Documentation
This is where we will document all of our changes to the seperate modules

## Ground Rules and Git Setup
To download the git into your desired directory/venv go there and type "git clone https://github.com/jamontroy/Library-Lunatic.git", this should download the files into your directory

Contribution Workflow for making changes to the repo

1. Pull the most recent version of the project
   git pull

2. Make your code changes

3. Stage your changes
   git add .

4. Commit your changes
   git commit -m "Describe what you changed"

5. Pull again to make sure the repo is up to date
   git pull

6. Push your changes to GitHub
   git push


## Ground Rules Around Modules
I'm not going to lie I'm not a software developer so I looked up how I/We should approach this to avoid the 1000 line obelisk of code

We are going to create modules that contain a containerized aspect of the game. Some examples of these conatainers will be
- player.py
    - player collisions
    - variables such as positioning
- bookshelves.py
    - collisions
- books.py
    - collisions
    - array with how many appear
- hazard.py
    - collision
- palette.py
    - centralized place for all of the colors in the game
- hud.py
    - timer
    - points
    - Inventory
- draw.py
- input.py
    - how inputs from the player output into the game

Of course this isn't an exhaustive list but I hope it helps to illustrate a little bit how to segment info. We definitely will add more modules when stuff comes up

# Actual Documentation

## books.py
Contains the Book class.

Each book has a tag "red", "blue", "green"
that must match a shelf tag to score a point.

Usage:
book = Book(center=(x, y), tag="red")
book.draw(surface)

To create a book:
- center is a tuple of (x, y) position on screen
- tag must be one of: "red", "green", "blue"

## Colors (palette.py)
All colors live in COLORS from Source_Code/palette.py 
(feel free to change anything )

COLORS.player      - the player sprite
COLORS.wall        - walls and barriers for outside map or around
COLORS.hazard      - hazard sprites for hazard throught map
COLORS.book_red    - red book
COLORS.book_green  - green book
COLORS.book_blue   - blue book
COLORS.shelf_red   - red shelf for the red books
COLORS.shelf_green  - green shelf for green books
COLORS.shelf_blue   - blue shelf (you guessed it blue books)
COLORS.text        - main text color this is a bright white we can change later to whatever
COLORS.subtle      - secondary text color like a grayer color can also change to whatever
COLORS.hud_timer_ok  - timer color when plenty of time (Just an idea I had to have color change based on time left on lock can add later or whatever)
COLORS.hud_timer_low - timer color when running out of time (red)
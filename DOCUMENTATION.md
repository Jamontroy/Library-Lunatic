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

## game.py
Is made to be a compilation of all of the classes to run the game

It currently has the 4 basic method of
- __init__
    - Initializes the screen, the Player, the Draw class, and updates running to True
- handle_event()
    - handle_event is reading singular events that are happening while the game is played.
    - So it has conditional to respond based on those events
    - If the user pressed escape we want to set self.running to False to kill the game.
- update()
    - Will run all of the individual update methods from the other classes to keep it clean
    - self.player.update(dt) - runs the player.update method
- draw
    - runs the draw method from Renderer


- Added self.timer = 60.0 to track time remaining
- Added self.hud = HUD(self.screen, self.SCREEN_W) to initialize the HUD
- update() now counts the timer down each frame with self.timer -= dt
- draw() now calls self.hud.draw() to render the HUD on screen

## draw.py

- Class Renderer
    - initializes the screen
    - takes the draw methods from other classes such as player and combines them into Renderer

## player.py

- Class player
The player class contains all of the movement and drawing for the player box. The movement currently is based off of the week 2 example with easily changable feel variables at the top of the file.
    - variables(SPEED, ACCEL, FRICTION, STOP_THRESHOLD)
    - __init__
        - self.rect creates a rect in the center of the screen
        - self.pos gets the center position for self.rect
        - self.velocity is initialized
        - * Note the point of Vector2 is to have a placehold for x and y that can be computed at the same time. Its essentially an object holding both the x and y values.
    - read_direction
        - This section is is that actual key to movement with normalization.
        - returns as a Vector2 with x and y
        - if direction key pressed move to corresponding direction
        - normalize the direction so that it does not do the 1.4x on diagonals
    - update
        - this section is mostly updating movement based on the absense or presence of keystrokes
        - velocity = direction times acceleration times dt
        - friction is only applied when there is no key press
        - There is a STOP_THRESHOLD to completely stop the player if their velocity is less than 20
        - There is a conditional to make sure velocity doesn't go above SPEED

        - Move Code
            - changes pos based on where the players velocity
            - right after that it changes the rect.center to the new center of the rectange based on thew updated pos
            - It then checks if the rectangle is on an edge and clamps it if it is.
            and if that is the case pos is updated
    - draw
        - has the draw code the the player rectange.

## bookshelves.py
    I'll fill this out when its more fleshed out.

## hud.py
Contains the HUD class which draws the display at the top of the screen.

- Class HUD
    - __init__
        - takes screen and screen_w to know where to position text
        - sets up the font used for all HUD text
    - _draw_text
        -  method to avoid repeating render and blit every time we draw text
    - draw
        - draws the HUD panel at the top of the screen
        - Score shown in the top left
        - Timer shown in the top center, turns red when under 10 seconds testing this now sure if we will like it
        - Carrying count shown in the top right

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

- COLORS.player      - the player sprite
- COLORS.wall        - walls and barriers for outside map or around
- COLORS.hazard      - hazard sprites for hazard throught map
- COLORS.book_red    - red book
- COLORS.book_green  - green book
- COLORS.book_blue   - blue book
- COLORS.shelf_red   - red shelf for the red books
- COLORS.shelf_green  - green shelf for green books
- COLORS.shelf_blue   - blue shelf (you guessed it blue books)
- COLORS.text        - main text color this is a bright white we can change later to whatever
- COLORS.subtle      - secondary text color like a grayer color can also change to whatever
- COLORS.hud_timer_ok  - timer color when plenty of time (Just an idea I had to have color change based on time left on lock can add later)
- COLORS.hud_timer_low - timer color when running out of time (red)
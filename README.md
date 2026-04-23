# Lunatic-Librarian Description

Library Lunatic is an Overcooked-style time-attack arcade game set in a library. You play a frantic librarian racing to pick up color-coded books scattered across the floor and deliver them to their matching color-coded bookshelves before the clock runs out.

Core loop: Pick up colored books (max 3 at a time) → deliver to matching shelf → score points and earn +2 seconds on the timer → continue until time runs out trying to get high score. Powerups and hazards mix up the pace.

## How to run

From this folder:

- `python3 -m venv .venv`
- `source .venv/bin/activate`
- `python -m pip install -r requirements.txt`
- `python main.py`

The game window is 600 × 800 and runs at 60 FPS. Audio requires working speakers/headphones but is not required for gameplay.

## Controls
Can control the character using WASD or arrow keys:
    Move up:    W or ↑
    Move down:  S or ↓
    Move left:  A or ←
    Move right: D or →
    Start game (from title screen):  Space
    Restart (from game over screen): Space
    Quit:      Esc or close window

Pickups / interactions are automatic on contact:
    Walk over a book to pick it up (carry up to 2)
    Walk into a matching-color shelf to deliver all carried books of that color
    Walk over a powerup to activate it
    Bumping a pedestrian hazard costs 5 seconds

Powerups Include:
    Speed Boots — temporary movement speed boost (5s)
    Bookmark — 2× score multiplier (5s)
    Hourglass — freezes the countdown timer (5s)

Known Issues
Issue | Severity | Notes:
    Some sprites can appear slightly clipped into shelves/walls due to sprite size vs. hitbox boundaries| Low | Visual only and gameplay unaffected
    Books can spawn stacked on one another if their spawn positions happen to overlap | Low | Very Rare both books remain collectable

None of these cause crashes or softlocks. The game passes a full start → play → game over → restart cycle cleanly.

## Credits
Code — Joe Montroy, Mazen Malas, James Knott 

Sprites & pixel art — Joe Montroy (original work)

music.wav — background loop (source: TODO change)
bookPickup.mp3 — book pickup SFX (source: TODO change)
BookDropOff.wav — book delivery SFX (source: TODO change)
lolo_s-power-up-474087.mp3 — powerup pickup SFX (source: TODO change)
u_n2rdb8hxnh-incorrect-293358.mp3 — incorrect/wrong delivery SFX (source: TODO change)
PedCol.mp3 — pedestrian collision SFX (source: TODO confirm)
timerCountdown.wav — final-seconds countdown SFX (source: TODO change)
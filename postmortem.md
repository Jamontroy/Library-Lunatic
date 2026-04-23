# Postmortem

This project saw the development of Lunatic Librarian, a time-attack arcade game. It follows our titular librarian, 
collecting/returning books, avoiding nasty patrons, and taking advantage of certain powerups to do so. During its 
development, we went through a few challenges, found unique solutions, and experienced unexpected circumstances.

First off, though many of the systems had their challenges, one of the easiest starting points was a movement system. 
The system implemented was an 8-directional normalized input. Due to the nature of the game being time-attack, we chose
for a lighter but tighter input feel, as to keep the pace of the game from feeling sluggish. Because one of the first
things we attacked in class was a basic movement system, this was one of the most basic to implement, giving us a good 
baseline for our first deliverable. 

We also found that, despite our expectations, there are some systems that were easier to implement than first thought.
Case in point: collision behavior. The player interacts with numerous objects throughout the game - books, bookshelves,
patrons, etc. However, each one of these objects has a different collision behavior with the player. However, most of 
our collisions are built upon the same framework: draw the bounding box, detect collisions, and define collision behavior.
This framework allowed us to greatly simplify, and thus diversify, the behaviors of our objects. 

However, as seen with collisions, one of our biggest hurdles was class structure. While some of our classes in different
files are well-defined, such as for the player and for the books, others were somewhat ambiguous, like the collisions
class. In this particular instance, some collision behaviors were easy to define outside the main game structure, as is
the case with static objects, like the HUD or the Bookshelves. However, for objects that affect the game's internal
state, like with powerups or with books, which prevented us from fully outsourcing our collision behaviors to
Collisions.py.

Another challenge we faced was the score system. Our aim for the system was to have the librarian carry a stack of books
and return them to their respectively colored bookshelves. However, upon first implementation, we found it hard to be
able to implement a system that allowed books to be returned in both an arbitrary order and with potentially multiple 
returns made during one interaction. As such, we had to figure out what was essentially a proto array based inventory
system. This allowed us to be able to iterate through the inventory for each relevant item, and to be able to display it
as such on the HUD.

If we were to start with a fresh slate, one thing that we would have done differently is the planning of the file structure.
As it stands, our file structure is somewhat well organized. However, as mentioned before, there are parts of our code
that caused us some ambiguity between what the game handled vs what it outsourced to other classes. As such, before even
beginning to program in the most basic elements of the game, we should have navigated better the organizational structure
of our system, and what it would take in order to maintain and upkeep that system structure.

However, with what we had, we were still able to playtest the game, and tune different knobs of it therein. One such
adjustment towards the tail end of development, after implementing the hazards class. Originally, we had two hazards:
Pedestrian and Puddle. The pedestrian "takes up the librarian's time", decreasing the game timer by a substantial amount.
However, the puddle essentially functioned in the same way, except spawned at random areas on the play map and would
cause the librarian to "slip", and pause for a few moments before being able to move again. After playtesting, however,
the Puddle hazard did not aid the feel of the game. In fact, it actively interrupted a flow, causing an unpredictably 
choppy feel to the gameplay. As such, we decided to phase out that object, and instead make the patron behavior more
complex by introducing rules governing its movement, rather than simply defining a fixed path in which it would travel.
## Run software.py after running PokerStars game.

####Working features:
####    -> Recon cards on table
####    -> Recon game stage
####    -> Recon players' cards
####    -> Recon player's turn
####    -> Recon possible moves
####    -> Gives you tight-aggressive rating.

######Example output:
######    Cards on table: S8 H7 ST
######    Game stage: Floop
######    Player cards: D9 HA
######    Tight-agressive rating: trash
######    Possible moves: raise fold call

**This project has been made to learn some python basics, it's far from being perfect. Sorry!**
Software fits up to 6 game windows on full HD screen (hard coded, it should be changed).
ATM it's only operating on one table (first).
6 and 9 are both recognized as 6. This problem has been solved in card_value() function
There are a some not used function, those were used to save pictures of cards, players, token etc.
Screenshot > screen_all_and_save() makes a screenshot of each screen and saves it to screenshots folder.
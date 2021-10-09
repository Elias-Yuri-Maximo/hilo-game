from game.director import Director

print("Welcome to High/Low!")
print("Ready to risk it all? Guess whether the next card will be higher or lower to win points!")
print("You lose if your score becomes zero!")
print("Here's 300 points to start. Good luck!\n")

director = Director()
director.start_game()

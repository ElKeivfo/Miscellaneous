NumberofGuesses = 0
NumberToGuess = int(input("Please choose a number between 1 and 10 (1 and 10 are included): "))
while NumberToGuess == float or (NumberToGuess <=0 or NumberToGuess >= 11):
  try:
    NumberToGuess = int(input("Please choose a number between 1 and 10 (1 and 10 are included): "))
  except:
    NumberToGuess = int(input("Invalid! Please choose a number between 1 and 10 (1 and 10 are included): "))
Found = False
while NumberofGuesses != 5 and Found == False:
  guess = int(input("Player2 please guess the number of Player1: "))
  NumberofGuesses += 1
  if guess == NumberToGuess:
    print("Player 2 Wins")
    Found = True
if NumberofGuesses == 5:
  print("Player 1 Wins")

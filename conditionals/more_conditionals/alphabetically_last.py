# A program which asks the user for two words. 
# The program then prints out whichever of the two comes alphabetically last.

word1 = input("Please type in the 1st word: ")
word2 = input("Please type in the 2nd word: ")

#.lower() is used to convert the inputs into lowercase characters
if word1.lower() > word2.lower():
    print(f"{word1} comes alphabetically last.")

elif word2.lower() > word1.lower():
    print(f"{word2} comes alphabetically last.")

else:
    print("You gave the same word twice.")


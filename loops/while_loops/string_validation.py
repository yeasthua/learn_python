# A program which keeps asking the user for words. If the user types in end, the program then prints out the the "sentence" formed, and finish.
# The program also ends if the user typed in the same word twice in a row.

word = ""
prev_word = ""
while True:
    user_word = input("Please type in a word: ")

    if user_word == "end":
        break
    
    if user_word == prev_word:
        break
    
    prev_word = user_word   # Variable for previous word (only stores the previous input every iteration using just " = ")
    word += user_word + " " # Stores every input into {word} to be concatenated with " "

print(word)
# A program which asks for the user's name. 
# If the name is Huey, Dewey or Louie, the program should recognise the user as one of Donald Duck's nephews.

# And if the name is Morty or Ferdie, the program should recognise the user as one of Mickey Mouse's nephews.

name = input("Please type in your name: ")

if name.lower() == "huey" or name.lower() == "dewey" or name.lower() == "louie":
    print("I think you might be one of Donald Duck's nephews.")

elif name.lower() == "morty" or name.lower() == "ferdie":
    print("I think you might be one of Mickey Mouse's nephews.")

else:
    print("You're not a nephew of any character I know of.")
# Program that uses multiple if's to print other if block that is within its range
print("What is the weather forecast for tomorrow?")

temp = int(input("Temperature: "))
rain = input("Will it rain (yes/no): ")

#if over 20, this line will the only one that prints
print("Wear jeans and a T-shirt")

#if less than 20 this line alongside the other prints prior to this will run
if temp <= 20:
    print("I recommend a jumper as well")

#if less than 10 this line alongside the other prints prior to this will run
if temp <= 10:
    print("Take a jacket with you")

#if less than 5 this line alongside the other prints prior to this will run
if temp <= 5:
    print("Make it a warm coat, actually")
    print("I think gloves are in order")

# Runs if input on rain is "yes"
if rain == "yes":
    print("Don't forget your umbrella!")

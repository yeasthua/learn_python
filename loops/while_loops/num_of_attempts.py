# A program which keeps asking the user for a PIN code until they type in the correct one, which is 4321.
attempts = 1

while True:
    pin = int(input("PIN: "))

    if pin == 4321:
        break
   
    print("Wrong")
    attempts += 1

if attempts == 1:
    print("Correct! It only took you one single attempt!")

else:
    print(f"Correct! It took you {attempts} attempts")
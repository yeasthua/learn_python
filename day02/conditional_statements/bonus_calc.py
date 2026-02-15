points = int(input("How many points are on your card? "))

# If there are less than a hundred points on the card, the bonus is 10 %
if points < 100:
    points_new = points * 1.1
    print("Your bonus is 10 %")

# In any other case the bonus is 15 %
if points >= 100:
    points_new = points * 1.15
    print("Your bonus is 15 %")

print("You now have", points_new, "points")
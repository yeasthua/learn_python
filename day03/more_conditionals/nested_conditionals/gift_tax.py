# A program which calculates the correct amount of tax for a gift from a close relative.


gift = float(input("Value of gift: "))

# if gift is lower than 5000, it has no tax
if gift < 5000:
    tax = 0

# TAX TABLE for 5000 to 1,000,000
elif gift >= 5000 and gift <= 1000000:
    if gift <= 25000:
        tax = (100 + (gift - 5000) *0.08)
    
    elif gift <= 55000:
        tax = (1700 + (gift - 25000) *0.10)
    
    elif gift <= 200000:
        tax = (4700 + (gift - 55000) *0.12)
    
    elif gift <= 1000000:
        tax = (22100 + (gift - 200000) *0.15)

# TAX TABLE for above 1,000,000    
else:
    tax = (142100 + (gift - 1000000) *0.17)


# If there is no tax, this block will run
if tax == 0:
    print("No tax!")

# Otherwise this block will run
else:
    print(f"Amount of tax: {tax} euros")
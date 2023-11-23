print("Welcome to the tip calculator")
bill = float(input("What was thw bill amount?$"))
per = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
ppl = int(input("How many people to split the bill?"))
pay = (((bill * per)/100)+bill)/ppl
print(f"Each person should pay : ${round(pay,2)}")
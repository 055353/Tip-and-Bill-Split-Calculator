# Creating a tip calculator and a bill split calculator

# Taking the total bill
Bill = float(input("What is the total bill? "))

# Asking for the tip percentage
Tip = float(input("What percentage do you want to give? "))

# Number of people splitting the bill
Number_of_people = int(input("How many people are splitting the bill? "))

# Calculating the tip amount
Tip_given = Tip / 100
final_tip = Bill * Tip_given

# Calculating the total bill including tip and splitting among people
Total_Bill = (Bill + final_tip) / Number_of_people

# Printing the amount each person should pay
print("Each person should pay " + str(Total_Bill) + " Ghc")

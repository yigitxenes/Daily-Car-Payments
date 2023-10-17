miles = int(input("Enter The Total Miles Driven in a Day: "))
gas = int(input("Enter How Much Is a 1 Gallone of Gasoline: "))
avg = int(input("Enter Your Car's Average Miles Per Galon: "))
fees = int(input("Enter How Much Parking Fees You Get a in a Day: "))
tolls = int(input("Enter How Much You Pay Tolls Per Day: "))
daily_cost = miles*avg/gas+fees+tolls
print("Daily Cost: ", daily_cost, "$")  

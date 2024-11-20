total = 0 
count = 0


userInput =input("Please enter a number: ")
while userInput != "done":
    total += int(userInput)
    if userInput == "done":
         count += 1
         Print("Running average: total/count")

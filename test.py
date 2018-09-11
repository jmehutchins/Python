numlist = list()
while True :
    inp = input("Enter a number: ")
    if inp == "done" : break
    try:
        value = float(inp)
    except:
        print("Invalid entry, try again")
        continue
    value = float(inp)
    numlist.append(value)
average = sum(numlist) / len(numlist)
print("Average: ", average)

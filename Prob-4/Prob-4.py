# Module 7
#   Programming Assignment 10
#     Prob-4.py

# <Garrett>

# File path = Prob-4/balances.txt

def main():
    fileName = open('Prob-4/balances.txt', 'r')
    interest = 1 + float(input("Enter annual interest rate as a decimal value: "))
    items = []
    for line in fileName.readlines(): 
        for line in line.split():
            items.append(float(line))
    fileName.close()
    newBal(interest, items)
    return items

def newBal(interest, items):
    newItems = []
    for x in items:
        y = interest * x
        newVal = format(round(y, 2), '.2f')
        newItems.append(newVal)
    with open('Prob-4/balances.txt', 'w') as f:
        for item in newItems:
            f.write(item + "\n")

main()  
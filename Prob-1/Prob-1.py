# Module 7
#   Programming Assignment 10
#     Prob-1.py

# <Garrett>

def main():
    sum = 0
    x = float(input("Enter a positive number to add to the sum (negative to quit): "))
    while x >= 0:
        sum += x
        x = float(input("Enter a positive number to add to the sum (negative to quit): "))
    print("The sum of the numbers entered is", sum)
main()    
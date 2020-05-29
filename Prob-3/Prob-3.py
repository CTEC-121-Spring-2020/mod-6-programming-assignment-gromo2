# Module 7
#   Programming Assignment 10
#     Prob-3.py

# <Garrett>

def main():
    '''
    sum = 0
    x = float(input("Enter a positive number to add to the sum: "))
    while x:
        sum += x
        x = float(input("Enter a positive number to add to the sum: "))

    print("The sum of the numbers entered is", sum)
    
    x = -1       
    while x < 0: 
        x = float(input("Enter a positive number to add to the sum: "))
'''
    # do not change the while loop definition below
    x = float(input("Enter a positive number to add to the sum (blank to exit): "))
    sum = 0
    try:
        while True:
            if x < 0:
                print("The number you have entered is not positive.")
                x = float(input("Enter a positive number to add to the sum (blank to exit): "))
            while x >= 0:
                sum += x
                x = float(input("Enter a positive number to add to the sum (blank to exit): "))
    except:
        print("The sum of the values is:", sum)




        



main()    
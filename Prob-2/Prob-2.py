# Module 7
#   Programming Assignment 10
#     Prob-2.py

# <Garrett>
# file path: Prob-2/Prob-2-Input.txt
def main():
    fileName = input("Enter the path of the desired file: ")
    inFile = open(fileName, 'r')
    sum = 0
    for line in inFile.readlines():
        for line in line.split():
            print(line)
            sum += float(line)
            
    print("The sum of the numbers is: ", sum)
main()
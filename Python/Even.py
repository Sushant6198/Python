def CheckEven(No):
    if(No % 2 == 0):
        print("It is even number")
    else:
        print("It is odd number")

def main():
    print("Enter Number : ")
    A = int(input())

    CheckEven(A)

main()
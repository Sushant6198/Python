
def main ():
    print("Enter number of elements that you want to list: ")
    size = int(input())

    Arr = list()

    print(input("Enter the elements: "))

    for i in range(size):
        no = int(input())
        Arr.append(no)

    print("Entered elements are : ",Arr)

if __name__ == "__main__":
    main ()

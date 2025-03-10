#Check_Number
def numbers():
    numbers = int(input("Enter any numbers: "))
    if numbers % 2 == 0:
        print(numbers, "is an even number")
    else:
        print(numbers, "is an odd number")
        
numbers()

while True:
    a = input("Run again?: ")
    if a == "Yes":
        numbers()
        
    else:
        b = print("Program Done")
        break
    
import time

def numCheck(number): #checks if a number is negative or not
    numinput = int(number)
    if numinput >= 0:
        return int(number)
    else:
        print("Please input a non-negative number")
        return None

def primeCheck(firstnum, secondnum):
    print("Your prime numbers are: ", end="")
    for number in range(firstnum, secondnum):
        is_prime = True
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
        if is_prime and number > 1:
            print(number, end=" ")
    print("\n")
    time.sleep(1)

while True:
    #setting the variables to a value of None
    #Because it'll conflict if set to 0
    startRange = None
    endRange = None

    while startRange is None:
        startRange = numCheck(input("Enter a number [start]: "))
    if startRange == 0:
        print("Thank you have a nice day!")
        break

    while endRange is None or startRange > endRange:
        endRange = numCheck(input("Enter a number [end]: "))
        if startRange > endRange:
            print(f"Enter a number greater than {startRange}")

    primeCheck(startRange, endRange + 1)


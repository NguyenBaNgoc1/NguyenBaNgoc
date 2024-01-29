Ngov = int(input("Enter number u wanna check: "))

Me = False

if Ngov == 1:
    print("The number is not a prime number")
else:
    for i in range(2, Ngov):
        if Ngov % i == 0:
            Me = True
            break

if Me:
    print("The number is not a prime number")
else:
    print("The number is a prime number")


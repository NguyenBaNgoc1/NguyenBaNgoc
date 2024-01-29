prime = int(input("Enter a number:  "))

def is_prime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num -1):
            if num % i == 0:
                return False
        return True

result = is_prime(prime)

def Tong_so_nguyen_to(i,j):
    sum = 0
    for v in range (i, j):
        if is_prime(v):
            sum += v
    return sum

My_total_number = Tong_so_nguyen_to(1, 25)
print (My_total_number)
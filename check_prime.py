NUM=int(input("Enter Number:"))

def check_prime(num):
    for i in range(1,num):
        if num % i == 0:
            return False
    return True

prime_status = check_prime(NUM)
if prime_status == True:
    print("The given number is prime")
else:
    print("The given number is not prime")

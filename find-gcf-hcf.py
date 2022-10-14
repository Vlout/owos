NUM1=int(input("Enter Number 1:"))
NUM2=int(input("Enter Number 2:"))

def lcm(num1,num2):
    # range of these numbers must lie between num1*num2 (if no common factors/prime) and greatest number just run through all of them
    if num1 > num2:
        greater = num1
    else:
        greater = num2
    for i in range (greater, (num1*num2)+1):
        if i%num1==0 and 1%num2==0:
            print("LCM found")
            return i

def gcf(num1, num2,lcm):
    gcf = int((num1* num2) / lcm)
    print("GCF found")
    return gcf

LCM=lcm(NUM1, NUM2)
GCF=gcf(NUM1, NUM2, LCM)

print("GCF and LCM of", NUM1, NUM2,":")
print (GCF,",", LCM)

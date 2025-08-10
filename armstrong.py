# STUB CODE
def armstrongcheck(num, temp, fa):
    while num > 0:
        ans = num % 10
        fa = fa + ans * ans * ans
        num = num // 10
    if fa == temp:
        print("armstrong")
    else:
        print("not a armstrong")

#DRIVER CODE
num = int(input("enter the number to check armstrong or not:"))
temp = num
fa = 0
armstrongcheck(num, temp, fa)

###############

#num = int(input("enter the number to check armstrong or not:"))
#temp = num
#fa = 0
#while num > 0 :
#    ans = num % 10
#    fa = fa + ans * ans * ans
#    num = num // 10
#if fa == temp:
#    print("armstrong")
#else:
#    print("not a armstrong")
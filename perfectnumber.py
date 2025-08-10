def perfectnumber (num):
    for i in range(1, num):
        if num % i == 0:
            mylist.append(i)
    sums = sum(mylist)
    if num == sums:
        print("perfect number")
    else:
        print("not a perfect number")

num = int(input("enter the number:"))
mylist = []
perfectnumber(num)

#####################
#num = int(input("enter the number:"))
#mylist = []
#for i in range (1, num):
#    if num % i == 0:
#        mylist.append(i)
#sums = sum(mylist)
#if num == sums:
#    print("perfect number")
#else:
#    print("not a perfect number")

#######################

def perfectnum(num):
    count = 2
    sum = 1
    while (count <= (num//2)):
        if ((num % count)== 0) :
            sum += count
        count += 1
    if (num == sum):
        print("P")
    else :
        print("NP")
num = 6
perfectnum(num)
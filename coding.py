###weird or not###
n = int(input())
if n % 2 == 1:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")

####arithemetic operators####

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c=a+b
    print(c)
    d=a-b
    print(d)
    e=a*b
    print(e)

### division ###

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c=a//b
    print(c)
    d=a/b
    print(d)


### for loop ###
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i**2)


### consecutive numbers using for loop###
if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        print(i,end="")

### leap year or not###
def is_leap(year):
    if year % 4==0:
        if year % 100==0:
            if year %400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    

year = int(input())
print(is_leap(year))
        




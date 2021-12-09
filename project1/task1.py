#targil_1.5
"""
s=int(input("enter your salary:"))
p=int(input("percent:"))
n= s*p/100+s
print(f" your new salary is{n}")
"""
#targil_1.6
"""
r=int(input("enter radius:"))
pi=3.14
print(f"Circle area: {r*r*pi}\nCircle circumference: {2*pi*r}")
"""
#targil3.1
"""
num=int(input("enter a number"))
if num%2==0:
    print("even")
else:
    print("uneven")
"""
#targil3.2
"""
n1=int(input("enter a number"))
n2=int(input("enter a number"))
n3=int(input("enter a number"))
if n1>n3 and n1>n2:
    print(n1)
elif n2>n1 and n2>n1:
    print(n2)
elif n3>n1 and n3>n2:
elif  print(n3)
else: print("sorry, try different numbers")
"""
#targil3.3
"""
n=input("enter the amount of computers you treated")
if n =='':
    print("tomorrow you need to treat 30")
else:
    print(f"you need to treat {int(n)*2}")
"""
#targil4.1
"""
n1=int(input("enter number"))
n2=int(input("enter number"))
n=n1
if n1%2==0:
    while n<n2-2:
        print(n+2)
        n+=2
else:
    while n<n2-1:
        print(n+1)
        n+=2
"""
#targil4.2
"""
n1=int(input("enter number greater than 10:"))
while n1%2==0 or n1%3==0 or n1%5==0  or n1%7==0:
    print("not prime number")
    n1 = int(input("enter number"))
print("prime number")
###
n1=int(input("enter number:"))
c=1
while n1%c!=0 and c<10:
    c+=1
    n1 = int(input("enter number greater than 10:"))
print("prime")
"""
#targil4.3
"""
n=int(input("Guess the number I picked"))
c=1
while n!=c:
    if n<c:
        n=int(input("too low, try again"))
    elif n>c:
        n = int(input("too high, try again"))
if n==c:
    print(f"well done, my number is {c} ")
 """
#targil4.4
#print("choose a number between 0 and 100 and i'll guess it")












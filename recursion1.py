
def display(n):
    print(n)
    n+=1
    if n<=5:
        display(n)

display(1)


#Factorial of recursion:

def fact(num):
    if num == 1:
        return 1
    else:
        return num*fact(num-1)

result = fact(5)
print(result)


def fact(num):
    if num==1:
        return 1
    else:
         
        return num + fact(num-1)
    
result = fact(2)
print(result)


#Home Work:

#reverse a string:

def reverse(str):
    size = len(str)
    if (size == 0):
        return
    else:
        last_char = str[size-1]
        print(last_char,end=" ")
        reverse(str[0:size-1])

reverse("Pavithra")

#Palindrome:

def palindrome(sen):
    if len(sen)!= 1:
        sen1 = palindrome(sen[1:])+sen[0]
        print("sen1",sen1, "sen", sen)
        return sen1
        
    else:
        return sen
    
sen = "Kalaivani"
if sen == palindrome(sen):
    print("The string is palindrome")
else:
    print("The string is not palindrome")


#Armstrong Number:
    def arm(n):
        if n<10:
            return n*n*n
        return (n%10)*(n%10)*(n%10)+arm(int(n/10))
num = int(input("Enter any number"))

r = arm(num)

if r == num:
    print(num,"Is an Amstrong Number")
else:
    print(num,"Is not an Amstrong Number")


#Fibonacci series :
    def fibonacci(num):
        if num == 0:
            return 0
        elif num == 1:
            return 1
        else:
            return fibonacci(num-2) + fibonacci(num-1)
    for x in range(20):
        print(fibonacci(x))
    

    
#GCD:

def gcd(a,b):
    if a%b==0:
        return b
    return gcd(b, a%b)
num = int(input("Enter first Number "))
num1 = int(input("Enter second number"))
print("GCD = " ,gcd(num,num1))


#lcm:
def lcm(a,b,c):
    c = c+b
    if c%a == 0 and c%b ==0:
        return c
    return lcm(a,b,c)
num = int(input("Enter first number"))
num1= int(input("Enter second number"))
m = 0
print("LCM = ",lcm(num,num1,m))





def getUserNamePassword(username,password):
    if username != 'ABCD':
        print("incorrect username")
        username = input("Enter username: ")
        password = input("Enter your password: ")
        getUserNamePassword(username,password)
        
        if password != 'Boopathy':
            print("Incorrect password")
            username = input("Enter username: ")
        password = input("Enter your password: ")
        getUserNamePassword(username,password)
        
        username = input("Enter username: ")
        password = input("Enter your password: ")
        getUserNamePassword(username,password)






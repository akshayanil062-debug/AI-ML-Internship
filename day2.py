task 2 : Basic coding
print("Name: Akshay Anil")
print("Age: 22")
print("Course: B.Tech")

a = 10
b = 5
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)

num = 7
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

a = 10
b = 20
if a > b:
    print("Largest:", a)
else:
    print("Largest:", b)

name = input("Enter your name: ")
print("Hello", Akshay Anil)

Task 3 : Logic building
num = int(input("Enter number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

a = 5
b = 8
c = 3
if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)

marks = int(input("Enter marks: "))
if marks > 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
else:
    print("Grade C")

Task 4 : Loop Practice 
for i in range(1, 21):
    print(i)

for i in range(1, 11):
    if i % 2 == 0:
        print(i)

n = 5
sum = 0
for i in range(1, n+1):
    sum += i
print("Sum:", sum)

for i in range(10, 0, -1):
    print(i)

Task 5 : Fuction Practice 
def add(a, b):
    return a + b

print("Add:", add(3, 4))


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print("Is Prime:", is_prime(7))


def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

print("Factorial:", factorial(5))

Task 9 : Bonus
for i in range(1, 5):
    print("*" * i)

num = 123
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
print("Reversed:", rev)

num = 12345
count = 0
while num > 0:
    count += 1
    num = num // 10
print("Digits:", count)

# Task 2: List Problems -

nums = [10, 5, 20, 8, 15, 5, 10]

print("Original List:", nums)

# 1. Find maximum and minimum
print("\n1. Maximum and Minimum")
print("Maximum:", max(nums))
print("Minimum:", min(nums))

# 2. Find second largest
print("\n2. Second Largest")
unique_nums = list(set(nums))   
unique_nums.sort()

if len(unique_nums) >= 2:
    print("Second largest:", unique_nums[-2])
else:
    print("Not enough elements")

# 3. Remove duplicates
print("\n3. Remove Duplicates")
no_duplicates = list(set(nums))
print("List without duplicates:", no_duplicates)

# 4. Count even and odd numbers
print("\n4. Count Even and Odd Numbers")
even = 0
odd = 0

for n in nums:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even numbers:", even)
print("Odd numbers:", odd)


# Task 3: String Problems - 

text = input("Enter a string: ")

# 1. Reverse string
print("\n1. Reversed String")
print("Reversed:", text[::-1])

# 2. Check palindrome
print("\n2. Palindrome Check")
if text == text[::-1]:
    print("It is a Palindrome")
else:
    print("It is NOT a Palindrome")

# 3. Count characters
print("\n3. Character Count")
print("Total characters:", len(text))

# 4. Count vowels and consonants
print("\n4. Vowels and Consonants Count")

vowels = "aeiouAEIOU"
v = 0
c = 0

for ch in text:
    if ch.isalpha():
        if ch in vowels:
            v += 1
        else:
            c += 1

print("Vowels:", v)
print("Consonants:", c)


# Task 4: Dictionary Problems - 

# 1. Create student list
students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

print("\nStudent List:", students)

# 2. Find topper
print("\n2. Topper")
topper = max(students, key=students.get)
print("Topper:", topper, "-", students[topper])

# 3. Calculate average
print("\n3. Average Marks")
average = sum(students.values()) / len(students)
print("Average:", average)

# 4. Filter passed students (pass mark = 50)
print("\n4. Passed Students (marks >= 50)")
passed = {name: marks for name, marks in students.items() if marks >= 50}
print(passed)

# Task 7: Logic Challenge - 

# Taking input for lists
list1 = list(map(int, input("Enter elements of list1: ").split()))
list2 = list(map(int, input("Enter elements of list2: ").split()))

# Combine both lists for some operations
combined = list1 + list2

print("\nList1:", list1)
print("List2:", list2)

# 1. Find second smallest number
print("\n1. Second Smallest Number")
unique = list(set(combined))
unique.sort()

if len(unique) >= 2:
    print("Second smallest:", unique[1])
else:
    print("Not enough elements")

# 2. Merge two lists without duplicates
print("\n2. Merge Without Duplicates")
merged = list(set(list1 + list2))
print("Merged list:", merged)

# 3. Find frequency of elements
print("\n3. Frequency of Elements")
freq = {}

for num in combined:
    freq[num] = freq.get(num, 0) + 1

print("Frequency:", freq)


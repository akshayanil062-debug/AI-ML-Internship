# Task 2: File Handling

filename = "data.txt"

# 1. Create file and write details
with open(filename, "w") as f:
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    f.write(f"Name: {name}\nAge: {age}\n")

print("\nData written to file.")

# 2. Read file and display
print("\nFile Content:")
with open(filename, "r") as f:
    content = f.read()
    print(content)

# 3. Append new data
with open(filename, "a") as f:
    new_data = input("\nEnter additional data to append: ")
    f.write(new_data + "\n")

print("\nData appended.")

# Read again
with open(filename, "r") as f:
    content = f.read()

# 4. Count number of lines
lines = content.split("\n")
print("\nNumber of lines:", len(lines))

# 5. Count number of words
words = content.split()
print("Number of words:", len(words))

# Task 3: Exception Handling

# 1 & 2: Divide by zero + invalid input
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

except ValueError:
    print("Error: Invalid input (enter numbers only)")

else:
    print("Result:", result)

finally:
    print("Execution completed\n")


# 4. File not found handling
try:
    with open("sample.txt", "r") as f:
        print(f.read())

except FileNotFoundError:
    print("Error: File not found")

# Task 4: Logic Challenge

filename = "data.txt"

with open(filename, "r") as f:
    content = f.read()

# 1. Find longest word
words = content.split()
longest = max(words, key=len)
print("Longest word:", longest)

# 2. Count vowels in file
vowels = "aeiouAEIOU"
vowel_count = 0

for ch in content:
    if ch in vowels:
        vowel_count += 1

print("Vowel count:", vowel_count)

# 3. Remove duplicate lines
with open(filename, "r") as f:
    lines = f.readlines()

unique_lines = list(set(lines))

with open("cleaned.txt", "w") as f:
    f.writelines(unique_lines)

print("Duplicate lines removed. Saved in 'cleaned.txt'")

name = input("What is your name? ")
favorite_food = "pizza"
print("Hi " + name + "! I like " + favorite_food + " too!")

print(6 * 3)
print(10 % 3)
print(10 + 5)
print(10 % 2)

# age = input("How old are you? ")
# print(age + 1)

age = int(input("How old are you? "))
print(age + 1)

age = 17
print("You are " + str(age))

age = 12
if age < 13:
    print("You are a kid")

age = int(input("Enter age: "))
if age < 13:
    print("You are a kid")
else:
    print("You are a teenager")

score = int(input("Enter score: "))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("Keep trying")

number = int(input("Enter a number: "))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
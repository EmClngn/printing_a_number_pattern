# print a number pattern in the shape of a pyramid

# pseudo code

# ask user how many layers of the pyramid do they want
layers = int(input("How many layers do you want your pyramid to be? "))

# use for loop to create pattern
for outer in range(layers + 1):
    for inner in range(outer):
        print(outer, end = " ")
    print()


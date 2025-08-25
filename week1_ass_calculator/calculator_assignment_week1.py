# defining a funct for addition
def add(a, b):
    return a + b

# defining a funct for subtraction
def subtract(a, b):
        return a - b

# defining a fuct for multiplication
def prod(a, b):
      return a * b

# defining a funct for devision
def div(a, b):
      if b == 0:
          return "Cannot divide by zero"
      return a / b

# Collecting inputs
a = float(input("Enter first digit: ").strip())
opr = input("Enter operator (+, -, x, /): ").strip()
b = float(input("Enter second digit: ").strip())

# if statement + output
if opr == "+":
    print(a, opr, b, "=", add(a, b))
elif opr == "-":
    print(a, opr, b, "=", subtract(a, b))
elif opr == "x":
    print(a, opr, b, "=", prod(a, b))
elif opr == "/":
    print(a, opr, b, "=", div(a, b))
else:
    print("Invalid operator. Please use +, -, x, or /.")
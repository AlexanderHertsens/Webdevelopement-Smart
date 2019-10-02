"""

SOLUTIONS ROBUST ARE ON GITHUB RAFFSON (OPLEIDER)

"""

number1 = int(input("number 1: "))
number2 = int(input("number 2: "))
operator = input("operator(+ - * /): ")

if operator == "+":
	print(number1 + number2)
elif operator == "-":
	print(number1 - number2)
elif operator == "*":
	print(number1 * number2)
elif operator == "/":
	print(number1 / number2)
else:
	print("Something went wrong here")

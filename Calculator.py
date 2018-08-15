num1=float(input("Enter a first value: "))
op = input("Enter an operator: ")
num2=float(input("Enter a second value: "))



if op == "+":
    wynik = num1 + num2 
    print(wynik)
elif op == "-":
    wynik = num1 - num2
    print(wynik)
elif op == "/":
    wynik = num1 / num2
    print(wynik)
elif op == "*":
    wynik = num1 * num2
    print(wynik)
else:
    print("Invalid operation")
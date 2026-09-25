number1 = float(input())
number2 = float(input())

def max2(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2

result = max2(number1, number2)
print(result)
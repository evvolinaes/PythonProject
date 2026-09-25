a = int(input())
b = int(input())
c = int(input())

if a+b<=c or a+c<=b  or b+c<=a:
    print("Не существует")
else:
    p = a+b+c
    p1 = (a + b + c)/2
    s = (p1*(p1-a)*(p1-b)*(p1-c))**0.5
    print(p)
    print(f"{s:.2f}")



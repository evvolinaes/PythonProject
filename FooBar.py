
a = int(input())
if a%3==0 and a%5==0:
    print("Foobar")
else:
    if a%3==0:
        print("Foo")
    else:
        if a%5==0:
            print("Bar")
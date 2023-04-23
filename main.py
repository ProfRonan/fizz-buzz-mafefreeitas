x=int(input("digite um número:"))
y=True
if x % 3==0 and x % 5==0:
    y=False
    print("FizzBuzz")
elif x % 3==0:
    y=False
    print("Fizz")
elif x % 5==0:
    y=False
    print("Buzz")
else:
    y=True
    print(x)

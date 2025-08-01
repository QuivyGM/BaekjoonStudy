fb1 = input()
fb2 = input()
fb3 = input()

# if number exists
number = 0
if fb1.isdigit():
    number = int(fb1) + 3
elif fb2.isdigit():
    number = int(fb2) + 2
else:
    number = int(fb3) + 1
    
if number % 15 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print(number)
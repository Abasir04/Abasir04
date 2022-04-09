# if divisible by 3 print fizz by 5 print buzz by 3 and 5 print fizzbuzz
i = 1
while i < 101:
    if (i % 3 == 0) and (i % 5 != 0):
        print("fizz")
    elif (i % 3 != 0) and (i % 5 == 0):
        print("buzz")
    elif (i % 5 == 0) and (i % 3 == 0):
        print("fizz buzz")
    else:
        print(i)
    i += 1

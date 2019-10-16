def increment(a, b):
    a = a + b
    return a

a = int(input("Num1:"))
b = int(input("Num2:"))
c = int(input("num3:"))

a = increment(a, 5)
b = increment(b, 5)
c = increment(c, 5)

print("a="+str(a))
print(b)
print(c)

def   add_two_numbers():
    number1  =   1
    number2  =   2
    answer  =  number1  +  number2
    print "{} plus {} is {}" .format(number1, number2, answer)

add_two_numbers()


my_favourite_cats = ["cleo", "fluffy", "softy"]
print my_favourite_cats[1]

def   add_two_numbers_from_args(number1, number2):
    answer  =  number1  +  number2
    print  "{} plus {} is {}" .format(number1, number2, answer)
add_two_numbers_from_args( 5 , 10 )

a = [3,5,6,11,13,17,19,23,29]
for num in a:
    print(str(num) + "is a prime")

def add_two_numbers_and_return_value():
    number1 = 1
    number2 = 2
    answer =number1 + number2
    return answer
returned_value=add_two_numbers_and_return_value()
print returned_value

1 == 1
1 == 0
(1 == 1) and (1 == 0)

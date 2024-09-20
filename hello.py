input_value = ''
while input_value != 'q':
    input_value = (input("type q for quite "))
    if eval(input_value) % 2 == 0:
        print("the number is even")

    else:
        print("the number is odd")

    print(input_value)
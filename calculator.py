"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
is_calculation_over = False
while not is_calculation_over:

    user_input = input("Please enter your equation > ")
    tokens = user_input.split(' ')

    token = tokens[0]
    #case when the input is "q"
    if token == "q" and len(tokens) == 1:
       is_calculation_over = True
    #all other cases
    else:
        #cases when only one parameter needed
        token1 = int(tokens[1])
        if token == 'cube':
            result = cube(token1)
            print(result)
        elif token == 'square':
            result = square(token1)
            print(result)
        else:
             #cases when both parameters are needed
            token2 = int(tokens[2])

            if token == '+':
                result = add(token1,token2)
                print(result)

            elif token == '-':
                result = subtract(token1,token2)
                print(result)

            elif token == '/':
                result = divide(token1,token2)
                print(result)
            
            elif token == '*':
                result = multiply(token1,token2)
                print(result)
            
            elif token == 'pow':
                result = pow(token1,token2)
                print(result)

            elif token == 'mod':
                result = mod(token1,token2)
                print(result)
            else:
                print("Wrong input! Try again! ")
           
                



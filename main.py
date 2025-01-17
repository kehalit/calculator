
def calculate(user_input):
    #This function performs the core arithmetic operations.

   #checking if the user inputs only single digit (3 characters) and 4 operators only
    if len(user_input) == 3 and user_input[0].isdigit() and user_input[2].isdigit() and user_input[1] in "+,-,*,/,~":

    #extract numbers and converting in to integer and extract operators
        num1 = int(user_input[0])
        num2 = int(user_input[2])
        operator = user_input[1]

    # doing the calculations
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return  num1 - num2
        elif operator == '*':
            return  num1 * num2
        elif operator == '/' :
            if num2 == 0:
                return "Error: Division by zero "
            return  num1 / num2
        elif operator == 'exit':
            quotient = num1 // num2
            remainder = num1 % num2
            return quotient , remainder
    else:
        return 'Invalid input please enter only single digit number.'


def main():
    #This function is the entry point of the program and handles user interaction.

    print("Welcome to the Python calculator!")
    calculations_number = int(input("how many calculations you want to do? "))

    # Loop through the number of calculations inserted by user
    for i in range(calculations_number):
        user_input = input("What do you want to calculate? ")
        result = calculate(user_input)

    #here needed to use isinstance for ~ operator
        if isinstance(result, tuple):
            quotient , remainder = result
            print (f'The answer is:{quotient} ')
            print (f'The remainder is: {remainder}')
        else:
            print(f"The answer is {result}")

if __name__ == "__main__": #dunder-main idiom
    main()
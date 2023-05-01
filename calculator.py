while True:
    try:
        #numbers
        number1 = float(input("First Number: "))
        number2 = float(input("Second Number: "))
        options = input("What action do you want to do? (+, -, *, /): ")

        #options
        if options == "+":
            print(number1 + number2)
        elif options == "-":
            print(number1 - number2)
        elif options == "*":
            print(number1 * number2)
        elif options == "/":
            print(number1 / number2)
        else:
            print("Error,please enter the correct command!")
        
        #exit
        choice = input("Exit! (y/n): ")
        if choice.lower() == "y":
            break

    except ValueError:
        print("Error,please enter the correct command!")

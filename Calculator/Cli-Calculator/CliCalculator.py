def add(_input_number1, _input_number2, choice="+"):
    return _input_number1 + _input_number2

def subtract(_input_number1, _input_number2, choice="-"):
    return _input_number1 - _input_number2

def multiply(_input_number1, _input_number2, choice="*"):
    return _input_number1 * _input_number2

def divide(_input_number1, _input_number2, choice="/"):
    if _input_number2 != 0:
        return _input_number1 / _input_number2
    else:
        print("float division by zero")

def power(_input_number1, _input_number2, choice="^"):
    return _input_number1 ** _input_number2

def remainder(_input_number1, _input_number2, choice="%"):
    return _input_number1 % _input_number2



def select_op(choice):

    if choice == '#':
        return -1
    elif choice == '$':
        return 0
    elif (choice in ('+','-','*','/','^','%','#','$')):
        while(True):
            number1 = str(input("Enter first number: "))
            print(number1)
            if number1.endswith('$'):
                return 0
            if number1.endswith('#'):
                return -1

            try:
                _input_number1 = float(number1)
                break
            except:
                print("Not a valid number,please enter again")
                continue

        while(True):
            number2 = str(input("Enter second number: "))
            print(number2)
            if number2.endswith('$'):
                return 0
            if number2.endswith('#'):
                return -1

            try:
                _input_number2 = float(number2)
                break
            except:
                print("Not a valid number,please enter again")
                continue
    
        
        if choice == "+":
            output = add(_input_number1, _input_number2)
        elif choice == '-':
            output = subtract(_input_number1, _input_number2)
        elif choice == '*':
            output = multiply(_input_number1, _input_number2)
        elif choice == '/':
            output = divide(_input_number1, _input_number2)
        elif choice == '^':
            output = power(_input_number1, _input_number2)
        elif choice == '%':
            output = remainder(_input_number1, _input_number2)
        else:
            print("Something Went Wrong")
        print(_input_number1, choice ,_input_number2, "=", output)
    else:
        print("Unrecognized operation")


#End the select_op(choice) function here
#-------------------------------------
#This is the main loop. It covers Task 1 (Section 1)
#YOU DO NOT NEED TO CHANGE ANYTHING BELOW THIS LINE
while True:
  print("Select operation.")
  print("Add      : + ")
  print("Subtract : - ")
  print("Multiply : * ")
  print("Divide   : / ")
  print("Power    : ^ ")
  print("Remainder: % ")
  print("Terminate: # ")
  print("Reset    : $ ")
  

  # take input from the user
  choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
  print(choice)
  if(select_op(choice) == -1):
    #program ends here
    print("Done. Terminating")
    exit()

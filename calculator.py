plus = '+'
minus = '-'
multiplication = '*'
division = '/'
option = input("Choose your option (+, -, *, /): ")
if option != plus and option != minus and option != multiplication and option != division:
   print("Chosen option is wrong!")
   exit()
first_num = int(input("Choose your first number: "))
second_num = int(input("Choose your second number: "))
if option == plus:
    print("Your result is:", first_num + second_num)
elif option == minus:
    print("Your result is:", first_num - second_num)
elif option == multiplication:
    print("Your result is:", first_num * second_num)
elif option == division and second_num == 0:
    print("Division by 0 is impossible!")
    exit()
elif option == division:
    print("Your result is:", first_num / second_num)
else:
    print("What a wonderful world!")

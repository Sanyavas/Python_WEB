result = None
operand = None
operator = None
wait_for_number = True
while True:
    user_input = input(">>>")
    
    if user_input == '=':
        print(result)
        break
    
    if wait_for_number:
        try:
            operand = int(user_input)
            wait_for_number = False
            if not result:
                continue
        except ValueError:
            print('Not number')
            continue
    
    if not result:
        result = operand
    
    if operator == '+':
        result += operand
        operator = None
        continue
    
    if operator == '-':
        result -= operand
        operator = None
        continue
    
    if operator == '*':
        result *= operand
        operator = None
        continue
    
    if operator == '/':
        result /= operand
        operator = None
        continue
    
    if not wait_for_number:
        try:
            if user_input in ('+', '-', '/', '*'):
                operator = user_input
                wait_for_number = True
            else:
                raise ValueError
        except ValueError:
            print('Not operator')
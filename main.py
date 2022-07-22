from Calculator.operations import Operations

operations = Operations()

while True:
    print('**********CALCULADORA**********')
    num1 = int(input('Primeiro número: '))
    operator = input('Operador: ')
    num2 = int(input('Segundo número: '))

    if operator == '+':
        print(num1, "+", num2, "=", operations.sum(num1, num2))
    elif operator == '-':
        print(num1, "-", num2, "=", operations.subtract(num1, num2))
    elif operator == '*':
        print(num1, "*", num2, "=", operations.multiply(num1, num2))
    elif operator == '/':
        print(num1, "/", num2, "=", operations.divide(num1, num2))

    continue_calculation = input('Deseja realizar outra operação? (sim/não)')
    print(' ')
    if continue_calculation == 'não':
        break









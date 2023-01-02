print('Добро пожаловать в калькулятор!!!')
operation_num = 1
last = 0

try:
    while True:
        try:

            if operation_num == 1:
                a = int(input('Введите первое число: '))
                operator = input('Введите знак: ')
                b = int(input('Введите второе число: '))

                if operator == '+':
                    last += a + b
                    print(last)
                    operation_num += 1

                elif operator == '-':
                    last += a - b
                    print(last)
                    operation_num += 1

                elif operator == '*':
                    last += a * b
                    print(last)
                    operation_num += 1

                elif operator == '/':
                    try:
                        last += a / b
                        print(last)
                        operation_num += 1

                    except ZeroDivisionError:
                        print('На ноль делить нельзя!')

                elif operator == 'end':
                    break

            else:
                print('Ваш результат: {0}'.format(last))
                operator = input('Введите знак: ')
                b = int(input('Введите второе число: '))

                if operator == '+':
                    last += last + b
                    print(last)

                elif operator == '-':
                    last += last - b
                    print(last)

                elif operator == '*':
                    last += last * b
                    print(last)

                elif operator == '/':
                    try:
                        last += last / b
                        print(last)

                    except ZeroDivisionError:
                        print('На ноль делить нельзя!')
                elif operator == 'end':
                    break

        except ValueError:
            print('Вы ввели неверное значение!')

except KeyboardInterrupt:
    print('\nДо свидания!')

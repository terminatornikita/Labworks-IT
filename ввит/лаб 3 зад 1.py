def read_file():
    file_name = input('Введите имя файла для чтения: ')
    print('1) Прочитать весь файл сразу.')
    print('2) Прочитать файл построчно.')
    n = input('Введите 1 или 2 для выбора метода чтения: ')
    try:
        if n == '1':
            with open(file_name, 'r') as file:
                print('Чтение файла целиком:')
                content = file.read()
                print(content)
        elif n == '2':
            with open(file_name, 'r') as file:
                print('Чтение файла построчно:')
                for line in file:
                    print(line, end='')
        else:
            print('Неверный режим чтения')
    except FileNotFoundError:
        print(f"Файл '{file_name}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


read_file()

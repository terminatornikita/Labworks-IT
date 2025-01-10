def write_to_file():
    user_text = input('Введите текст для записи в файл: ')
    with open('user_input.txt', 'a') as file:
        file.write(user_text + '\n')
    print('Текст успешно записан в файл user_input.txt.')
    
write_to_file()

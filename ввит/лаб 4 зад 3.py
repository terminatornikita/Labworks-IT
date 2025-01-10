from packet.privetstvie import greet
import packet.chisla
import packet.stroki

n= input("Введите имя: ")
print (f'Здравствуйте, {n}!')

a = int(input('Введите первое число:'))
b = int(input('Введите второе число:'))
sum_result = packet.chisla.sum_numbers(a, b)
difference_result = packet.chisla.difference_numbers(a, b)
multiply_result = packet.chisla.multiply_numbers(a, b)
divmod_result = packet.chisla.divmod_numbers(a, b)
print(f"Сумма = {sum_result}")
print(f"Разность = {difference_result}")
print(f"Произведение = {multiply_result}")
print(f"Частное = {divmod_result}")

t = input('Напишите что-нибудь: ')
reversed_text = packet.stroki.reverse_string(t)
print(f"Магия: {reversed_text}")




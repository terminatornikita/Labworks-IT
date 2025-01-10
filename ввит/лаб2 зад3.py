n = int(input('Введите число:'))
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
        else:
            return True 
if is_prime(n):
    print(f"{n} простое число")
else:
    print(f"{n} не простое число")
        



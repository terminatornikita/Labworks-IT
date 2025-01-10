a = int(input('Текущее значение радиуса: '))
b = input('Хотите изменить значение радиуса? (да/нет)')
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius
    
    def set_radius(self, new_radius):
        self.radius = new_radius
circle_instance = Circle(a)  
print("Исходный радиус:", circle_instance.get_radius())

if b == "да":
    c = int(input('Насколько хотите изменить значение?'))
    circle_instance.set_radius(c)  
    print("Новый радиус:", circle_instance.get_radius())



class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def get_info(self):
        return f"Имя: {self.name}, ID: {self.emp_id}"

class Manager(Employee):
    def __init__(self, name, emp_id, department):
        super().__init__(name, emp_id)
        self.department = department

    def manage_project(self, project_name):
        return f"Менеджер {self.name} управляет проектом: {project_name}"

    def get_info(self):
        return f"{super().get_info()}, Отдел: {self.department}"

class Technician(Employee):
    def __init__(self, name, emp_id, specialization):
        super().__init__(name, emp_id)
        self.specialization = specialization

    def perform_maintenance(self, task):
        return f"Техник {self.name} выполняет техническое обслуживание: {task}"

    def get_info(self):
        return f"{super().get_info()}, Специализация: {self.specialization}"
class TechManager(Manager, Technician):
    def __init__(self, name, emp_id, department, specialization):
        Manager.__init__(self, name, emp_id, department)
        Technician.__init__(self, name, emp_id)
        self.team = []

    def add_employee(self, employee):
        self.team.append(employee)

    def get_team_info(self):
        return "\n".join([employee.get_info() for employee in self.team])

    def manage_project(self, project_name):
        return f"Тех. менеджер {self.name} управляет проектом: {project_name}"

    def perform_maintenance(self, task):
        return f"Тех. менеджер {self.name} выполняет техническое обслуживание: {task}"

# Создание сотрудников    
employee1 = Employee("Иван Иванов", 1001)
manager1 = Manager("Анна Смирнова", 1002, "Маркетинг")
technician1 = Technician("Петр Петров", 1003, "Электроника")
tech_manager1 = TechManager("Мария Кузнецова", 1004, "ИТ", "Сетевые технологии")

# Добавление сотрудников в команду тех.менеджера
tech_manager1.add_employee(employee1)
tech_manager1.add_employee(manager1)
tech_manager1.add_employee(technician1)

# Вывод информации о сотрудниках и команде
print(employee1.get_info())
print(manager1.get_info())
print(technician1.get_info())
print(tech_manager1.get_team_info())
print(tech_manager1.manage_project("Проект А"))
print(tech_manager1.perform_maintenance("Обслуживание серверов"))


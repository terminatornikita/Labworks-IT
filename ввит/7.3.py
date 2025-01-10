class Technician(Employee):
    def __init__(self, name, emp_id, specialization):
        super().__init__(name, emp_id)
        self.specialization = specialization

    def perform_maintenance(self, task):
        return f"Техник {self.name} выполняет техническое обслуживание: {task}"

    def get_info(self):
        return f"{super().get_info()}, Специализация: {self.specialization}"

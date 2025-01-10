class TechManager(Manager, Technician):
    def __init__(self, name, emp_id, department, specialization):
        Manager.__init__(self, name, emp_id, department)
        Technician.__init__(self, name, emp_id, specialization)
        self.team = []

    def add_employee(self, employee):
        self.team.append(employee)

    def get_team_info(self):
        return "\n".join([employee.get_info() for employee in self.team])

    def manage_project(self, project_name):
        return f"Тех. менеджер {self.name} управляет проектом: {project_name}"

    def perform_maintenance(self, task):
        return f"Тех. менеджер {self.name} выполняет техническое обслуживание: {task}"

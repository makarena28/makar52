class Employee:

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_info(self):
        return f'{self.name}, {self.id}'


class Manager(Employee):

    def __init__(self, name, id, department):
        Employee.__init__(self, name, id)
        self.department = department

    def manage_project(self):
        return f'{self.name} управляет проектом в отделе {self.department}'


class Technician(Employee):
    def __init__(self, name, id, specialization):
        Employee.__init__(self, name, id)
        self.specialization = specialization

    def perform_maintenance(self):
        return f'{self.name} выполняет обслуживание по специальности {self.specialization}'


class TechManager(Manager, Technician):
    def __init__(self, name, id, department, specialization):
        Manager.__init__(self, name, id, department)
        Technician.__init__(self, name, id, specialization)
        self.team = []

    def add_employee(self, employee):
        self.team.append(employee)

    def get_team_info(self):
        return [employee.get_info() for employee in self.team]


employee1 = Employee('Egor', 1)
employee2 = Employee('Kirill', 2)
employee3 = Employee('Alice', 3)
for i in [employee1, employee2, employee3]:
    print(i.get_info())

manager1 = Manager('Vladlen', 4, 'IT')

technician1 = Technician('Alexandr', 5, 'programmer')

tech_manager1 = TechManager('Georgiy', 6, 'IT', 'Senior_programmer')

tech_manager1.add_employee(employee1)
tech_manager1.add_employee(employee2)
tech_manager1.add_employee(employee3)
print(tech_manager1.get_team_info())





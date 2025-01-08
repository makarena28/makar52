class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_info(self):
        return f"Name: {self.name}, ID: {self.id}"


class Manager(Employee):
    def __init__(self, name, id, department):
        super().__init__(name, id)
        self.department = department

    def manage_project(self):
        return f"{self.name} is managing projects in {self.department} department."


class Technician(Employee):
    def __init__(self, name, id, specialization):
        super().__init__(name, id)
        self.specialization = specialization

    def perform_maintenance(self):
        return f"{self.name} is performing maintenance in {self.specialization}."


class TechManager(Manager, Technician):
    def __init__(self, name, id, department, specialization):
        Manager.__init__(self, name, id, department)
        Technician.__init__(self, name, id, specialization)
        self.team = []

    def add_employee(self, employee):
        self.team.append(employee)

    def get_team_info(self):
        team_info = ""
        for employee in self.team:
            team_info += employee.get_info() + "\n"
        return team_info


employee1 = Employee("John Doe", 1)
manager1 = Manager("Jane Smith", 2, "Marketing")
technician1 = Technician("Mike Johnson", 3, "IT")
tech_manager1 = TechManager("Alice Brown", 4, "Development", "Engineering")


print(employee1.get_info())
print(manager1.manage_project())
print(technician1.perform_maintenance())

tech_manager1.add_employee(employee1)
tech_manager1.add_employee(manager1)
tech_manager1.add_employee(technician1)
print(tech_manager1.get_team_info())

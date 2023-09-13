from person_class import *
class Employee(Person):
	def __init__(self,f_name,l_name,age,employee_code,salary):
		super().__init__(f_name,l_name,age)
		self.employee_code = employee_code 
		self.salary = salary

	def all_info(self):
		super().info_display()
		print(f"employee_code is:{self.employee_code}")
		print(f"salary is :{self.salary}")
if __name__ == "__main__":
	empl1 = Employee("mina","rezaee",25,"123456",10000)
	print(empl1.salary)
	empl1.all_info()

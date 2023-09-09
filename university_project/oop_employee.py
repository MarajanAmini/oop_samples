class Employee:
	def __init__(self,f_name,l_name,age,employee_code,salary):
		self.f_name = f_name
		self.l_name = l_name
		self.age = age
		self.employee_code = employee_code
		self.salary = salary

	def info_display(self):
		print(f"first name is :{self.f_name}")
		print(f"last name is :{self.l_name}")
		print(f"age is :{self.age}")
	def all_info(self):
		self.info_display()
		print(f"employee_code is:{self.employee_code}")
		print(f"salary is :{self.salary}")
"""empl1 = Employee("mina","rezaee",25,"123456",10000)
print(empl1.salary)
empl1.all_info()"""
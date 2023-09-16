from employee_class_library import *
from user_class_lib import *
class Library:
	def __init__(self):
		self.employees = []
		self.users = []
	def find_index_employee(self,employee_code):
		for i,j in enumerate(self.employees):
			if  j.employee_code == employee_code :
				return i
		return -1
	def find_index_user(self,user_code):
		for i,j in enumerate(self.users):
			if j.user_code == user_code :
				return i
		return -1
	def add_user (self,user):
		ind = self.find_index_user(user.user_code)
		if ind == -1 :
			self.users.append(user)
		else:
			print("this code exist !")
	def add_employee(self,employee):
		ind = self.find_index_employee(employee.employee_code)
		if ind == -1 :
			self.employees.append(employee)
		else:
			print("this code exist!")
	def display_employee(self):
		for i in self.employees:
			print(type(i))
			i.all_info()
		
	def display_user(self):
		for i in self.users:
			print(type(i))
			i.all_info()



	def edit_user (self,user_code):
		ind = self.find_index_user(user_code)
		if ind != -1:
			new_f_name= input("new name:") 
			new_l_name = input("new l_name:")
			new_age = input(" new age:")
			self.users[ind].f_name = new_f_name or self.users[ind].f_name
			self.users[ind].l_name = new_l_name or self.users[ind].l_name
			self.users[ind].age = int(new_age or self.users[ind].age)
		
		else:
			print("there is no user!")
	def edit_employee (self,employee_code):
		ind = self.find_index_employee(employee_code)
		if ind != -1:
			new_f_name= input("new name:") 
			new_l_name = input("new l_name:")
			new_salary = input("new salary:")
			self.employees[ind].f_name = new_f_name or self.employees[ind].f_name
			self.employees[ind].l_name = new_l_name or self.employees[ind].l_name
			self.employees[ind].salary = int(new_salary or self.employees[ind].salary) 
		else:
			print("there is no employee!")
	def search_user(self,user_code):
		ind = self.find_index_user(user_code)
		if ind != -1:
			self.users[ind].all_info()
		else:
			print(" not foand !!")
	def search_employee(self,employee_code):
		ind = self.find_index_employee(employee_code)
		if ind != -1:
			self.employees[ind].all_info()
		else:
			print(" not foand!!")

	def remove_user(self,user_code):
		ind = self.find_index_user(user_code)
		if ind != -1 :
			self.users.pop(ind)
			print('removed!')
		else:
			print("there is no this user")
	def remove_employee(self,employee_code):
		ind = self.find_index_employee(employee_code)
		if ind != -1 :
			self.employees.pop(ind)
		else:
			print(' there is no employee!')

if __name__ == "__main__" :
	Library1 = Library()
	user1 = User("ali","rezaee",21,"1234")
	Library1.add_user(user1)
	Library1.display_user()
	print(user1.__dict__)
	empl1 = Employee("mina","moradi",29,"123456",20000)
	Library1.add_employee(empl1)
	Library1.display_employee()
	print(empl1.__dict__)



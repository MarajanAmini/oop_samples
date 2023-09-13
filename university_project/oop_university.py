from oop_student import *
from oop_employee import *
class University:
	def __init__(self):
		self.employees = []
		self.students = []
	def find_index_employee(self,employee_code):
		for i,j in enumerate(self.employees):
			if  j.employee_code == employee_code :
				return i
		return -1
	def find_index_student(self,student_code):
		for i,j in enumerate(self.students):
			if j.student_code == student_code :
				return i
		return -1
	def add_student (self,student):
		ind = self.find_index_student(student.student_code)
		if ind == -1 :
			self.students.append(student)
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
			i.all_info()
		
	def display_students(self):
		for i in self.students:
			i.all_info()


	def edit_student (self,student_code):
		ind = self.find_index_student(student_code)
		if ind != -1:
			new_f_name= input("new name:") 
			new_l_name = input("new l_name:")
			new_score = input("new score:")
			new_age = input(" new age:")
			self.students[ind].f_name = new_f_name or self.students[ind].f_name
			self.students[ind].l_name = new_l_name or self.students[ind].l_name
			self.students[ind].score = float(new_score or self.students[ind].score)
			self.students[ind].age = int(new_age or self.students[ind].age)
		
		else:
			print("there is no Student!S")
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
	def search_student(self,student_code):
		ind = self.find_index_student(student_code)
		if ind != -1:
			self.students[ind].all_info()
		else:
			print(" not foand !!")
	def search_employee(self,employee_code):
		ind = self.find_index_employee(employee_code)
		if ind != -1:
			self.employees[ind].all_info()
		else:
			print(" not foand!!")

	def remove_student(self,student_code):
		ind = self.find_index_student(student_code)
		if ind != -1 :
			self.students.pop(ind)
			print('removed!')
		else:
			print("there is no this Student")
	def remove_employee(self,employee_code):
		ind = self.find_index_employee(employee_code)
		if ind != -1 :
			self.employees.pop(ind)
		else:
			print(' there is no employee!')

if __name__ == "__main__" :
	uni1 = University()
	stu1 = Student("ali","rezaee",21,19,"1234")
	uni1.add_student(stu1)
	uni1.display_students()




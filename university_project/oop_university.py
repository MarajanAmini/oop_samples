from oop_student import *
from oop_employee import *
class university:
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
university1 = university()
while True:
	answer = input("you can select:add,edit,search,remove,display_students,exit:")
	if answer == "add":
		select = input("stud or empl:")
		if select == "stud":
			student_code =input("enter a student_code:")
			f_name = input("name of student :")
			l_name = input("last name of student:")
			score = float(input ("score of student :"))
			age = int(input("age of student:"))
			stu1 = Student(f_name,l_name,age,score,student_code)
			university1.add_student(stu1)
		elif select == "empl":
			employee_code =input("enter a employee_code:")
			f_name = input("name of employee :")
			l_name = input("last name of employee:")
			salary = int(input ("salary of employee :"))
			age = int(input("age of employee:"))
			empl1 = Employee(f_name,l_name,age,employee_code,salary)
			university1.add_employee(empl1)

		else:
			print("not faond this option!!")
	elif answer == "edit":
		answer = input("stu or empl:")
		if answer == "stu":
			code_student = input(" a code :")
			university1.edit_student(code_student)
		elif answer == "empl":
			employee_code = input("a code:")
			university1.edit_employee(employee_code)



	elif answer == "remove":
		answer = input("student or employee:")
		if answer == "student":
			code_student = input(" a code :")
			university1.remove_student(code_student)

		elif answer == "employee":
			employee_code = input(" a code :")
			university1.remove_employee(employee_code)

	elif answer == "display":
		answer = input("student or employee:")
		if answer == "student":
			university1.display_students()
		elif answer == "employee":
			university1.display_employee()


	elif answer == "search":
		answer = input("stu or empl:")
		if answer == "stu":
			student_code = input("a code:")
			university1.search_student(student_code)
		elif answer == "empl":
			employee_code = input("a code:")
			university1.search_employee(employee_code)
	elif answer == "exit":
		break
	elif answer == "":
		pass

	else:
		print("not faond this option!!")





			





















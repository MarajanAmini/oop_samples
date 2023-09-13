from oop_university import *
def main():
	university1 = University()
	while True:
		answer = input("you can select:add,edit,search,remove,display_students,exit:")
		if answer == "add":
			select = input("student or employee:")
			if select == "student":
				student_code =input("enter a student_code:")
				f_name = input("name of student :")
				l_name = input("last name of student:")
				score = float(input ("score of student :"))
				age = int(input("age of student:"))
				stu1 = Student(f_name,l_name,age,score,student_code)
				university1.add_student(stu1)
			elif select == "employee":
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
			answer = input("student or employee:")
			if answer == "student":
				code_student = input(" a code :")
				university1.edit_student(code_student)
			elif answer == "employee":
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
			answer = input("student or employee:")
			if answer == "student":
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


if __name__ == "__main__" :
	main()





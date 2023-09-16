from library_class import *
def main():
	library1 = Library()
	while True:
		answer = input("you can select:add,edit,search,remove,display,exit:")
		if answer == "add":
			select = input("user or employee:")
			if select == "user":
				user_code =input("enter a user_code:")
				f_name = input("name of user :")
				l_name = input("last name of user:")
				age = int(input("age of user"))
				user1 = User(f_name,l_name,age,user_code)
				library1.add_user(user1)
			elif select == "employee":
				employee_code =input("enter a employee_code:")
				f_name = input("name of employee :")
				l_name = input("last name of employee:")
				salary = int(input ("salary of employee :"))
				age = int(input("age of employee:"))
				empl1 = Employee(f_name,l_name,age,employee_code,salary)
				library1.add_employee(empl1)

			else:
				print("not found this option!!")
		elif answer == "edit":
			answer = input("user or employee:")
			if answer == "user":
				code_user = input(" a code :")
				library1.edit_user(code_user)
			elif answer == "employee":
				employee_code = input("a code:")
				library1.edit_employee(employee_code)
			else:
				print("command not found!!")				
		elif answer == "remove":
			answer = input("user or employee:")
			if answer == "employee":
				employee_code = input(" a code:")
				library1.remove_employee(employee_code)
			elif answer == "user":
				user_code = input("a code:")
				library1.remove_user(user_code)
			else:
				print("command not found!!")
		elif answer == "search":
			answer = input("user or employee:")
			if answer == "employee":
				employee_code = input(" a code:")
				library1.search_employee(employee_code)
			elif answer == "user":
				user_code = input(" a code:")
				library1.search_user(user_code)
			else:
				print("command not found!!")
		elif answer == "display":
			answer = input("user or employee:")
			if answer == "user":
				library1.display_user()
			elif answer == "employee":
				library1.display_employee()
			else:
				print("command not found!!")
		elif answer == "exit":
			break
		elif answer == "":
			pass
		else:
			print("command not found !!")







if __name__ == "__main__":
	main()

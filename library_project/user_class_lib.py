from person_class import *
class User (Person):
	def __init__(self,f_name,l_name,age,user_code):
		super().__init__(f_name,l_name,age)
		self.user_code = user_code
	def all_info(self):
		super().info_display()
		print(f"user_code is:{self.user_code}")

if __name__ == "__main__":
	user1 = User ("sara","momeni",27,"12345")
	print(user1.l_name)
	user1.info_display()	

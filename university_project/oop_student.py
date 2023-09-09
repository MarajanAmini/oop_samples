class Student :
	def __init__(self,f_name,l_name,age,score,student_code):
		self.f_name = f_name
		self.l_name = l_name
		self.age = age
		self.student_code = student_code
		self.score = score

	def info_display(self):
		print(f"first name is :{self.f_name}")
		print(f"last name is :{self.l_name}")
		print(f"age is :{self.age}")
	def all_info(self):
		self.info_display()
		print(f"student_code is:{self.student_code}")
		print(f"score is :{self.score}")
"""stu1 = Student("sara","shirazi",23,19,"12345")
print(stu1.student_code)
stu1.info_display()
stu1.all_info()"""
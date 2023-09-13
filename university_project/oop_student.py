from person_class import *
class Student (Person):
	def __init__(self,f_name,l_name,age,student_code,score):
		super().__init__(f_name,l_name,age)
		self.student_code = student_code
		self.score = score

	def all_info(self):
		super().info_display()
		print(f"student_code is:{self.student_code}")
		print(f"score is :{self.score}")
if __name__ == "__main__":
	stu1 = Student("sara","shirazi",23,19,"12345")
	print(stu1.l_name)
	stu1.info_display()

from abc import ABC,abstractmethod
class Person(ABC):
	def __init__(self,f_name,l_name,age):
		self.f_name = f_name
		self.l_name = l_name
		self.age = age
	def info_display(self):
		print(f"first name is :{self.f_name}")
		print(f"last name is :{self.l_name}")
		print(f"age is :{self.age}")
	@abstractmethod
	def all_info(self):
		pass
"""if __name__ == "__main__":
	per1 = Person("sara","amini",21)
	print(per1.age)"""
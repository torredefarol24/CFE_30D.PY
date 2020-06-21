class Animal:
	noise = "rrr"
	color = "red"
	
	def hello(self):
		print("hey")
	

	def make_noise(self):
		print(f"{self.noise}")


	def set_noise(self, new_noise):
		self.noise = new_noise
		return self.noise

	def get_color(self):
		print(f"{self.color}")


	def set_color(self, new_color):
		self.color = new_color
		return self.color


class Wolf(Animal):
	noise = "grwww"

class BabyWold(Wolf):
	color = "yellow"
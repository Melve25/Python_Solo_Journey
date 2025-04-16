class Monitor:
	def __init__(self, brand:str, resolution:str) -> None:
		self.brand = brand
		self.resolution = resolution
		self.turned_on: bool = False

	def turn_on(self) -> None:
		if self.turned_on:
			print(f"Monitor ({self.brand}) is already turned on.")
		else:
			self.turned_on = True
			print(f"Monitor ({self.brand}) is now turned on.")
				
	def turn_off(self) -> None:
		if self.turned_on:
			self.turned_on = False
			print(f"Monitor ({self.brand}) is now turned off.")
		else:
			print(f"Monitor ({self.brand}) is already turned off.")

	def choose_chanel(self, chanel: int) -> None:
		if self.turned_on:
			print(f"Канал {chanel} включен")
		else:
			print(f"Монитор не реагирует, он выключен")

	def __add__(self, other): 
		return f"{self.brand} + {other.brand}"
	
	def __str__(self) -> str: 
		return f"{self.brand} + (Resolution: {self.resolution})"
	
	def __repr__(self) -> str: 
		return f"class Monitor: (brand='{self.brand}' resolution='{self.resolution}')"
		
sony: Monitor = Monitor("sony", "1920x1080")
print(sony.brand)
print(sony.resolution)

huion: Monitor = Monitor("huion", "1280x720")
print(huion.brand)
print(huion.resolution) 

sony.turn_off()
sony.turn_on()

huion.choose_chanel(2)
huion.turn_on()
huion.choose_chanel(2)

print(sony + huion)
print(sony)

print(repr(sony))
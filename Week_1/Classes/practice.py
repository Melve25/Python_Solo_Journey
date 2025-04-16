class Device:
	def __init__(self, name:str) -> None:
		self.name: str = name
		self.status: bool = False
	
	def turn_on(self) -> None:
		if self.status:
			print("turned on already")
		else:
			self.status = True
			print("Turned on")

	def turn_off(self) -> None:
		if self.status:
			self.status = False
			print("turned off")
		else:
			
			print("Turned off already")

	def __str__(self) -> str:
		return f"name: {self.name}, status: {self.status}"

class Light(Device):
	def __init__(self, name: str) -> None:
		super().__init__(name)
		self.brightness = 0

	def set_brightness(self, value: int) -> None:
		if self.status:
			if value > 100:
				self.brightness = 100
			elif value < 0:
				self.brightness = 0
			else:
				self.brightness = value
			print(f"brightness: {self.brightness}")
		else:
			print("Please turn on device")


class Thermostat(Device):
	def __init__(self, name) -> None:
		super().__init__(name)
		self.temperature = 22

	def set_temperature(self, temperature:int) -> None:
		self.temperature = temperature
		print(f"temperature = {self.temperature}")

class Door(Device):
	def __init__(self, name) -> None:
		super().__init__(name)
		self.is_locked = True

	def lock(self) -> None:
		if self.is_locked:
			print("locked already")
		else:
			self.is_locked = True
			print("locked")

	def unlock(self) -> None:
		if self.is_locked:
			self.is_locked = False
			print("unlocked")
		else:	
			print("unlocked already")

class SmartHome:
	def __init__(self) -> None:
		self.all_devices: list = []
	
	def add_device(self, device) -> None:
		self.all_devices.append(device)
		print(f"device {device.name} added")

	def show_status(self) -> None:
		for device in self.all_devices:
			print(f"device: {device.name}, status: {device.status}")

	def turn_off_all(self) -> None:
		for device in self.all_devices:
			device.turn_off()
			print(f"device: {device.name}, status: {device.status}")

home: SmartHome = SmartHome()

lamp: Light = Light("bulb")
thermo: Thermostat = Thermostat("thermo")
door: Door = Door("door")
			
home.add_device(lamp)
home.add_device(thermo)
home.add_device(door)

lamp.turn_on()
lamp.set_brightness(70)

thermo.set_temperature(24)

door.lock()

home.show_status()
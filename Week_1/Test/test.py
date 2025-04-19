from functools import wraps

def logger(func):
	def wrapper(*args, **kwargs):
		total_price = func(*args, **kwargs)
		print(f"[LOG] Function name: {func.__name__} \n[LOG] Arguments: {kwargs} \n[LOG] Return is: {total_price}")
		return total_price
	return wrapper

def authorize(role: str):
	def decorator(func):
		@wraps(func)
		def wrapper(*args, **kwargs):
			if role.lower().strip() == kwargs.get('role'):
				return func(*args, **kwargs)
			else:
				return None
		return wrapper
	return decorator

class Client:
	def __init__(self, name: str, email: str) -> None:
		self.name = name 
		self.email = email
	def __str__(self) -> str:
		return f"Client name: {self.name}, Email: {self.email}"
	
	def __repr__(self) -> str:
		return f"class {Client.__name__}(name = '{self.name}', email='{self.email}')"

	def __eq__(self, other) -> bool:
		return self.email == other.email
	
class Order:
	def __init__(self, *args: tuple) -> None:
		self.products = args

	def total(self) -> int:
		total = 0
		for product in self.products:
			total += product[1]

		return total
	
	def __len__(self) -> int:
		return len(self.products)
	
	def __str__(self) -> str:
		order: str = ""

		for product in range(len(self.products)):
			order += f"{product+1}. Product: {self.products[product][0]}, price: {self.products[product][1]} \n"

		return order

class OrderProcessor:

	@logger
	@authorize(role="manager")
	def process_order(self, order: Order, **kwargs) -> float:
		discount = kwargs.get('discount')
		tax = kwargs.get('tax')

		final_price =  tax(discount(order.total()))
		return final_price
			


client1 = Client("Андрей", "andrei@example.com")
order1 = Order(("Ноутбук", 1000), ("Мышь", 50), ("Коврик", 10))

processor = OrderProcessor()
final_price = processor.process_order(order1, discount=lambda x: x * 0.9, tax=lambda x: x * 1.05, role="manager")

print(f"Итоговая сумма: {final_price}")

import time

def add_some_text(func):
	def wrapper():
		print(123)
		func()
	return wrapper
	
@add_some_text
def print_name():
	print("hello Max")
	
print_name()

def count_time(func):
	def wrapper():
		t1 = time.time()
		func()
		t2 = time.time()-t1
		print(f"It took {t2} seconds")
	return wrapper
	
@count_time
def do_something():
	time.sleep(.2)

do_something()


def mult_result(func):
	def wrapper(*args, **kwargs):
		print("started")
		val = func(*args, **kwargs) * 2
		print("ended")
		return val
		
	return wrapper

@mult_result
def add(x, y) -> int:
	return x + y

print(add(4, 2))


def log(level):
	def decorator(func):
		def wrapper(*args, **kwargs):
			print(f"[{level.upper()}] Вызов функции: {func.__name__}")
			return func(*args, **kwargs)
		return wrapper
	return decorator
	
@log("owner")
def greet(name):
    print(f"Привет, {name}!")

greet("Max")
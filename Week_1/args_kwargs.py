# ex1
nums = [1, 2, 3, 6, 12, 10]
print(nums)
print(*nums)

# ex2
def order_pizza(size):
	print(f"Order a {size} pizza.")
	
order_pizza("large")

# ex3
def order_pizza(size, *args):
    print(f"Order a {size} pizza with the following toppings: {args}")
    for topping in args:
          print(topping)
	
order_pizza("large", "pepperoni", "olives", "cheese")

# ex4
def order_pizza(size, *args, **kwargs):
	print(f"Order a {size} pizza with the following toppings: {args}")
	print(f"the courier's details is:")
	for key, value in kwargs.items():
		print(f"- {key}: {value}")
	for kw in kwargs:
		print(kw)	
	
	for kw in kwargs.keys():
		print(kw)	
	for kw in kwargs.values():
		print(kw)	
		
order_pizza("large", "pepperoni", "cheese", name="Alex", is_driving=True, tip=5)

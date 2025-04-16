## *Args, **Kwargs, и Лямбда-функции

Для начала надо разобрать что вообще значит “*” в python.

---

Символ **“*”** в python это оператор распаковки, он как бы раскрывает “скобки”, если **“*”** стоит рядом с итерируемым объектом, то соответственно его раскроет/распакует

> Пример:
> 
> 
> ```python
> nums = [1, 2, 3, 6, 12, 10]
> print(nums)
> print(*nums)
> 
> # output
> [1, 2, 3, 6, 12, 10]
> 1, 2, 3, 6, 12, 10
> ```
> 

---

Теперь ежели мы составим функцию с пицце, и передадим в нее размер.

> Пример:
> 
> 
> ```python
> def order_pizza(size):
> 	print(f"Order a {size} pizza.")
> 	
> order_pizza("large")
> ```
> 

Это решение рабочие в этом случае, но что если нам нужно передавать много чего, не только размер, но и начинку, коробку, и даже курьера который повезёт это пиццу?

---

## *args

Для такова сценария лучше подойдет **args***, давай представим что это будут наши добавки, python знает что первая переменная это **size** в то время как все остальное, уже касается ***args**

> Пример:
> 
> 
> ```python
> def order_pizza(size, *args):
> 	print(f"Order a {size} pizza with the following toppings: {args}")
> 	
> order_pizza("large", "pepperoni", "olives", "cheese")
> 
> # output
> Order a large pizza with the following toppings: ('pepperoni', 'olives', 'cheese')
> ```
> 

И так мы получаем сразу кортеж с оставшимися данными. Но есть нас будут смущать скобочки и запятые мы всегда может перебрать **args** с помощью **for loop**

> Пример:
> 
> 
> ```python
> for topping in args: 
> 	print(topping)
> 	
> # output 
> pepperoni
> olives
> cheese
> ```
> 

---

## **kwargs

Теперь разберем случай с ****kwargs**, это аргументы функции по ключевым словам(**keywords**). 

Давайте теперь добавим имя курьера, подтвердим что он на машине и сколько чаевых ему достанется.

> Пример:
> 
> 
> ```python
> def order_pizza(size, *args, **kwargs):
> 	print(f"Order a {size} pizza with the following toppings: {args}")
> 	print(f"the courier's details is:")
> 	for key, value in kwargs.items():
> 		print(f"- {key}: {value}")
> 
> # output
> order_pizza("large", "pepperoni", "cheese", name="Alex", is_driving=True, tip=5)
> ```
> 

Метод **.items()** в данном случае позволяет со словаря получить там и ключ и значение. Но есть методы позволяющие получить отдельно ключи и значения без надобности перебирать их вместе.

> Пример:
> 
> 
> ```python
> for key in kwargs.keys():
>     print(key)
> 
> for value in kwargs.values():
>     print(value)
> ```
> 

Методы **.keys()** и **.values()** как раз вернут только ключи или только значения.

---

## Лямбда-функции

Это однострочные (анонимные) функции, без имени и обычно используются для простых операций. 

> Структура функции проста
> 
> 
> ```python
> lambda аргументы: выражения
> ```
> 
> Эта функция буквально представляет собой данную структуру в нормальном коде
> 
> ```python
> def func(x):
>     return x + 1
>     
> # Равноценно:
> lambda x: x + 1
> ```
> 

---

Функцию можно использовать как с 1 так и с более аргументами

> Пример:
> 
> 
> ```python
> # example 1
> square = lambda x: x * x
> print(square(5))  
> 	# output 25
> 
> # example 2
> add = lambda x, y: x + y
> print(add(3, 7))  
> 	# output 10
> 
> # example 3
> max_val = lambda x, y: x if x > y else y
> print(max_val(8, 5))  
> 	# output 8
> ```
> 

Чаще всего эта функция используется совместно с **sorted(), map(), filter(), reduce()**

> Пример:
> 
> 
> ```python
> # Sorted
> words = ["python", "ai", "lambda", "decorator"]
> sorted_words = sorted(words, key=lambda word: len(word))
> print(sorted_words)  
> 	# output ['ai', 'python', 'lambda', 'decorator']
> 
> pairs = [(1, 3), (2, 1), (5, 0)]
> sorted_pairs = sorted(pairs, key=lambda x: x[1])
> print(sorted_pairs)  
> 	# output  [(5, 0), (2, 1), (1, 3)]
> 
> #Map
> nums = [1, 2, 3, 4]
> squared = list(map(lambda x: x ** 2, nums))
> print(squared)  
> 	# output  [1, 4, 9, 16]
> 
> #Filter
> nums = [1, 2, 3, 4, 5, 6]
> evens = list(filter(lambda x: x % 2 == 0, nums))
> print(evens)  
> 	# output  [2, 4, 6]
> 
> #Reduce
> from functools import reduce
> 
> nums = [1, 2, 3, 4]
> product = reduce(lambda x, y: x * y, nums)
> print(product)  
> 	# output  24
> 
> ```
>
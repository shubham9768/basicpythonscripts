Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:/Users/Shubham/AppData/Local/Programs/Python/Python36-32/projects/myy_turtle.py 
>>> 
 RESTART: C:/Users/Shubham/AppData/Local/Programs/Python/Python36-32/projects/myy_turtle.py 
>>> 
 RESTART: C:/Users/Shubham/AppData/Local/Programs/Python/Python36-32/projects/myy_turtle.py 
>>> 
>>> 
 RESTART: C:\Users\Shubham\AppData\Local\Programs\Python\Python36-32\projects\myy_turtle.py 
>>> 
>>> 
>>> 
>>> clear
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    clear
NameError: name 'clear' is not defined
>>> 
>>> 
>>> 
>>> data = 'xbox | 150 | New'
>>> data
'xbox | 150 | New'
>>> product = [:data.index['|']]
SyntaxError: invalid syntax
>>> product = [:data.index('|')]
SyntaxError: invalid syntax
>>> product = data[:data.index('|')]
>>> product
'xbox '
>>> price = data[data.index('|'):data.index('|')]
>>> price
''
>>> price = data[data.index('|'):data.index(' ')]
>>> price
''
>>> 
>>> price = data[data.index('|')]
>>> price
'|'
>>> price = data[data.index('|'):]
>>> price
'| 150 | New'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 

>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> price = data[data.index('|')+1:]
>>> price
' 150 | New'
>>> price[:price.index('|')]
' 150 '
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 


>>> 

>>> 

>>> 


>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 
>>> 
>>> 
>>> data.find('9')
-1
>>> data.find('|')
5
>>> data.find('|',7)
11
>>> data[data.find('|')+1:data.find('|',7)]
' 150 '
>>> 
>>> 
>>> 
>>> grocc['apple','banana',50,20,]
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    grocc['apple','banana',50,20,]
NameError: name 'grocc' is not defined
>>> grocc = ['apple','banana',50,20,]
>>> grocc
['apple', 'banana', 50, 20]
>>> grocc[10]
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    grocc[10]
IndexError: list index out of range
>>> grocc[2]
50
>>> 
>>> 
>>> 
>>> 
>>> Product,Price,Condition = data.split('|')
>>> Product
'xbox '
>>> Price
' 150 '
>>> Condition
' New'
>>> 
>>> 
>>> 
>>> 
>>> for i in range(10):
	print(i)

	
0
1
2
3

4
5
6
7
8
9
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
>>> 
>>> 
>>> 
>>> 
>>> numbers
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    numbers
NameError: name 'numbers' is not defined
>>> 
>>> 
>>> 
>>> 
>>> numbers = [1,2,3,4,5,6]
>>> numbers
[1, 2, 3, 4, 5, 6]
>>> for number in range(7,20)
SyntaxError: invalid syntax
>>> for number in range(7,20):
	numbers.append(number)

	
>>> numbers
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> 
>>> 
>>> 
>>> numbers[::-1]
[19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
>>> 
>>> 
>>> for number in range(a,s):
	numbers.append(number)

	
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    for number in range(a,s):
NameError: name 'a' is not defined
>>> 
>>> 
>>> 
>>> 
 RESTART: C:\Users\Shubham\AppData\Local\Programs\Python\Python36-32\projects\myy_turtle.py 
>>> 
 RESTART: C:/Users/Shubham/AppData/Local/Programs/Python/Python36-32/projects/circle.py 
>>> 
 RESTART: C:/Users/Shubham/AppData/Local/Programs/Python/Python36-32/projects/circle.py 
>>> 
 RESTART: C:\Users\Shubham\AppData\Local\Programs\Python\Python36-32\projects\circle.py 
>>> 
 RESTART: C:\Users\Shubham\AppData\Local\Programs\Python\Python36-32\projects\circle.py 
>>> 
 RESTART: C:\Users\Shubham\AppData\Local\Programs\Python\Python36-32\projects\circle.py 
>>> 
 RESTART: C:\Users\Shubham\AppData\Local\Programs\Python\Python36-32\projects\circle.py 
>>> 
 RESTART: C:\Users\Shubham\AppData\Local\Programs\Python\Python36-32\projects\circle.py 
>>> 
 RESTART: C:\Users\Shubham\AppData\Local\Programs\Python\Python36-32\projects\circle.py 
>>> 
 RESTART: C:\Users\Shubham\AppData\Local\Programs\Python\Python36-32\projects\circle.py 
Traceback (most recent call last):
  File "C:\Users\Shubham\AppData\Local\Programs\Python\Python36-32\projects\circle.py", line 15, in <module>
    square(150,90)
  File "C:\Users\Shubham\AppData\Local\Programs\Python\Python36-32\projects\circle.py", line 12, in square
    my_turtle.right(angle)
  File "C:\Users\Shubham\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 1678, in right
    self._rotate(-angle)
  File "C:\Users\Shubham\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 3276, in _rotate
    self._update()
  File "C:\Users\Shubham\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 2660, in _update
    self._update_data()
  File "C:\Users\Shubham\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 2646, in _update_data
    self.screen._incrementudc()
  File "C:\Users\Shubham\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 1292, in _incrementudc
    raise Terminator
turtle.Terminator
>>> 
 RESTART: C:\Users\Shubham\AppData\Local\Programs\Python\Python36-32\projects\circle.py 
>>> 
 RESTART: C:\Users\Shubham\AppData\Local\Programs\Python\Python36-32\projects\circle.py 
Traceback (most recent call last):
  File "C:\Users\Shubham\AppData\Local\Programs\Python\Python36-32\projects\circle.py", line 15, in <module>
    square(150,90)
  File "C:\Users\Shubham\AppData\Local\Programs\Python\Python36-32\projects\circle.py", line 12, in square
    my_turtle.right(angle)
  File "C:\Users\Shubham\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 1678, in right
    self._rotate(-angle)
  File "C:\Users\Shubham\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 3276, in _rotate
    self._update()
  File "C:\Users\Shubham\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 2660, in _update
    self._update_data()
  File "C:\Users\Shubham\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 2646, in _update_data
    self.screen._incrementudc()
  File "C:\Users\Shubham\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 1292, in _incrementudc
    raise Terminator
turtle.Terminator
>>> 
 RESTART: C:\Users\Shubham\AppData\Local\Programs\Python\Python36-32\projects\circle.py 
>>> 
 RESTART: C:\Users\Shubham\AppData\Local\Programs\Python\Python36-32\projects\circle.py 
>>> 
 RESTART: C:\Users\Shubham\AppData\Local\Programs\Python\Python36-32\projects\circle.py 
>>> 
 RESTART: C:\Users\Shubham\AppData\Local\Programs\Python\Python36-32\projects\circle.py 

 RESTART: C:\Users\Shubham\AppData\Local\Programs\Python\Python36-32\projects\circle.py 
>>> 
 RESTART: C:\Users\Shubham\AppData\Local\Programs\Python\Python36-32\projects\circle.py 
>>> 
>>> 
>>> 
>>> 
>>> 
 RESTART: C:/Users/Shubham/AppData/Local/Programs/Python/Python36-32/projects/dictionary.py 
9768364459
>>> 
 RESTART: C:/Users/Shubham/AppData/Local/Programs/Python/Python36-32/projects/dictionary.py 
9768364459
['9768364459', 'shubham@gmail.com']
>>> 
 RESTART: C:/Users/Shubham/AppData/Local/Programs/Python/Python36-32/projects/dictionary.py 
9768364459
9768364459
>>> 
 RESTART: C:/Users/Shubham/AppData/Local/Programs/Python/Python36-32/projects/dictionary.py 
6667764534
shubham@gmail.com
>>> 
>>> 

>>> 

>>> 


>>> 


>>> 

>>> 

>>> 

>>> 
>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 

>>> 


>>> false
Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    false
NameError: name 'false' is not defined
>>> False
False
>>> True
True
>>> 
>>> 
>>> 
>>> 
>>> 
>>> if 40<41:
	print("true")

	
true
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> for i in range(1000)
SyntaxError: invalid syntax
>>> for i in range(10):
	print(i)

	
0
1
2
3
4
5
6
7
8
9
>>> 
>>> 
>>> 
>>> count=0
>>> for i in range(1,4)
SyntaxError: invalid syntax
>>> for i in range(1,4):
	count=count+i
print(count)
SyntaxError: invalid syntax
>>> 
>>> for i in range(1,4):
	count=count+i
print('count')
SyntaxError: invalid syntax
>>> for i in range(1,4):
	count=count+i
	print('count')

	
count
count
count
>>> for i in range(1,4):
	count=count+1
	print('count')

	
count
count
count
>>> 
>>> 
>>> 
>>> 
 RESTART: C:/Users/Shubham/AppData/Local/Programs/Python/Python36-32/projects/addition.py 
1
3
6
>>> 
 RESTART: C:/Users/Shubham/AppData/Local/Programs/Python/Python36-32/projects/addition.py 
6
>>> 
 RESTART: C:/Users/Shubham/AppData/Local/Programs/Python/Python36-32/projects/addition.py 
6
>>> 
 RESTART: C:/Users/Shubham/AppData/Local/Programs/Python/Python36-32/projects/addition.py 
6
Traceback (most recent call last):
  File "C:/Users/Shubham/AppData/Local/Programs/Python/Python36-32/projects/addition.py", line 14, in <module>
    sum_list[1,2,3]
TypeError: 'function' object is not subscriptable
>>> 
 RESTART: C:/Users/Shubham/AppData/Local/Programs/Python/Python36-32/projects/addition.py 
6
>>> 
 RESTART: C:/Users/Shubham/AppData/Local/Programs/Python/Python36-32/projects/addition.py 
>>> 
 RESTART: C:/Users/Shubham/AppData/Local/Programs/Python/Python36-32/projects/addition.py 
>>> 
 RESTART: C:/Users/Shubham/AppData/Local/Programs/Python/Python36-32/projects/addition.py 
6
>>> 

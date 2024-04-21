x=5
y=-7
z=3
A=6
numbers=[]
if abs(x)<A:
    numbers.append(x)
if abs(y)<A:
    numbers.append(y)
if abs(z)<A:
    numbers.append(z)
squares=[num**2 for num in numbers]
print('Квадрыты чисел с модулем меньше',A,':',squares)
print(('Количество таких чисел:'),len(numbers))

# how to use a file as a module in Python

from classes import Planet  # 'classes라는 파일에서 Planet이라는 클래스를 import한다'

planetB = Planet('taeyoon', 10000, 9.0, 'Taeyoon System')

print(f'Name is {planetB.name}')  # 'Name is taeyoon'
print(f'Radius is {planetB.radius}')  # 'Radius is 10000'
print(f'Gravity is {planetB.gravity}')  # 'Gravity is 9.0'
print(f'System is {planetB.system}')  # 'System is Taeyoon System'
# 'The planet spins and spins at a very high speed'
print(planetB.spin('a very high speed'))

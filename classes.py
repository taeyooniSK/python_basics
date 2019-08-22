# class 는 객체가 어떤 모습을 가질 지를 보여주는 청사진(blue print)와 같은 것.

'''
# 1. 기본적인 class의 형태

class Planet:
    # __init__ : 이 클래스의 새로운 instance를 만들때 실행됨 ( JS의 contructor함수와 비슷)/ self(=='this' in JS)는 (self는 내가 클래스로 새로 만드는 인스턴으를 가리킴
    # __init__ 함수에는 argument로 항상 1개의 argument가 주어지는데 그것이 'self'이다. 'self'가 없으면 에러가 뜸.
    def __init__(self):
        self.name = 'Hoth'
        self.radius = 200000
        self.gravity = 5.5
        self.system = 'Hoth System'

    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'

planetA = Planet()

print(f'Name is {planetA.name}')
print(f'Radius is {planetA.radius}')
print(f'Gravity is {planetA.gravity}')
print(f'System is {planetA.system}')
'''


# 2. 새로운 인스턴스를 만들 때마다 custom value를 넣을 수 있는 class

class Planet:
    # class level attribute, 클래스 안의 메소드들이 모두 공유할 수 있는 variable이라고 보면 됨(즉, 이 클래스로 만들어진 모든 인스턴트에서 이 variable 사용 가능)
    shape = 'round'

    def __init__(self, name, radius, gravity, system):
        # 이 클래스로 만들 인스턴스의 attributes들
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.system = system

    # 이 메소드는 인스턴스에서 사용할 수 있는 메소드 ( 클래스 자체에서 이 메소드에 접근 불가능 즉 Planet.orbit()은 안됨 )
    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'

    # 이 클래스 메소드는 클래스 레벨에서 접근할 수 있을 뿐만 아니라, 인스턴스에서도 접근이 가능함
    @classmethod  # class level의 메소드(데코레이터)
    def commons(cls):
        return f'All planets are {cls.shape}'

    @staticmethod  # 내가 직접 전달한 argument에 대해 클래스 레벨이나 인스턴스 레벨에서 로직을 실행할 수 있는 메소드
    def spin(speed='2000 kms per hour'):
        return f'The planet spins and spins at {speed}'


planetB = Planet('taeyoon', 10000, 9.0, 'Taeyoon System')

print(f'Name is {planetB.name}')
print(f'Radius is {planetB.radius}')
print(f'Gravity is {planetB.gravity}')
print(f'System is {planetB.system}')
print(Planet.shape)  # 클래스 level의 attribute라 클래스를 통해 접근해도 출력이 됨
print(planetB.shape)  # 클래스의 인스턴스를 통해서도 접근 가능
# print(Planet.name)  # name은 __init__ 함수를 통해 만들어진 인스턴스에서만 접근 가능


# 클래스 메소드가 클래스레벨과 인스턴스 레벨에서 접근 가능
# print(Planet.commons())  # 'All planets are round'
# print(planetB.commons())  # 'All planets are round'
print(Planet.spin())
print(planetB.spin('a very high speed'))

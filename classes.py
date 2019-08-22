# 'space라는 패키지(='여러 개의 모듈의 묶음')안에 planet이라는 모듈에서 Planet이라는 클래스를 가져온다.'
from space.planet import Planet
from space.calc import planet_mass, planet_vol

planetB = Planet('taeyoon', 10000, 9.0, 'Taeyoon System')

# 정상적으로 print하는 것을 확인할 수 있다. JS에서 보여주는 module형태랑은 숫서만 조금 다를 뿐 똑같다.
print(f'Name is {planetB.name}')  # 'Name is taeyoon'
print(f'Radius is {planetB.radius}')  # 'Radius is 10000'
print(f'Gravity is {planetB.gravity}')  # 'Gravity is 9.0'
print(f'System is {planetB.system}')  # 'System is Taeyoon System'

planetB_mass = planet_mass(planetB.gravity, planetB.radius)
planetB_vol = planet_vol(planetB.radius)

# 'planetB's mass : 1.3493253373313343e+19'
print(f'planetB\'s mass : {planetB_mass}')
# 'planetB's volume : 418933333.3333333'
print(f'planetB\'s volume : {planetB_vol}')

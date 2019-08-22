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

class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def get_name(self):
        print(self.name)

    def double_health_points(self):
        self.health_points *= 2

    def __str__(self):
        return f"{self.nickname} has a superpower of {self.superpower} and {self.health_points} health points."

    def __len__(self):
        return len(self.catchphrase)


my_hero = SuperHero('Piter Parker', 'Spiderman', 'super spider', 100, 'piter spider man')

class Tanoshero(SuperHero):
    glove = 'glove'
    def __init__(self,name, nickname, superpower, health_points, catchphrase,damage=False, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def double_health_points(self):
        self.fly = True
        return self.health_points ** 2

    def fly(self):
        return f'fly in the {self.fly}_phrase'

class Darkside(SuperHero)

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage=False, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def double_health_points(self):
        self.fly = True
        return self.health_points ** 2

    def fly(self):
        return f'fly in the {self.fly}_phrase'

thor = Tanoshero('thor', 'bog', 'grom', 200, 'хз', damage=300)
cap = Darkside('cap', 'pon', 'hello', 150, 'ladno', damage=100)
class Vilian(Tanoshero):
    SuperHero.people = 'monster'
    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        super().__init__(name, nickname, superpower, health_points, catchphrase)

    def Gen_x(self):
        pass

    def crit(self, hero):
       return self.damage ** 2

NAme = Vilian('tanos', 'tanka', 'kamni', 900, 'pon')
print(Vilian.crit(NAme, thor))
print(Vilian.crit(NAme, cap))







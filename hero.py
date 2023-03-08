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

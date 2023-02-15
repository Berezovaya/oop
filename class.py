class Bird:
    def __init__(self, name):
        print('Появилась новая птица!')
        self.name = name

    def rename(self, new_name):
        self.name = new_name


b = Bird("Жанна")
print("Я птица. Меня зовут " + b.name + '\n')

b2 = Bird("Сережа")
print("Я птица. Меня зовут " + b2.name)

b2.rename("Супер-Сережа")
print("Я птица. Теперь меня зовут " + b2.name + '\n')

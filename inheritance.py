class Bird:
    def __init__(self, name):
        print('Появилась новая птица!')
        self._name = name

    def say_your_name(self):
        print('Я птица! Меня зовут ' + self._name + '!\n')


class Phoenix(Bird):
    def reborn(self):
        print(self._name + ' возродился из пепла!!!')


b1 = Bird('Гоша')
b1.say_your_name()

b2 = Phoenix('Феня')
b2.say_your_name()
b2.reborn()

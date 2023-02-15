class Bird:
    def __init__(self, name):
        print('Появилась новая птица!')
        self._name = name               # private attribute

    def say_your_name(self):            # public method
        return self._name


b = Bird('Гоша')
print('Я птица! Меня зовут' + b.say_your_name()) # можно
print('Я птица! Меня зовут' + b._name) # нельзя

b._name = 'Больше не Гоша' # вообще нельзя

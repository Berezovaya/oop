class Bird:
    def sing(self):
        print('tweet-tweet!')


class Bear:
    def sing(self):
        print('RRRRRAAAA!')


class Human:
    def sing(self):
        print('eeee Makarena!')


bird1 = Bird()
bear1 = Bear()
human1 = Human()


for animal in [bird1, bear1, human1]:
    animal.sing()





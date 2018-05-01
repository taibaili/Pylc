class Animal(object):
    def __init__(self, hungry="yes", name=None, owner=None):
        self.hungry = hungry
        self.name = name
        self.owner = owner

    def noise(self):
        print('errr')

    def _internal_method(self):
        print("hard to find")


if __name__ == '__main__':
    dog = Animal()
    dog.owner = 'Sue'
    print()
    dog.owner
    dog.noise()

    cat = Animal()
    cat.owner = 'Yang'
    print()
    cat.owner
    cat.noise()

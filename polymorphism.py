from Person import Person

class Person2(Person):
    def greet(self, name=""):
        if name == "":
            print("Hello, " + self._first_name + "!")
        else:
            print("Hello, " + name + "!")


if __name__ == '__main__':
    my_artist = Person2('Rafael', 'Santos', 1976, 3, 23)
    print('my artist name is ' + my_artist.getName()[0] + ' ' + my_artist.getName()[1])
    my_artist.greet()
    my_artist.greet(name = "Theo")
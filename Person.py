import datetime, time

class Person:
    _birth_date = datetime.date.today()
    _first_name = ''
    _last_name = ''
    
    def __init__(self, first_name, last_name, birth_year, birth_month, birth_day):
        self._first_name = first_name
        self._last_name = last_name
        self._birth_date = datetime.date(birth_year, birth_month, birth_day)

    def getAge(self):
        return datetime.date.today().year - self._birth_date.year
    
    def getName(self):
<<<<<<< HEAD
        return (self._firstName, self._lastName)

    def greet(self):
        print("Hello there!")
=======
        return (self._first_name, self._last_name)
>>>>>>> 7278b59f6da716462a670f71c31e8d20ba7cc3dd

import datetime, time

class Person:
    _birthDate = datetime.date.today()
    _firstName = ''
    _lastName = ''
    
    def __init__(self, firstName, lastName, birth_year, birth_month, birth_day):
        self._firstName = firstName
        self._lastName = lastName
        self._birthDate = datetime.date(birth_year, birth_month, birth_day)

    def getAge(self):
        return datetime.date.today().year - self._birthDate.year
    
    def getName(self):
        return (self._firstName, self._lastName)

    def greet(self):
        print("Hello there!")
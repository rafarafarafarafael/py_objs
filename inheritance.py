from Person import Person

class FxArtist(Person):
    def __init__(self, first_name, last_name, birth_year, birth_month, birth_day):
        super(FxArtist, self).__init__(first_name, last_name, birth_year, birth_month, birth_day)


if __name__ == '__main__':
    my_artist = FxArtist('Rafael', 'Santos', 1976, 3, 23)
    print('my artist name is ' + my_artist.getName()[0] + ' ' + my_artist.getName()[1])


class Musician:

    def __init__(self, get_instrument, play_solo):
        """
        This is a doc
        """

        self.get_instrument = get_instrument
        self.play_solo = play_solo

    def __repr__(self):
        return {
            'get_instrument': self.get_instrument,
            'play_solo': self.play_solo
        }

    def __str__(self):
        return f'Musician(get_instrumtent={self.get_instrumnet} play_solo={self.play_solo}'


class Guitarist(Musician):
    # def __init__(self, get_instrument, play_solo):
    #     self.get_instrument = get_instrument
    #     self.play_solo = play_solo

    def __repr__(self):
        return {
            'get_instrument': self.get_instrument,
            'play_solo': self.play_solo
        }

    def __str__(self):
        return f'Musician(get_instrumtent={self.get_instrument} play_solo={self.play_solo}'


class Drummer(Musician):
    # def __init__(self, get_instrument, play_solo):
    #     self.get_instrument = get_instrument
    #     self.play_solo = play_solo

    def __repr__(self):
        return {
            'get_instrument': self.get_instrument,
            'play_solo': self.play_solo
        }

    def __str__(self):
        return f'Musician(get_instrumtent={self.get_instrument} play_solo={self.play_solo}'


class Bassist(Musician):
    # def __init__(self, get_instrument, play_solo):
    #     self.get_instrument = get_instrument
    #     self.play_solo = play_solo

    def __repr__(self):
        return {
            'get_instrument': self.get_instrument,
            'play_solo': self.play_solo
        }

    def __str__(self):
        return f'Musician(get_instrumtent={self.get_instrument} play_solo={self.play_solo}'


guitarist = Guitarist('Guitar', 'shredding')
bassist = Bassist('Bass', 'Thumping')
drummer = Drummer('Drums', 'Chopping')


class Band(Musician):

    def __init__(self, name, members):
        """
        This is a doc
        """

        self.name = name
        self.members = members

    def __str__(self):
        return f'Musician(name={self.name} members={self.members}'

    def __repr__(self):

        return {
            'name': self.name

        }

    def play_solos(self):
        # for member in self.members:
        return self.members.play_solo


python_band = Band('Python Maniacs', guitarist)

print(python_band.name)
print(python_band.members)
# print(python_band.play_solos)

class Musician:

    def __init__(self, get_instrument, play_solo):
        """This class has the base attributes for a musician.

        Args: 
            get_instrument (str): [Enter an instrument] 
            play_solo (str): [Enter there solo keyword]
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

    def __repr__(self):
        return {
            'get_instrument': self.get_instrument,
            'play_solo': self.play_solo
        }

    def __str__(self):
        return f'Musician(get_instrumtent={self.get_instrument} play_solo={self.play_solo}'


class Drummer(Musician):

    def __repr__(self):
        return {
            'get_instrument': self.get_instrument,
            'play_solo': self.play_solo
        }

    def __str__(self):
        return f'Musician(get_instrumtent={self.get_instrument} play_solo={self.play_solo}'


class Bassist(Musician):

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


class Band():

    def __init__(self, name, members):
        """Create a band by entering its name and members

        Args:
            name ([str]): [This is the name of your band]
            members ([obj]): [This is the members]
        """

        self.name = name
        self.members = members

    def __str__(self):
        return f'Musician(name={self.name} members={self.members}'

    def __repr__(self):

        return str({
            'name': self.name,
            'members': self.members
        })

    def play_solos(self):
        """prints out solos of the musicians

        Returns:
            [string]: [prints solos from the band in order]
        """
        arr = ''
        for i in self.members:
            if i:
                arr += i.play_solo + '\n'
        return arr

    def to_list(self):
        """retrieves previous band (needs patch)

        Returns:
            [string]: [Names of previous band members]
        """
        arr = ''
        for i in self.members:
            if i:
                arr += i.get_instrument + '\n'
        return arr


python_band = Band('Python Maniacs', [bassist, guitarist])
python_band_two = Band('rollers', [drummer, guitarist])

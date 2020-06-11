class Musician:

    def __init__(self, get_instrument, play_solo):
        """
        This is a doc
        """

        self.get_instrument = get_instrument
        self.play_solo = play_solo

    def __repr__(self):
        return {
            'get_instrument': {self.get_instrument},
            'play_solo': {self.play_solo}
        }

    def __str__(self):
        return f'Musician(get_instrumtent={get_instrumnet} play_solo={play_solo}'


class Guitarist(Musician):
    def __init__(self, get_instrument, play_solo):
        self.get_instrument = get_instrument
        self.play_solo = play_solo

    def __repr__(self):
        return {
            'get_instrument': {self.get_instrument},
            'play_solo': {self.play_solo}
        }

    def __str__(self):
        return f'Musician(get_instrumtent={get_instrumnet} play_solo={play_solo}'


class Drummer(Musician):
    def __init__(self, get_instrument, play_solo):
        self.get_instrument = get_instrument
        self.play_solo = play_solo

    def __repr__(self):
        return {
            'get_instrument': {self.get_instrument},
            'play_solo': {self.play_solo}
        }

    def __str__(self):
        return f'Musician(get_instrumtent={get_instrumnet} play_solo={play_solo}'


class Bassist(Musician):
    def __init__(self, get_instrument, play_solo):
        self.get_instrument = get_instrument
        self.play_solo = play_solo

    def __repr__(self):
        return {
            'get_instrument': {self.get_instrument},
            'play_solo': {self.play_solo}
        }

    def __str__(self):
        return f'Musician(get_instrumtent={get_instrumnet} play_solo={play_solo}'


guitarist = Guitarist('Guitar', 'shredding')
bassist = Bassist('Bass', 'Thumping')
drummer = Drummer('Drums', 'Chopping')


class Band:

    def __init__(self, name, members, play_solos, )

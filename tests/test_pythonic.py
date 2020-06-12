from pythonic_garage_band.pythonic_garage_band import (
    Musician,
    Guitarist,
    guitarist,
    Bassist,
    bassist,
    Drummer,
    drummer,
    Band)


def test_garage_guitarist():
    guitarist = Guitarist('Guitar', 'shredding')
    actual = guitarist.play_solo
    expected = 'shredding'
    assert actual == expected


def test_garage_guitarist_two():
    guitarist = Guitarist('Guitar', 'shredding')
    actual = guitarist.get_instrument
    expected = 'Guitar'
    assert actual == expected


def test_garage_bassist():
    bassist = Bassist('bass', 'thumping')
    actual = bassist.play_solo
    expected = 'thumping'
    assert actual == expected


def test_garage_bassist_two():
    bassist = Bassist('bass', 'thumping')
    actual = bassist.get_instrument
    expected = 'bass'
    assert actual == expected


def test_garage_drummer():
    drummer = Drummer('drums', 'chopping')
    actual = drummer.play_solo
    expected = 'chopping'
    assert actual == expected


def test_garage_drummer_two():
    drummer = Drummer('drums', 'chopping')
    actual = drummer.get_instrument
    expected = 'drums'
    assert actual == expected


def test_garage_band():
    python_band = Band('Python Maniacs', guitarist)
    actual = python_band.name
    expected = 'Python Maniacs'
    assert actual == expected


def test_garage_band_two():
    python_band = Band('Python Maniacs', [guitarist])
    actual = python_band.play_solos()
    expected = 'shredding\n'
    assert actual == expected


def test_garage_band_three():
    python_band = Band('Python Maniacs', [guitarist, drummer])
    actual = python_band.play_solos()
    expected = 'shredding\nChopping\n'
    assert actual == expected

""" Provides a musician playing an instrument"""


class Musician:
    """
    A musician owning an instrument and playing musical notes.
    """

    def __init__(self, name, instrument):
        """
        Creates the musician.
        :param name: The name of the musician.
        :param instrument: The reference to the instrument.
        """
        self._name = name
        self._instrument = instrument

    @property
    def name(self):
        """
        Gets the name of the musician
        :return: str
        """
        return self._name

    def play_note(self, the_tone):
        """
        Plays the musical note on the instrument.
        :param the_tone: der gespielte Ton
        """
        print(f'{self._name} spielt mit {self._instrument.play_note(the_tone)}')

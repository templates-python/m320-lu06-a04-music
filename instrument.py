""" Provides a class for an instrument """


class Instrument:
    """
    A music instrument with the ability to play a musical note.
    """

    def __init__(self, designation):
        """
        Creates an instrument with the designation.
        :param designation: the designation, i.e. Posaune
        """
        self._designation = designation

    @property
    def designation(self):
        """
        Gets the designation of this instrument.
        :return: designation
        """
        return self._designation

    def play_note(self, the_note):
        """
        Plays one musical note.
        :param the_note: The musical not to be played.
        :return: A text that shows the note played.
        """
        return str(f'{self._designation} den Ton {the_note}')

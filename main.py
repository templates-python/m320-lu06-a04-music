"""
main.py is used to execute the application.
The required objects are created and the
methods are called as specified.
"""
from instrument import Instrument
from musician import Musician


def main():
    """ main function to run the application """
    guitar = Instrument('Gitarre')
    piano = Instrument('Klavier')
    maxi = Musician('Max', guitar)
    moritz = Musician('Moritz', piano)

    maxi.play_tone('a')
    moritz.play_tone('f')


if __name__ == '__main__':
    main()

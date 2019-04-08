##
## EPITECH PROJECT, 2019
## 205IQ_2018
## File description:
## utilities
##

from sys import stderr

def error(str: str) -> None:
    """Write error on standard output then exits with error."""
    stderr.write(str)
    exit(84)

def usage() -> None:
    """Display helper."""
    print('USAGE\n\t./205IQ u s [IQ1] [IQ2]\n',
        'DESCRIPTION\n\tu\tmean\n\ts\tstandard deviation',
        '\tIQ1\tminimum IQ\n\tIQ2\tmaximum IQ',
        sep='\n')
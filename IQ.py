##
## EPITECH PROJECT, 2019
## 205IQ_2018
## File description:
## IQ
##

from utilities import error
from math import pi, sqrt, exp

def get_proba(data: [int]) -> [float]:
    """Get the proba result tab, from 0 to 200."""
    IQ_proba = []
    for i in range (0, 201):
        result = 1 / (data[1] * sqrt(2 * pi)) * \
            exp(-0.5 * pow((i - data[0]) / data[1], 2))
        IQ_proba.append(result)
    return IQ_proba

def inferior_IQ(data: [float]) -> None:
    """Writes a percentage of people with inferior IQ."""
    if 0 < data[2] < 200:
        result = 0
        for i in range(0, data[2] * 100):
            result += 1 / (data[1] * sqrt(2 * pi)) * \
                exp(-0.5 * pow(((i / 100) - data[0]) / data[1], 2))
        print('{:.01f}% of people have an IQ inferior to {:d}'
            .format(result, data[2]))
    else:
        error('IQ must be integer between 0 and 200.\n')

def between_IQ(data: [float]) -> None:
    """Writes a percentage of people with IQ between IQ1 and IQ2."""
    if 0 < data[2] < data[3] < 200:
        result = 0
        i = data[2]
        while (i < data[3]):
            result += 1 / (data[1] * sqrt(2 * pi)) * \
                exp(-0.5 * pow((i - data[0]) / data[1], 2))
            i += 0.01
        print('{:.01f}% of people have an IQ between {:d} and {:d}'
              .format(result, data[2], data[3]))
    else:
        error('IQ must be integers between 0 and 200, and IQ1 < IQ2.\n')

def print_IQ_tab(IQ_tab: [float]) -> None:
    """Print proba results from 0 to 200."""
    for i in range(0, 201):
        print('{:d} {:.05f}' .format(i, IQ_tab[i]))

def IQ_parser(data: [int]) -> None:
    """Redirect to correct IQ calculator option."""
    if len(data) == 2:
        print_IQ_tab(get_proba(data))
    elif len(data) == 3:
        inferior_IQ(data)
    elif len(data) == 4:
        between_IQ(data)

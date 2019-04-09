##
## EPITECH PROJECT, 2019
## 205IQ_2018
## File description:
## IQ
##

from math import pi, sqrt, exp

def get_proba(data: [int]) -> [float]:
    """Get the proba result tab, from 0 to 200."""
    IQ_proba = []
    for i in range (0, 201):
        result = 1 / (data[1] * sqrt(2 * pi)) * \
            exp(-0.5 * pow((i - data[0]) / data[1], 2))
        IQ_proba.append(result)
    return IQ_proba

def print_IQ_tab(IQ_tab: [float]) -> None:
    """Print proba results from 0 to 200."""
    for i in range(0, 201):
        print('{:d} {:.05f}' .format(i, IQ_tab[i]))

def IQ_parser(data: [int]) -> None:
    """Redirect to correct IQ calculator option."""
    IQ_tab = get_proba(data)
    if len(data) == 2:
        print_IQ_tab(IQ_tab)

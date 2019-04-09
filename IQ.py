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
    # result = 0.00
    for i in range (0, 201):
        result = 1 / (data[1] * sqrt(2 * pi)) * exp(- (pow((i - data[0]), 2) / pow(2 * data[1], 2)))
        IQ_proba.append(result * 100)
    return IQ_proba


def IQ_parser(data: [int]) -> None:
    """Redirect to correct IQ calculator option."""
    print(len(get_proba(data)))
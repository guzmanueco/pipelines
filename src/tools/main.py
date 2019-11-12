import sys
import argparse
import subprocess
import dataset.py

def recibeConfig():
    parser = argparse.ArgumentParser(description='Comparar número de suicidios con la renta per capita del país')
    parser.add_argument('--country',
                        help='país que quieres analizar'
                        )
    parser.add_argument('--suicides',
                        help='ordena países por numero de suicidios'
                        )
    parser.add_argument('--pc',
                        help='ordena países por renta per capita'
                        )

    args = parser.parse_args()
    print(args)
    return args
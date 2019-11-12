import sys
import argparse
import subprocess
import dataset
import sorting

def recibeConfig():
    parser = argparse.ArgumentParser(description='Comparar número de suicidios con la renta per capita del país')
    parser.add_argument('--country',help='retorna lista de países disponibles',)
    parser.add_argument('--suicides', help='ordena países por numero de suicidios')
    parser.add_argument('--pc', help='ordena países por renta per capita')
    grupo.add_argument('--comp_pc', help='Compara lista de países por renta pc', action='store_true')           # action guarda el argumento
    grupo.add_argument('--comp_sui', help='Compara lista de países por numero de suicidios', action='store_true')

    args = parser.parse_args()
    print(args)
    return args

# funcion principal
def main(): 

    args=parse()

    # opciones
    print(args)
    if args.country:
        print ('Lista de países disponibles:\n{}'.format(listing_countries())

    elif args.suicides:
        print ('Países ordenados por número de suicidios:\n{}'.format(sorting_suicides())

    elif args.pc:
        print ('Países ordenados por renta per capita:\n{}'.format(sorting_pc())

    else:
        print ('Error: se requiere un argumento para realizar la accion.')


if __name__=='__main__':
    main()

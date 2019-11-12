import pandas as pd
import dataset

def sorting_pc():
    data=dataset.cleaning_merging()
    return data.sort_values(by='per capita',ascending=False)

def sorting_suicides():
    data=dataset.cleaning_merging()
    return data.sort_values(by='suicides_no',ascending=False)

def listing_countries():
    data=(dataset.cleaning_merging())
    countries=list(data['country'])
    return countries

def comparing_countries_pc(lst):
    #lst debe ser una lista de países que estén en el data
    data=(dataset.cleaning_merging())
    for e in data['country']:
        if e not in lst:
            data=data[data['country']!=e]
    return data.sort_values(by='per capita',ascending=False)

def comparing_countries_suicides(lst):
    #lst debe ser una lista de países que estén en el data
    data=(dataset.cleaning_merging())
    for e in data['country']:
        if e not in lst:
            data=data[data['country']!=e]
    return data.sort_values(by='suicides_no',ascending=False)

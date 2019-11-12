import pandas as pd
import requests
import json

def getDataset():
    path="../../Input/who_suicide_statistics.csv"
    data=pd.read_csv(path)
    # Getting suicides in 2015
    data=data.loc[data['year']==2015]
    # Grouping by country
    data=data.groupby(['country','year'],as_index=False)['suicides_no','population'].sum()
    return data


def getApi():
    res=requests.get("http://api.worldbank.org/v2/country/ALB;ATG;ARG;ARM;ABW;AUS;AUT;BLR;BEL;BRA;BRN;CHL;COL;HRV;CUB;CYP;CZE;DNK;DMA;ECU;EGY;EST;FIN;GEO;DEU;GRC;GRD;GTM;HUN;ISL;IRN;ISR;ITA;JPN;KAZ;KGZ;LVA;LTU;LUX;MLT;MUS;MEX;NLD;NIC;NOR;PAN;PER;POL;QAT;KOR;MDA;ROM;RUS;KNA;VCT;SYC;SVN;ZAF;ESP;SWE;CHE;THA;TUR;TKM;UKR;GBR;USA;URY/indicator/NY.GNP.PCAP.CD?date=2015&format=json&per_page=1000")
    result = res.json()
    new_result=[]
    for e in result:
        for x in e:
            new_result.append(x)
    new_result=new_result[6:]
    per_capita=pd.DataFrame(new_result)
    per_capita=per_capita[['country','date','value']]
    for i in range(len(per_capita['country'])):
        per_capita['country'][i]=per_capita['country'][i]['value']
    per_capita=per_capita.sort_values(by='country')
    return per_capita



def cleaning_merging():
    final_country=[]
    final_country_api=[]
    per_capita=getApi()
    data=getDataset()
    country_api=(set(per_capita['country']))
    country_api=list(country_api)
    country_api=sorted(country_api)
    country=(set(data['country']))
    country=list(country)
    country=sorted(country)
    for e in country_api:
        if e not in country:
            final_country_api.append(e)
    for e in country:
        if e not in country_api:
            final_country.append(e)
    for e in final_country:
        data=data[data['country']!=e] 
    for e in final_country_api:
        per_capita=per_capita[per_capita['country']!=e]
    per_capita=per_capita['value']
    data['per capita']=per_capita
    return data
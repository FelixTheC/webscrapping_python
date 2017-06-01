#! /usr/env/python3

from bs4 import BeautifulSoup as bs
import requests
import pandas

r = requests.get('http://www.century21.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/')

if r.status_code == 200:
    c = r.content
    soup = bs(c, 'html.parser')
    all = soup.find_all('div', {'class': 'propertyRow'})
    l = []
    for item in all:
        dic = {}
        dic['Price'] = item.find('h4',{'class': 'propPrice'}).text.replace('\n','').replace(' ', '')
        dic['Address'] = item.find('span', {'class': 'propAddresse'})[0].text
        dic['Zip'] = item.find('span', {'class': 'propAddresse'})[1].text
        try:
            dic['Bed'] = item.find('span', {'class': 'infoBed'}).find('b').text
        except:
            dic['Bed'] = None
        
        try:
            dic['Sqrft'] = item.find('span', {'class': 'infoSqft'}).find('b').text
        except:
            dic['Sqrft'] = None
            
        try:
            dic['FullBath'] = item.find('span', {'class': 'infoValueFullBath'}).find('b').text
        except:
            dic['FullBath'] = None
        try:
            dic['HalfBath'] = item.find('span', {'class': 'infoValueHalfBath'}).find('b').text
        except:
            dic['HalfBath'] = None            
            
        for column_group in item.find_all('div', {'class': 'columnGroup'}):
            for feature_group, feature_name in zip(column_group.find('span', {'class': 'featureGroup'}),
                                                   column_group.find('span', {'class': 'featureName'})):
                if 'Lot Size' in feature_group.text:
                    dic['Lot Size'] = feature_name.text
        l.append(dic)
        
    df = pandas.DataFrame(l)
    df.to_csv('estate.csv')
                                          
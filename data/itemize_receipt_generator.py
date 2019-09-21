# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 11:35:16 2019

@author: JZST6G
"""

# install the requests package using 'python -m pip install requests'
import json
import requests

catergory_type = "Shopping"

#read in all customer information
with open('response_1569075691492.json') as json_file:
    data = json.load(json_file)

#extract all customers' id number
customers = data["result"]
counter=0
for p in customers["customers"]:
    if counter < 100:
        response = requests.get(
            'https://api.td-davinci.com/api/customers/' + p['id']+'/transactions',
            headers = { 'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDQlAiLCJ0ZWFtX2lkIjoiOWQwNzY0NzgtNjgzZi0zZDA3LTg4MWMtYmJiMTkxZmQ3YWI4IiwiZXhwIjo5MjIzMzcyMDM2ODU0Nzc1LCJhcHBfaWQiOiIxYjQ3ODdmNC0yNDQxLTQxNDMtOTA4Ny1mZmFhMGQ1MDVlYjEifQ.Qaw2i6mRrcOzUF2KC8AZllRi5IYKrGjQfrVicROMeJo' },
            json={ 'continuationToken': '' }
        )
        
        for transaction in response_data["result"]:
            if transaction['categoryTags'][0] == catergory_type:
                #Determine amount paid
                amount = float(transaction['currencyAmount'])
                
                
                transaction['id']=[transaction['id']]
                transaction['id'].append('milk')
        with open(p['id']+'.json', 'w') as outfile:
            json.dump(response_data, outfile)
        counter+=1
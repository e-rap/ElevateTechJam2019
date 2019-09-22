# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 19:44:20 2019

@author: JZST6G
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 15:03:16 2019

@author: JZST6G
"""
import json

class data_processor:
    
    def __init__(self, first_name, last_name):
        self.given_name = first_name
        self.surname = last_name
        self.customer_id = 'xxxxxxxxxx'
        self.transactions = []
        
    def get_customer_id(self):
        with open('response_1569075691492.json') as json_file:
            data = json.load(json_file)
        #extract all customers' id number
        customers = data["result"]
        for p in customers["customers"]:
            if p["givenName"] == self.given_name and p["surname"] == self.surname:
                self.customer_id = p["id"]
                break
            
            
    def get_customer_transactions(self):
        if self.customer_id != 'xxxxxxxxxx':
            with open(self.customer_id+'.json') as json_file:
                data = json.load(json_file)
            for transaction in data['result']:
                if ('locationPostalCode' in transaction):
                    if transaction['categoryTags'][0] == 'Shopping':
                        for item in transaction['id']['items']:
                            item['postal_code'] = transaction["locationPostalCode"]
    #                        item['lat'] = transaction['locationLatitude']
                            item['customer_id'] = self.customer_id
                            self.transactions.append(item)
        return self.transactions
    
    def process(self):
        self.get_customer_id()
        self.get_customer_transactions()
        return  self.transactions 
    

        
                
with open('response_1569075691492.json') as json_file:
    data = json.load(json_file)

#extract all customers' id number
customers = data["result"]
counter=0

customer_info = {}
customer_info = []

for p in customers["customers"]:
    if counter < 1000:        
        data = data_processor(p["givenName"],p["surname"])
        counter+=1
        customer_info += data.process()

with open('customer_transaction_data.json', 'w') as outfile:
    json.dump(customer_info, outfile)
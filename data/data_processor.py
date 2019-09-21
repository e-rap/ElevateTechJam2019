# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 15:03:16 2019

@author: JZST6G
"""

class data_processor:
    
    def __init__(self, first_name, last_name):
        self.given_name = first_name
        self.surname = last_name
        self.customer_id = 'xxxxxxxxxx'
        self.total_co2 = 0
        self.recyclability = 0
        self.location = "xxxxxx"
        
    def get_customer_id(self):
        with open('response_1569075691492.json') as json_file:
            data = json.load(json_file)
        #extract all customers' id number
        customers = data["result"]
        for p in customers["customers"]:
            if p["givenName"] == self.given_name and p["surname"] == self.surname:
                self.customer_id = p["id"]
                break
            
            
    def get_customer_co2_footprint(self):
        if self.customer_id != 'xxxxxxxxxx':
            with open(self.customer_id+'.json') as json_file:
                data = json.load(json_file)
            for transaction in data['result']:
                if transaction['categoryTags'][0] == 'Shopping':
                    for item in transaction['id']['items']:
                        self.total_co2 += item['co2_emissions']
        return self.total_co2
    
    def get_customer_recyclability(self):
        counter =0
        total_recyclability =0
        if self.customer_id != 'xxxxxxxxxx':
            with open(self.customer_id+'.json') as json_file:
                data = json.load(json_file)
            for transaction in data['result']:
                if transaction['categoryTags'][0] == 'Shopping':
                    for item in transaction['id']['items']:
                        total_recyclability += item['recylable']
                        counter+=1
        self.recyclability = total_recyclability/counter
        return self.recyclability
    
    def get_customer_location(self):
        with open('response_1569075691492.json') as json_file:
            data = json.load(json_file)
        #extract all customers' id number
        customers = data["result"]
        for p in customers["customers"]:
            if p["id"] == self.customer_id:
                self.location = p["addresses"]["principalResidence"]["postalCode"]
                break
        return self.location
    
    def process(self):
        self.get_customer_id()
        self.get_customer_co2_footprint()
        self.get_customer_recyclability()
        self.get_customer_location()
        return {"name" : self.given_name + " " + self.surname ,
        'id': self.customer_id,
        'location': self.location,
        'recylable' : self.recyclability,
        'co2_emissions' : self.total_co2} 
        
                
with open('response_1569075691492.json') as json_file:
    data = json.load(json_file)

#extract all customers' id number
customers = data["result"]
counter=0
for p in customers["customers"]:
    if counter < 100:        
        data = data_processor(p["givenName"],p["surname"])
        counter+=1
        print(data.process())
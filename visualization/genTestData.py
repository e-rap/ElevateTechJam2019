import json
import random


def genCustomer():
    
    customer = dict()
    customer['cust_id'] = genCustomer.cust_id
    customer['postal_code'] = "V4R 2N5"
    customer['recyle_score'] = random.random()
    customer['co2_waste_kg'] = random.randint(0,5)
    genCustomer.cust_id += 1
    return customer
genCustomer.cust_id = 0

def main():
    data = list()
    for i in range(0,10):
        data.append(genCustomer())

    with open('testData.json', 'w') as file:
        json.dump(data, file)W

if __name__ == "__main__":
    main()
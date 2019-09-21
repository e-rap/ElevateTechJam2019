import sys
import json
from random import seed
from random import randint

# seed random number generator
seed(2)

class rand_item_generator:
    
    def __init__(self):
        # The format "Item" : [Price,recyclable,co2 emissions]
        self.__items_list = [
        {"name" : "Milk",
        'price': 2,
        'recylable' : 1,
        'co2_emissions' : 1} ,         
        {"name" : "Tea",
        'price': 4,
        'recylable' : 1,
        'co2_emissions' : 2},
        {"name" : "Fruits",
        'price': 3,
        'recylable' : 1,
        'co2_emissions' : 0.5}
        ]

    def get_item(self):
        max_rand_num = len(self.__items_list) - 1
        rand_num = randint(0,max_rand_num)
        return json.dumps(self.__items_list[rand_num])




if __name__ == "__main__":
    rd_gen = rand_item_generator() 
    print(rd_gen.get_item())
    print(rd_gen.get_item())
    pass
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
        'recylable' : 0,
        'co2_emissions' : 1} ,         
        {"name" : "Tea",
        'price': 4,
        'recylable' : 0,
        'co2_emissions' : 2},
        {"name" : "Fruits",
        'price': 3,
        'recylable' : 1,
<<<<<<< HEAD
        'co2_emissions' : 3},
        {"name" : "Cereals",
        'price': 7,
        'recylable' : 0,
        'co2_emissions' : 3},
        {"name" : "Butter",
        'price': 3,
        'recylable' : 1,
        'co2_emissions' : 6},
        {"name" : "Cigarettes",
        'price': 30,
        'recylable' : 0,
        'co2_emissions' : 5},
        {"name" : "Tissues",
        'price': 9,
        'recylable' : 1,
        'co2_emissions' : 1},
        {"name" : "Local Chicken",
        'price': 15,
        'recylable' : 1,
        'co2_emissions' : 0},

        {"name" : "Kraft Slices",
        'price': 8,
        'recylable' : 1,
        'co2_emissions' : 7},

        {"name" : "Plastic Bags",
        'price': 3,
        'recylable' : 0,
        'co2_emissions' : 10}

=======
        'co2_emissions' : 0.5},
        {"name" : "Vegetables",
        'price': 5,
        'recylable' : 1,
        'co2_emissions' : 1},
        {"name" : "Beef",
        'price': 2,
        'recylable' : 1,
        'co2_emissions' : 10},
        {"name" : "Pork",
        'price': 2,
        'recylable' : 1,
        'co2_emissions' :6},
        {"name" : "Chicken",
        'price': 2,
        'recylable' : 1,
        'co2_emissions' : 1},
        {"name" : "Plastic",
        'price': 0.5,
        'recylable' : 0,
        'co2_emissions' :4},
        {"name" : "Steel",
        'price': 2,
        'recylable' : 1,
        'co2_emissions' : 3},
        {"name" : "Soda",
        'price': 1,
        'recylable' : 1,
        'co2_emissions' : 0.5},
        {"name" : "Food Containers",
        'price': 1,
        'recylable' : 0,
        'co2_emissions' : 2},
        {"name" : "Plastic Bags",
        'price': 0.5,
        'recylable' : 0,
        'co2_emissions' : 2},
        {"name" : "Ceramics",
        'price': 3,
        'recylable' : 0,
        'co2_emissions' : 2},
        {"name" : "Tetra Packs",
        'price': 2,
        'recylable' : 0,
        'co2_emissions' : 4}
>>>>>>> 981448e43dd5bdb401e8994ab2167b2b2ec112ec
        ]

    def get_item(self):
        max_rand_num = len(self.__items_list) - 1
        rand_num = randint(0,max_rand_num)
        return json.dumps(self.__items_list[rand_num])




if __name__ == "__main__":
    rd_gen = rand_item_generator() 
    print(rd_gen.get_item())
    print(rd_gen.get_item())
    print(rd_gen.get_item())
    pass
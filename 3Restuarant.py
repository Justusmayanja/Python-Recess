class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("\nRestaurant Name:", self.restaurant_name)
        print("Cuisine Type:", self.cuisine_type)


restaurant1 = Restaurant("Sunrise Restaurant", "African Food")
restaurant2 = Restaurant("Pizza Palace", "Italian Food")
restaurant3 = Restaurant("Dragon Kitchen", "Chinese Food")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
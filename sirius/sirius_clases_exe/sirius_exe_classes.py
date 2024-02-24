"""
Order management in a restaurant
Describe the class architecture for order management in a restaurant. You need to create the following classes:

Dish class:
Fields:
Name of dish
Price
Methods:
Getters and setters for fields

Order class:
Fields: 
Customer - object of class "Customer"
Dish list - array or list of objects of class "Dish"
Methods:
Add a dish to the order
Remove a dish from the order
Get the list of dishes in the order

Restaurant class:
Fields:
Orders - list of objects of class "Order"
List of all restaurant dishes - list of objects of class "Dish"
List of available restaurant dishes - list of objects of class "Dish"
Methods:
Create an order if all its dishes are available
Delete order
Get the list of orders
"""

class Dish():
  def __init__(self, price, name): # все атрибуты которые обязвтельны для этого класса
    self.price = price 
    self.name = name
  
  def get_name(self):
    return self.name
  
  def get_price(self):
    return self.price
  
  def change_name(self, new_name):
    self.name = new_name
    print("name changed")
  
  def change_price(self, new_price):
    self.price = new_price
    print("price changed")


class Customer():
  def __init__(self, name_of_the_customer):
    self.name_of_the_customer = name_of_the_customer

class Order():
  def __init__(self, customer_name: Customer, order: list[Dish]):
    
    self.customer_name = customer_name
    self.order = order


  def add_dish_to_the_order(self, dish: Dish | list[Dish]):
    if isinstance(dish, Dish):
      self.order.append(dish)
      print("item added")
    elif isinstance(dish, list):
      for element in dish:
        self.order.append(element)
      print("List added")
  
  def remove_dish_from_the_list(self, dish: Dish | list[Dish]):
    if isinstance(dish, Dish):
      if dish in self.order:
        self.order.remove(dish) 
        print(f"{dish} removed")
      elif dish not in self.order:
        print("Check your spelling or make sure the dish you want to remove is in the list")
    elif isinstance(dish, list):
      rejected_dishes = []
      for item in dish:
        if item in self.order:
          self.order.remove(item)
        else:
          rejected_dishes.append(item)
      if len(rejected_dishes) == 0:
        print("Done")
      else:
        print(f"The following have not been found in list (rejected): {rejected_dishes}")

  def return_order_list(self):
    return self.order
  
class Restaurant():
  def __init__(self, orders_all: list[Order], all_restaurant_dishes: list[Dish], available_restaurant_dishes: list[Dish]) -> None:
    self.orders_all = orders_all
    self.all_restaurant_dishes = all_restaurant_dishes
    self.available_restaurant_dishes = available_restaurant_dishes

  def create_new_order(self, customer_name, list_dishes):
    for food in list_dishes:
      if food not in self.available_restaurant_dishes:
        print(f"{food} is not avalible")
        break
    order_no = f"Order number: {len(self.orders_all)}"
    order_no = Order( customer_name, list_dishes)
    self.orders_all.append(order_no)

  def delete_order(self, order_name):
    if order_name in self.orders_all:
      self.orders_all.remove(order_name)
      print("Done")
    elif order_name not in self.orders_all:
      print("This order is not in list.")

  def get_list_of_orders(self):
    return self.orders_all
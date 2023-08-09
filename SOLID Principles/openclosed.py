""" Suppose we have a Product class that represents a generic product, and we want to calculate the
total price of a list of products. Initially, the Product class only has a price attribute, and we can calculate the 
total price of products based on their prices. Now, let's say we want to add a discount feature, where some products might have a 
discount applied to their prices. To add this feature, we would need to modify the existing Product class and the calculate_total_price
function, which violates the Open/Closed Principle. Redesign this program to follow the Open-Closed Principle(OCP) which represents
 “Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification.” """

class Product:
    def __init__(self, price):
        self.price = price

class RegularPricing:
    def calculate_price(self, product):
        return product.price

class DiscountedPricing:
    def __init__(self, discount_percentage):
        self.discount_percentage = discount_percentage

    def calculate_price(self, product):
        discounted_price = product.price * (1 - self.discount_percentage / 100)
        return discounted_price

def calculate_total_price(products, pricing_strategy):
    total_price = 0
    for product in products:
        total_price += pricing_strategy.calculate_price(product)
    return total_price

products = [Product(100), Product(50), Product(75)]

regular_pricing_strategy = RegularPricing()
discounted_pricing_strategy = DiscountedPricing(discount_percentage=10)

print("Total Price (Regular Pricing):", calculate_total_price(products, regular_pricing_strategy))
print("Total Price (Discounted Pricing):", calculate_total_price(products, discounted_pricing_strategy))

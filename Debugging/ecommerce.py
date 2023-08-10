""" Find the cases where the logic to handle adding or removing products from cart fails. Handle these cases after debugging.
Note: Use Python Debugger (pdb) to debug the whole code with the necessary “breakpoint()” function. Use different syntax such as 
where (w), next (n), step (s), continue (c), print (p) etc.
(Hint: Negative quantity should not be allowed to add to cart and non present product should not be allowed to remove)"""

import pdb

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self):
        return self.price * self.quantity

    def update_quantity(self, new_quantity):
        if new_quantity >= 0:
            self.quantity = new_quantity
        else:
            print("Invalid quantity value. Quantity cannot be negative.")

class ShoppingCart:
    def __init__(self):
        self.products = {}

    def add_product(self, product, quantity):
        if product in self.products:
            self.products[product] += quantity
        else:
            self.products[product] = quantity

    def remove_product(self, product, quantity):
        if product in self.products:
            if quantity > 0 and self.products[product] >= quantity:
                self.products[product] -= quantity
                if self.products[product] == 0:
                    del self.products[product]
            else:
                print("Invalid quantity or product not present in the specified quantity.")
        else:
            print("Product not found in the cart.")

    def get_total_cart_price(self):
        total_price = 0
        for product, quantity in self.products.items():
            total_price += product.get_total_price() * quantity
        return total_price

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.shopping_cart = ShoppingCart()

    def add_to_cart(self, product, quantity):
        if quantity > 0: 
            self.shopping_cart.add_product(product, quantity)
        else:
            print("Invalid quantity. Quantity must be positive.")

    def remove_from_cart(self, product, quantity):
        self.shopping_cart.remove_product(product, quantity)

    def checkout(self):
        total_price = self.shopping_cart.get_total_cart_price()
        if total_price > 0:
            print(f"Checking out... Your total is ${total_price}.")
            self.shopping_cart.products = {}
        else:
            print("Your cart is empty. Nothing to checkout.")
            

product1 = Product("Keyboard", 50, 2)
product2 = Product("Mouse", 30, 3)

customer = Customer("Demo Name", "demo.name@example.com")
customer.add_to_cart(product1, 1)
pdb.set_trace()  

customer.add_to_cart(product2, 2)
pdb.set_trace()  # Pause here and inspect the cart after adding the second product

customer.checkout()
pdb.set_trace()  # Pause here to inspect the checkout process

customer.add_to_cart(product1, -1)
pdb.set_trace()  # Pause here to inspect adding a negative quantity to cart

customer.remove_from_cart(product2, 3)
pdb.set_trace()  # Pause here to inspect removing more quantity than present

print("All debugging points have been reached.")

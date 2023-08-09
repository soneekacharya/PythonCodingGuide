""" Suppose we have an interface called PaymentProcessor that defines methods for processing payments and refunds. Then we have a 
class called OnlinePaymentProcessor that implements the PaymentProcessor interface. However, some parts of our system only need to 
process payments and do not handle refunds. Redesign this program to follow the Interface Segregation Principle (ISP) principle
which represents that “Clients should not be forced to depend upon methods that they do not use. Interfaces belong to clients, 
not to hierarchies.” (Hint: Create two different classes in which one class use interfaces for process payment and another
class can process and refund payment both)"""

from abc import ABC, abstractmethod

class PaymentHandler(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class RefundHandler(ABC):
    @abstractmethod
    def process_refund(self, amount):
        pass

class OnlinePaymentProcessor(PaymentHandler):
    def process_payment(self, amount):
        print(f"Processing payment of ${amount}")

class OnlinePaymentRefundProcessor(RefundHandler):
    def process_payment(self, amount):
        print(f"Processing payment of ${amount}")

    def process_refund(self, amount):
        print(f"Processing payment of ${amount}")

def main():
    payment_handler = OnlinePaymentProcessor()
    payment_handler.process_payment(100)

    payment_refund_handler = OnlinePaymentRefundProcessor()
    payment_refund_handler.process_payment(200)

from abc import ABC, abstractmethod

class ICustomerService(ABC):
    @abstractmethod
    def get_customer_by_username(self, username): pass

    @abstractmethod
    def register_customer(self, customer): pass

    @abstractmethod
    def get_all_customers(self): pass

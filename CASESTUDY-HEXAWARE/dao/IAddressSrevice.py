from abc import ABC, abstractmethod

class IAddressService(ABC):
    @abstractmethod
    def get_addresses_by_customer_id(self, customer_id): pass

    @abstractmethod
    def add_address(self, address): pass

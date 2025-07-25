from abc import ABC, abstractmethod

class IVehicleService(ABC):
    @abstractmethod
    def get_all_vehicles(self): pass

    @abstractmethod
    def get_available_vehicles(self): pass

    @abstractmethod
    def get_vehicle_by_id(self, vehicle_id): pass

    @abstractmethod
    def add_vehicle(self, vehicle): pass

    @abstractmethod
    def update_vehicle(self, vehicle): pass

    @abstractmethod
    def delete_vehicle(self, vehicle_id): pass

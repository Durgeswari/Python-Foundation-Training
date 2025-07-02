from abc import ABC, abstractmethod

class IAdminService(ABC):
    @abstractmethod
    def get_admin_by_username(self, username): pass

    @abstractmethod
    def register_admin(self, admin): pass

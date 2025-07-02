from abc import ABC, abstractmethod

class IRoleService(ABC):
    @abstractmethod
    def get_all_roles(self): pass

    @abstractmethod
    def get_role_by_id(self, role_id): pass

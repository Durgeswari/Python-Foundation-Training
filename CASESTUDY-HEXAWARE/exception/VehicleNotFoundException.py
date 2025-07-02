class VehicleNotFoundException(Exception):
    def _init_(self, message="Vehicle not found."):
        super()._init_(message)

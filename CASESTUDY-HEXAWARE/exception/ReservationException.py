class ReservationException(Exception):
    def _init_(self, message="Error occurred during reservation."):
        super()._init_(message)

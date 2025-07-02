class InvalidInputException(Exception):
    def _init_(self, message="Invalid input provided."):
        super()._init_(message)

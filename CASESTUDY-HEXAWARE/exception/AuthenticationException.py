class AuthenticationException(Exception):
    def _init_(self, message="Invalid username or password."):
        super()._init_(message)

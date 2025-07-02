import hashlib
class Customer:
    def __init__(self, customer_id, first_name, last_name, email, phone, username, password_hash, registration_date):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.username = username
        self.password_hash = password_hash
        self.registration_date = registration_date

    def authenticate(self, input_password):
        input_hash = hashlib.sha256(input_password.encode()).hexdigest()
        return self.password_hash == input_hash

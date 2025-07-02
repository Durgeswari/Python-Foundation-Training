import hashlib
class Admin:
    def __init__(self, admin_id, first_name, last_name, email, phone, username, password_hash, role_id, join_date):
        self.admin_id = admin_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.username = username
        self.password_hash = password_hash
        self.role_id = role_id
        self.join_date = join_date
    
    def authenticate(self, input_password):
        input_hash = hashlib.sha256(input_password.encode()).hexdigest()
        print("Expected hash:", self.password_hash)
        print("Entered hash :", input_hash)
        return self.password_hash == input_hash

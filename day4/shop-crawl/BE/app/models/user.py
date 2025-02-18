class User:
    def __init__(self, id, email, password, name, created_at=None):
        self.id = id
        self.email = email
        self.password = password
        self.name = name
        self.created_at = created_at
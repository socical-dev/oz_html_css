class Product:
    def __init__(self, id, category, brand, name, price, created_at=None):
        self.id = id
        self.category = category
        self.brand = brand
        self.name = name
        self.price = price
        self.created_at = created_at
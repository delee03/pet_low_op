class ManageProducts:
    name: str
    price: float
    category: str
    def __init__(self, name: str, price: float, category: str) -> None:
        self.name = name
        self.price = price
        self.category = category
        
    def apply_product(self, discount: float) -> float:
        return self.price - (self.price * discount / 100)
    def get_info(self) -> str:
        return f"Product: {self.name}, Price: {self.price}, Category: {self.category}"
    
product1 = ManageProducts("Laptop", 1000.0, "Electronics")

info = product1.get_info()
print(info)
discount = product1.apply_product(10)
print(f"Discounted price: {discount}")
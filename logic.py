class POSLogic:
    def __init__(self):
        self.cart = {}
        self.prices = {
            "Producto1": 10.0,
            "Producto2": 15.0,
            "Producto3": 20.0,
        }

    def add_to_cart(self, product, quantity):
        if product in self.cart:
            self.cart[product] += quantity
        else:
            self.cart[product] = quantity

    def calculate_total(self):
        total = 0.0
        for product, quantity in self.cart.items():
            if product in self.prices:
                total += self.prices[product] * quantity
        return total

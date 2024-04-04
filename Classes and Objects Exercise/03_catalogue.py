class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name):
        self.products.append(product_name)

    def get_by_letter(self, first_letter):
        return sorted([product for product in self.products if product.startswith(first_letter)])

    def __repr__(self):
        items = '\n'.join(sorted(self.products))
        return f"Items in the {self.name} catalogue:\n{items}"


catalogue = Catalogue("My Catalogue")
catalogue.add_product("Apple")
catalogue.add_product("Banana")
catalogue.add_product("Orange")
catalogue.add_product("Grapes")
catalogue.add_product("Mango")
print(catalogue)

print("Products starting with 'A':", catalogue.get_by_letter('A'))

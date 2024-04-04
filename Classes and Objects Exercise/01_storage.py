class Storage:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []

    def add_product(self, product):
        if len(self.storage) < self.capacity:
            self.storage.append(product)
            print(f"Product {product} added to the storage.")
        else:
            print("Not enough space in the storage to add the product.")

    def get_products(self):
        return self.storage


storage = Storage(5)
storage.add_product("Apple")
storage.add_product("Banana")
storage.add_product("Orange")
storage.add_product("Grapes")
storage.add_product("Mango")  # This will print "Not enough space in the storage to add the product."

print("Products in storage:", storage.get_products())

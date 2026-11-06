from product import Product


class PhysicalProduct(Product):
    """A physical product. Adds a weight attribute to the base Product."""

    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    @property
    def weight(self):
        return self.__weight

    # Method overriding: reuse the parent part, then add our own.
    def display_information(self):
        super().display_information()
        print("  Type: Physical | Weight: " + format(self.__weight, ".2f") + " kg")

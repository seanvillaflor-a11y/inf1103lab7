from product import Product


class DigitalProduct(Product):
    """A digital product. Adds a download_size attribute to the base Product."""

    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        self.__download_size = download_size

    @property
    def download_size(self):
        return self.__download_size

    def display_information(self):
        print("  Type: Digital | Download Size: "
              + format(self.__download_size, ".2f") + " MB")

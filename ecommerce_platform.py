# ecommerce_platform.py

class Product:

    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price


class DiscountableItem:

    def __init__(self, discount_percentage):
        self.discount_percentage = discount_percentage

    def calculate_discount(self, price):
        return price * self.discount_percentage / 100


class TaxableItem:

    def __init__(self, tax_rate):
        self.tax_rate = tax_rate

    def calculate_tax(self, price):
        return price * self.tax_rate / 100


class SaleProduct(Product, DiscountableItem, TaxableItem):

    def __init__(self,
                 product_id,
                 name,
                 price,
                 discount_percentage,
                 tax_rate):

        Product.__init__(self, product_id, name, price)
        DiscountableItem.__init__(self, discount_percentage)
        TaxableItem.__init__(self, tax_rate)

    def final_price(self):

        discount = self.calculate_discount(self.price)

        discounted_price = self.price - discount

        tax = self.calculate_tax(discounted_price)

        return discounted_price + tax

    def display_product(self):

        print("Product ID:", self.product_id)
        print("Name:", self.name)
        print("Original Price:", self.price)
        print("Discount:", self.discount_percentage, "%")
        print("Tax Rate:", self.tax_rate, "%")
        print("Final Selling Price:", self.final_price())


product1 = SaleProduct(
    "P001",
    "Laptop",
    2000,
    10,
    18
)

product1.display_product()

print("\nMRO")
print(SaleProduct.mro())
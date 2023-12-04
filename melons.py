"""Classes for melon orders."""


class AbstractMelonOrder:
    """Base class"""

    def __init__(self, species, qty):
        self.species = species
        self.qty = qty
        self.shipped = False

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5

        if self.species == "Christmas melon":
            base_price = base_price * 1.5
        
        total = (1 + self.tax) * (self.qty) * base_price

        if self.order_type == "international" and self.qty > 10:
            total += 3

        return total
    
    def mark_shipped(self):
        """Record that an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        super().__init__(species, qty)
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
    

class GovernmentMelonOrder(AbstractMelonOrder):
    """A melon order from a US government entity."""

    order_type = "government"
    tax = 0.00

    def __init__(self, species, qty):
        super().__init__(species, qty)
        self.passed_inspection = False
    
    def mark_inspection(self, passed):
        self.passed_inspection = passed
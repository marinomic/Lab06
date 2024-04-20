from dataclasses import dataclass


@dataclass()
class Retailer:
    """
    Class that represents a Retailer object from the table go_retailers in the database
    """
    retailer_code: int
    retailer_name: str
    type: str
    country: str

    def __eq__(self, other):
        return self.retailer_code == other.retailer_code

    def __hash__(self):
        return hash(self.retailer_code)

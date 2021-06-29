"""from ..customer import contact  # ..to add from other folder in tree

contact.email()
"""
# print('Sales initialized', __name__)


def calc_tax():
    pass


def calc_shipping():
    pass


if __name__ == "__main__":  # only in this module __name__ will be __main__ in other modules It will have a name ecommerce.shopping.sales
    print('Sales started')
    calc_tax()
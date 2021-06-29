""" ONE of the ways how to import ecommerce
from sales import calc_shipping, calc_tax

calc_shipping()
calc_tax()

"""
# import app.ecommerce.shopping.sales
# import sys

# app.ecommerce.shopping.sales.calc_shipping()  # to avoid duplication with  ecommerce.sales... let;s use 'from...'
# print(sys.path)  # allows to see the address of packages

# from app.ecommerce.shopping.sales import calc_shipping

# calc_shipping()
"""
# Or if need implement a lot of modules
"""
# from app.ecommerce.shopping import sales

# sales.calc_shipping()

"""
from ecommerce.shopping import sales

#print(dir(sales))
print(sales.__name__)
print(sales.__package__)
print(sales.__file__)


print("we one the right way :=)")
"""

from ecommerce.shopping import sales


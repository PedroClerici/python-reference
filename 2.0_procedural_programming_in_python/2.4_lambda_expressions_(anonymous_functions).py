"""
Lambda Expressions (Anonymous Functions)
"""

# Lambda function example:
a = lambda x, y: x * y
print(a(2, 5))

# Shorting products based in price:
products = [
    ['pan', 13],
    ['milk', 6],
    ['cup', 7],
    ['wine', 50],
    ['candy', 8],
]
# Without lambdas:
# def get_price(item):
#     return item[1]
# products.sort(key=get_price, reverse=True)

# With lambdas:
products.sort(key=lambda product: product[1], reverse=True)
print(products)

# HINT: Sorted is a function that sorts a list without changing
# the original list.
print(sorted(products, key=lambda product: product[1]))

cars = [("Tesla", "$40K"),
        ("BMW", "$65K"),
        ("Ferrari", "$400K")
        ]

prices = list(map(lambda price: price[1], cars))
print(prices)

# lamada take and iterate "price", after ":" we say what we want to "price[1], and then where it sould happens "cars"
# map take it from array and make a new object only with "price[1] variables"
# list make it in list cuž you can NOT print map object

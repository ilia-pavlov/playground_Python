items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)

#items.sort(key=lambda item: item[1]) # parameters(item): expression item[1]
#print(items)


items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]


items.sort(key=lambda something: something[0] )
print(items)


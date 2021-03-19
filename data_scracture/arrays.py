# array like list but for more then 10.000 modules
# check python 3 typecode

from array import array

numbers = array("i", [1, 2, 3])
numbers.append(4)
print(numbers)


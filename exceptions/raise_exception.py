from timeit import timeit

code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age can not be 0 or less")
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:  # 'as' give the object the name, currently 'error'
    pass  # instead of print(error) 
"""

code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age

xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
"""
print("First code = ", timeit(code1, number=10000))  # calculate time of program
print("Second code = ", timeit(code2, number=10000))
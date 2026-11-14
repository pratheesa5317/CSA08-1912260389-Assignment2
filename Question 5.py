def add_item(item, order=None):
    if order is None:
        order = []

    order.append(item)
    return order

def calculate(a, b):
    return a+b, a-b

x = 10

def outer():
    y = 20

    def inner():
        nonlocal y
        y = 30

    inner()
    print("Nonlocal:", y)

print("Order:", add_item("Tea"))
print("Order:", add_item("Coffee"))

add, sub = calculate(20, 10)

print("Addition:", add)
print("Subtraction:", sub)

outer()
print("Global:", x)

import time

items = ["Tea", "Coffee", "Juice", "Milk"]

start = time.perf_counter()

text1 = ""
for item in items:
    text1 += item + ";"

time1 = time.perf_counter() - start

start = time.perf_counter()

text2 = ";".join(items) + ";"

time2 = time.perf_counter() - start

start = time.perf_counter()

text3 = "".join(f"{item};" for item in items)

time3 = time.perf_counter() - start

print("Using +:", text1)
print("Using join:", text2)
print("Using f-string:", text3)

print("Plus time:", time1)
print("Join time:", time2)
print("F-string time:", time3)

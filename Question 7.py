import time

items = ["Item" + str(i) for i in range(10000)]

start = time.perf_counter()

text1 = ""
for item in items:
    text1 += item + ";"

time1 = time.perf_counter() - start

start = time.perf_counter()

text2 = ";".join(items) + ";"

time2 = time.perf_counter() - start

print("Original Output:", text1[:50])
print("Optimised Output:", text2[:50])

print("Same Output:", text1 == text2)

print("Original Time:", time1)
print("Optimised Time:", time2)

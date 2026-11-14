units = int(input("Enter electricity units: "))
ration = input("Ration card (yes/no): ").lower()
age = input("Member above 80 (yes/no): ").lower()

if units <= 100:
    print("Full Subsidy")
elif units <= 200 and ration == "yes":
    print("Partial Subsidy")
elif units > 200 and age == "yes":
    print("No Subsidy")
else:
    print("No Subsidy")

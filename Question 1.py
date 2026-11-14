units = int(input("Enter electricity units: "))
ration_card = input("Ration card available (yes/no): ")
age_above_80 = input("Member above 80 (yes/no): ")

if units <= 100:
    print("Full Subsidy")

elif units <= 200 and ration_card == "yes":
    print("Partial Subsidy")

else:
    print("No Subsidy")

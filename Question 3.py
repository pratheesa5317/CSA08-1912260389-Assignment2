def normalise(text):
    return text.replace(" ", "").replace("-", "").upper()

def validate(reg):
    if len(reg) not in (9, 10):
        return False

    if not reg[:2].isalpha():
        return False

    if not reg[2:4].isdigit():
        return False

    if not reg[4:-4].isalpha():
        return False

    if not reg[-4:].isdigit():
        return False

    return True

number = input("Enter vehicle number: ")
number = normalise(number)

if validate(number):
    print("Valid Registration Number")
else:
    print("Invalid Registration Number")

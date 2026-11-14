def normalise(text):
    text = text.replace(" ", "")
    text = text.replace("-", "")
    return text.upper()

def is_valid(reg):
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

reg = input("Enter vehicle number: ")

reg = normalise(reg)

if is_valid(reg):
    print("Valid Registration Number")
else:
    print("Invalid Registration Number")

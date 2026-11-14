correct_otp = "1234"
attempts = 0

while attempts < 3:
    otp = input("Enter OTP: ")

    if otp == "":
        print("Blank entry")
        continue

    attempts += 1

    if otp == correct_otp:
        print("Login Successful")
        break
    else:
        print("Wrong OTP")

else:
    print("Account Locked for 30 minutes")

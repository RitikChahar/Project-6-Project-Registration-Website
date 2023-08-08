import random

def generate_otp():
    otp = ""
    for i in range(0,6):
        otp += str(random.randint(0, 9))
    return otp

if __name__ == "__main__":
    otp = generate_otp()
    print("Your 6-digit OTP:", otp)

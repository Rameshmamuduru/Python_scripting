import secrets
import string

def generate_otp(length=6, otp_type="digits"):
    """Generate a secure OTP based on given type."""
    
    if otp_type == "digits":
        characters = string.digits
    elif otp_type == "alphanumeric":
        characters = string.ascii_letters + string.digits
    elif otp_type == "strong":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        raise ValueError("Invalid OTP type")

    otp = ''.join(secrets.choice(characters) for _ in range(length))
    return otp


def main():
    print("\n=== Secure OTP Generator ===")
    
    try:
        length = int(input("Enter OTP length (default 6): ") or 6)
    except ValueError:
        print("Invalid input! Using default length 6.")
        length = 6

    print("\nSelect OTP Type:")
    print("1. Digits Only")
    print("2. Alphanumeric")
    print("3. Strong (letters, digits, symbols)")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        otp_type = "digits"
    elif choice == "2":
        otp_type = "alphanumeric"
    elif choice == "3":
        otp_type = "strong"
    else:
        print("Invalid choice! Using digits.")
        otp_type = "digits"

    otp = generate_otp(length, otp_type)
    
    print("\nYour Secure OTP is:", otp)
    print("===========================\n")


if __name__ == "__main__":
    main()

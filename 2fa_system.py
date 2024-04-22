import pyotp
import qrcode

def generate_2fa_secret():
    # Generate a TOTP secret
    secret = pyotp.random_base32()
    
    # Create a TOTP object
    totp = pyotp.TOTP(secret)
    
    # Generate a QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(totp.provisioning_uri(name="User", issuer_name="MyApp"))
    qr.make(fit=True)

    # Display the QR code
    image = qr.make_image(fill='black', back_color='white')
    image.show()

    return secret

def verify_2fa_code(secret, code):
    # Create a TOTP object
    totp = pyotp.TOTP(secret)
    
    # Verify the code
    if totp.verify(code):
        print("Authentication successful!")
    else:
        print("Authentication failed!")

if __name__ == "__main__":
    # Generate a 2FA secret and display the QR code
    secret = generate_2fa_secret()
    
    # Enter the 2FA code from the authenticator app
    code = input("Enter the 6-digit 2FA code from the authenticator app: ")

    # Verify the 2FA code
    verify_2fa_code(secret, code)

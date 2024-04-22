import re
from validate_email_address import validate_email

def validate_email_address(email):
    return validate_email(email)

def check_phishing_signs(headers):
    # Check for suspicious headers like "Reply-To" not matching "From"
    from_email = headers.get("From", "")
    reply_to_email = headers.get("Reply-To", "")
    
    if from_email.lower() != reply_to_email.lower():
        print("[*] Suspicious: 'Reply-To' does not match 'From'")

    # Check for mismatched sender domain and "Return-Path"
    match_from = re.search(r"@([\w.]+)", from_email)
    match_return_path = re.search(r"@([\w.]+)", headers.get("Return-Path", ""))
    
    if match_from and match_return_path and match_from.group(1) != match_return_path.group(1):
        print("[*] Suspicious: Mismatched sender domain and 'Return-Path'")

    # Check for suspicious domains in "From" and "Reply-To"
    if "From" in headers and "Reply-To" in headers:
        from_domain = re.search(r"@([\w.]+)", from_email)
        reply_to_domain = re.search(r"@([\w.]+)", reply_to_email)

        if from_domain and reply_to_domain and from_domain.group(1) != reply_to_domain.group(1):
            print("[*] Suspicious: Different domains in 'From' and 'Reply-To'")

if __name__ == "__main__":
    email = input("Enter the email address to validate: ")

    if not validate_email_address(email):
        print("[*] Invalid email address.")
        exit()

    print("[*] Email address is valid.")

    # Simulated email headers (replace with actual headers from the email)
    headers = {
        "From": "example@example.com",
        "Reply-To": "reply@example.com",
        "Return-Path": "<bounce@example.net>"
    }

    print("\n[*] Checking for phishing signs...")
    check_phishing_signs(headers)

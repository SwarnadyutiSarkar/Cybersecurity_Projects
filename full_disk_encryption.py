import subprocess

def enable_full_disk_encryption():
    """Enable full disk encryption using LUKS."""
    try:
        # Install required packages
        subprocess.run(["sudo", "apt", "install", "-y", "cryptsetup"], check=True)

        # Encrypt disk
        subprocess.run(["sudo", "cryptsetup", "luksFormat", "/dev/sda"], check=True)  # Replace "/dev/sda" with the disk to encrypt
        subprocess.run(["sudo", "cryptsetup", "luksOpen", "/dev/sda", "encrypted_disk"], check=True)

        print("Full disk encryption enabled.")
    except subprocess.CalledProcessError as e:
        print(f"Error enabling full disk encryption: {e}")

if __name__ == "__main__":
    enable_full_disk_encryption()

import base64
import base58
import binascii
import hashlib
import urllib.parse
import subprocess

MAGENTA="\033[35m"
RESET = "\033[0m"
GREEN = "\033[32m"
  
def print_banner():
    
    print(f"{GREEN}##############################################{RESET}")
    print(f"{GREEN}#           Code Cracker v0.1                #{RESET}")
    print(f"{GREEN}#               by Don_Epel                  #{RESET}")
    print(f"{GREEN}##############################################{RESET}")
    print(f"{GREEN}Simple tool to try to decode some text codes{RESET}")
    print(f"{GREEN}Use in case of CTF{RESET}")
    print(f"{GREEN}17-11-2024{RESET}")
    print("\n")


print_banner()

# Input text
input_text = input(f"{GREEN}Enter encoded text: {RESET}")

# Check if input is provided
if not input_text:
    print(f"{GREEN}Usage: python CodeCracker.py <text>{RESET}")
    exit(1)

print(f"{GREEN}Trying to decode the text: '{input_text}'{RESET}")
print(f"{MAGENTA}-------------------------------------------------------{RESET}")


# Hexadecimal Decoding
print("[*] Hexadecimal:")
try:
    # Verifica si los caracteres son válidos para hexadecimal
    if all(char in "0123456789abcdefABCDEF" for char in input_text) and len(input_text) % 2 == 0:
        decoded = binascii.unhexlify(input_text).decode('utf-8')
        print(decoded)
        # Second Hexadecimal decoding attempt (double encoding)
        try:
            print("[*] Second Hexadecimal attempt (double encoding):")
            print(binascii.unhexlify(decoded).decode('utf-8'))
        except (binascii.Error, UnicodeDecodeError):
            print("Not a valid double Hexadecimal encoding")
    else:
        print("Input contains invalid characters or is not a valid Hexadecimal string")
except (binascii.Error, UnicodeDecodeError):
    print("Not a valid Hexadecimal")
print(f"{MAGENTA}-------------------------------------------------------{RESET}")

# ROT3 Decoding
print("[*] ROT3 (Caesar):")
rot3_mapping = str.maketrans(
    'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
    'XYZABCDEFGHIJKLMNOPQRSTUVWxyzabcdefghijklmnopqrstuvw')
decoded = input_text.translate(rot3_mapping)
print(decoded)

if decoded != input_text:
    # Second ROT3 decoding attempt (double encoding)
    double_decoded = decoded.translate(rot3_mapping)
    print("[*] Second ROT3 attempt (double encoding):")
    print(double_decoded)

print(f"{MAGENTA}-------------------------------------------------------{RESET}")

# ROT13 Decoding
print("[*] ROT13 (Caesar):")
decoded = input_text.translate(str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', 
                                              'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'))
print(decoded)
if decoded != input_text:
    # Second ROT13 decoding attempt (double encoding)
    print("[*] Second ROT13 attempt (double encoding):")
    print(decoded.translate(str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', 
                                          'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm')))
print(f"{MAGENTA}-------------------------------------------------------{RESET}")

# Base64 Decoding
print("[*] Base64:")
try:
    decoded = base64.b64decode(input_text).decode('utf-8')
    print(decoded)
    # Second Base64 decoding attempt (double encoding)
    print("[*] Second Base64 attempt (double encoding):")
    print(base64.b64decode(decoded).decode('utf-8'))
except (binascii.Error, UnicodeDecodeError):
    print("Not a valid Base64")

print(f"{MAGENTA}-------------------------------------------------------{RESET}")

# Base58 Decoding
print("[*] Base58:")
try:
    # Verifica si los caracteres son válidos para Base58
    base58_alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    if all(char in base58_alphabet for char in input_text):
        decoded = base58.b58decode(input_text).decode('utf-8')
        print(decoded)
        # Second Base58 decoding attempt (double encoding)
        try:
            print("[*] Second Base58 attempt (double encoding):")
            print(base58.b58decode(decoded).decode('utf-8'))
        except (ValueError, binascii.Error, UnicodeDecodeError):
            print("Not a valid double Base58 encoding")
    else:
        print("Input contains invalid characters for Base58")
except (ValueError, binascii.Error, UnicodeDecodeError):
    print("Not a valid Base58")
print(f"{MAGENTA}-------------------------------------------------------{RESET}")

# Base32 Decoding
print("[*] Base32:")
try:
    decoded = base64.b32decode(input_text).decode('utf-8')
    print(decoded)
    # Second Base32 decoding attempt (double encoding)
    print("[*] Second Base32 attempt (double encoding):")
    print(base64.b32decode(decoded).decode('utf-8'))
except (binascii.Error, UnicodeDecodeError):
    print("Not a valid Base32")

print(f"{MAGENTA}-------------------------------------------------------{RESET}")

# Base85 Decoding
print("[*] Base85 (ASCII85):")
try:
    decoded = base64.a85decode(input_text).decode('utf-8')
    print(decoded)
    # Second Base85 decoding attempt (double encoding)
    print("[*] Second Base85 attempt (double encoding):")
    print(base64.a85decode(decoded).decode('utf-8'))
except (ValueError, binascii.Error, AttributeError, UnicodeDecodeError):
    print("Not a valid Base85 or ASCII85 encoding")

print(f"{MAGENTA}-------------------------------------------------------{RESET}")

# URL Decoding
print("[*] URL Decoding:")
try:
    decoded = urllib.parse.unquote(input_text)
    print(decoded)
    # Second URL decoding attempt (double encoding)
    print("[*] Second URL Decoding attempt (double encoding):")
    print(urllib.parse.unquote(decoded))
except Exception:
    print("Not a valid URL encoding")

print(f"{MAGENTA}-------------------------------------------------------{RESET}")

# Hash Identification
print("[*] Hash Identification:")
try:
    result = subprocess.run(['hashid', input_text], capture_output=True, text=True)
    if result.returncode == 0:
        print(result.stdout)
    else:
        print("Hash Identification: 'hashid' tool is not installed. Use 'pip install hashid' or 'sudo apt-get install hashid'")
except FileNotFoundError:
    print("Hash Identification: 'hashid' tool is not installed. Use 'pip install hashid' or 'sudo apt-get install hashid'")

print(f"{MAGENTA}-------------------------------------------------------{RESET}")

print("Tests completed. If any decoding makes sense, use it.")

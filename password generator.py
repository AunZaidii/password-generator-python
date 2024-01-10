
import random
import string
password=input("Enter password: ")
def check_password_strength(password):
    has_lowercase = any(char.islower() for char in password)
    has_uppercase = any(char.isupper() for char in password)
    has_digits = any(char.isdigit() for char in password)
    has_special_chars = any(char in string.punctuation for char in password)
    if has_lowercase and has_uppercase and has_digits and has_special_chars:
        return "strong"
    elif has_lowercase and has_uppercase and has_digits:
        return "medium"
    else:
        return "weak"
print(check_password_strength(password))

def generate_password(length=12, uppercase=True, lowercase=True, digits=True, special_chars=True):    
    character_set = ""
    if uppercase:
        character_set += string.ascii_uppercase        
    if lowercase:
        character_set += string.ascii_lowercase
    if digits:
        character_set += string.digits
    if special_chars:
        character_set += string.punctuation
    if character_set == ("No").lower():
        raise ValueError("At least one character type must be selected.")
    password = ''.join(random.choice(character_set) for _ in range(length))
    print("Here is your new password: ",password)
    return password

def main():
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter the password length (default is 12): ") or 12)
        uppercase = input("Include uppercase letters? (default is 'Yes'): ").lower() or ('Yes').lower()
        if uppercase == "":
            uppercase == True
        else:
            uppercase == False
        lowercase = input("Include lowercase letters? (default is 'Yes'): ").lower() or ('Yes').lower()
        if lowercase == "":
            lowercase == True
        else:
            lowercase == False    
        digits = input("Include digits? (default is 'Yes'): ").lower() or ('Yes').lower()
        if digits == "":
            digits == True
        else:
            digits == False    
        special_chars = input("Include special characters? (default is 'Yes'): ").lower() or ('Yes').lower()
        if special_chars == "":
            special_chars == True
        else:
            special_chars == False    
        password = generate_password(length, uppercase, lowercase, digits, special_chars)
        strength = check_password_strength(password)
    except ValueError as ve:
        print(f"Error: {ve}")
main()
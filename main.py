import random
import pyperclip
import string

#* The function to generate random strings
def get_random_string():
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(1))
    return result_str

#* The function to generate random numbers
def get_random_number():
    result_num = random.randint(0, 10)
    return result_num

#* The function to generate random characters
def get_random_character():
    charactersAllowed = ["'", "|", "<", ">", "(", ")", "[", "]", "{", "}", ",", ".", "/", "?", "`", "~"]
    result_char = random.choice(charactersAllowed)
    return result_char

#* The function to generate password
def generate_password():
    print()
    result_password = ""
    #? How many digits
    digits = int(input("How long do you want to generate a password? "))
    #* Random sequence
    SEL = [1, 2, 3]
    for digit in range(digits):
        thing = random.choice(SEL)
        if thing == 1:
            result_password += get_random_character()
        elif thing == 2:
            result_password += str(get_random_number())
        elif thing == 3:
            result_password += get_random_string()
    #? Is the password OK
    print()
    print(result_password)
    print()
    POK = input("Is the above password OK? (y/n): ")
    if POK == "y":
        pyperclip.copy(result_password)
        print()
        print("Password copied to clipboard!")
    elif POK == "n":
        generate_password()

#* Calling the function
generate_password()
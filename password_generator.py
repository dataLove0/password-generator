import random
import string

# Asks user if they want numbers and letters in their generated password
try:
    numbers = input("Do you want numbers in your password [Y/N]? ").lower()
    letters = input("Do you want letters in your password [Y/N]? ").lower()
    length = int(input("(8 RECOMMENDED) How much do you want the length? "))
except ValueError:
    print("Invalid value")

# If user is being an idiot
if length == 0:
    print("seriously.")

if numbers == "y" and letters == "y":
    print('Password is:', "".join(random.choices(string.ascii_letters + string.digits, k=length)))

elif numbers == "y" and letters == "n":
    print('Password is:', "".join(random.choices(string.digits, k=length)))

elif numbers == "n" and letters == "y":
    print('Password is:', "".join(random.choices(string.ascii_letters, k=length)))

# Another if user is being an idiot
elif numbers == "n" and letters == "n":
    print("I mean... there is no password without letters and numbers")

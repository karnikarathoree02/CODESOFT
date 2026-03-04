import random
import string

length = int(input("Enter password length: "))

print("Choose password type:")
print("1. Only Letters")
print("2. Letters + Numbers")
print("3. Letters + Numbers + Symbols")

choice = input("Enter choice (1/2/3): ")

if choice == '1':
    characters = string.ascii_letters
elif choice == '2':
    characters = string.ascii_letters + string.digits
elif choice == '3':
    characters = string.ascii_letters + string.digits + string.punctuation
else:
    print("Invalid choice!")
    exit()

password = ''.join(random.choice(characters) for _ in range(length))

print("Generated Password:", password)

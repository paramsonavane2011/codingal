import random
len = int(input("Enter the length of the password: "))
mix = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
password = ""
for i in range(len):
    password += random.choice(mix)

print(f"Password: {password}")
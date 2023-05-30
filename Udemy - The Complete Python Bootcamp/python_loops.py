# =====FOR LOOPS=====
# for letter in ["Python", "java", "javascript", "sql"]:
#     print(letter)

# =====RANGE=====
# r = range(1, 10)
# print(list(r))

# sum = 0
# for n in range(100):
#     sum += n
# print(sum)

# for _ in range(10):
#     print("do something", _)

# =====PASSWORD GENERATOR=====
# import random
# import string
# chars = string.ascii_letters+string.digits+string.punctuation
# # print(random.choice(chars))

# char_length = int(input("Password length: "))
# password = ""

# for _ in range(char_length):
#     char = random.choice(chars)
#     password += char
# print(password)

# =====FOR, CONTINUE=====
# for letter in "Python Goooo!":
#     if letter == "o":
#         continue
#     print(letter, end="")

# =====FOR, BREAK=====
# for letter in "Python Goooo!":
#     if letter == "o":
#         break
#     print(letter, end="")

# ===== WHILE LOOP=====
# x = 0
# while x < 10:
#     print("winner")
#     x += 1
#     if x == 9:
#         print("winner", x)
#         continue

# print("Hi there! I\'m Andrei.")
# print("Hi there! I'm Andrei.")
# message = "This is a string"
# print(type(message))

# MULTIPLE LINE STRING
# multiline_string = """I like Python
# multiple line
# string.
# """

# print(multiline_string)
# print("a\nb\nc\td\te")

# GETTING USER INPUT
# name = input("Please enter your name: ")
# print(name)

# CONVERTING TYPES
# miles = input("Enter value in miles: ")  # miles will be in string
# miles_to_float = (float(miles))
# km = miles_to_float * 1.609
# print(km)

# STRING INDEXING
movie = "The GodFather"
age = 54
# print(movie[2])
# print(movie[-1])  # -1 is the index of the last letter
# print(len(movie))

# strings are immutable
# -this is not allowed-
# movie[1] = "x"

# CONCATENATING AND REPEATING STRINGS
# print("#"*10)
# print(movie*5)

# STRING SLICING
# string_variable[start:stop]
# start - included
# stop - excluded
print(movie[0:9])
print(f"{movie} {age}")

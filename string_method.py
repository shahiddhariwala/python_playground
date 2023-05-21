# capitalize()
# Converts the first letter of a string to uppercase.
"hello world".capitalize()
'Hello world'

# casefold()
# Converts a string to all lowercase.
"HELLO WORLD".casefold()
'hello world'

# center()
# Centers a string in a specified width, padding it with spaces on the left and right.
"hello world".center(20, " ")
'  hello world  '

# count()
# Returns the number of times a substring appears in a string.
"hello world".count("l")
2

# endswith()
# Returns True if a string ends with a specified substring.
"hello world".endswith("d")
False

# expandtabs()
# Converts tabs in a string to spaces.
"hello\tworld".expandtabs()
'hello world'

# find()
# Returns the index of the first occurrence of a substring in a string.
"hello world".find("o")
2

# format()
# Formats a string using a specified format string.
"This is {0} string".format("formatted")
'This is formatted string'

# index()
# Returns the index of the first occurrence of a substring in a string, raising an exception if the substring is not found.
"hello world".index("o")
2

# isalnum()
# Returns True if a string contains only alphanumeric characters.
"hello123".isalnum()
True

# isalpha()
# Returns True if a string contains only alphabetic characters.
"hello".isalpha()
True

# isdecimal()
# Returns True if a string contains only decimal characters.
"123".isdecimal()
True

# isdigit()
# Returns True if a string contains only digits.
"123".isdigit()
True

# islower()
# Returns True if a string contains only lowercase characters.
"hello".islower()
True

# isspace()
# Returns True if a string contains only whitespace characters.
" ".isspace()
True

# istitle()
# Returns True if a string is titlecase.
"Hello World".istitle()
True

# isupper()
# Returns True if a string contains only uppercase characters.
"HELLO".isupper()
True

# ljust()
# Left-justifies a string in a specified width, padding it with spaces on the right.
"hello world".ljust(20, " ")
'hello world    '

# lower()
# Converts a string to all lowercase.
"HELLO WORLD".lower()
'hello world'

# lstrip()
# Strips whitespace characters from the left of a string.
" hello world".lstrip()
'hello world'

# replace()
# Replaces all occurrences of a substring in a string with a new substring.
"hello world".replace("world", "universe")
'hello universe'

# rfind()
# Returns the index of the last occurrence of a substring in a string.
"hello world".rfind("o")
5

# rindex()
# Returns the index of the last occurrence of a substring in a string, raising an exception if the substring is not found.
"hello world".rindex("o")
5

# rjust()
# Right-justifies a string in a specified width, padding it with spaces on the left.
"hello world".rjust(20, " ")
'    hello world'

# rstrip()
# Strips whitespace characters from the right of a string.
"hello world  ".rstrip()
'hello world'

# split()
# Splits a string into a list of substrings, using a specified delimiter.
"hello world".split()
['hello', 'world']

# startswith()
# Returns True if a string starts with a specified substring.
"hello world".startswith("hello")
True

# strip()
# Strips whitespace characters from the left and right of a string.
" hello world ".strip()
'hello world'

# swapcase()
# Swaps the case of all characters in a string.
"hello world".swapcase()
'HELLO WORLD'

# title()
# Converts the first letter of each word in a string to uppercase.
"hello world".title()
'Hello World'

# upper()
# Converts a string to all uppercase.
"hello world".upper()
'HELLO WORLD'

# zfill()
# Fills a string with zeros on the left, up to a specified width.
"123".zfill(5)
'00123'

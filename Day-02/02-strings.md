# Strings

**1. String Data Type in Python:**

- In Python, a string is a sequence of characters, enclosed within single (' '), double (" "), or triple (''' ''' or """ """) quotes.
- Strings are immutable, meaning you cannot change the characters within a string directly. Instead, you create new strings.
- You can access individual characters in a string using indexing, e.g., `my_string[0]` will give you the first character.
- Strings support various built-in methods, such as `len()`, `upper()`, `lower()`, `strip()`, `replace()`, and more, for manipulation.

**2. String Manipulation and Formatting:**

- Concatenation: You can combine strings using the `+` operator.
- Substrings: Use slicing to extract portions of a string, e.g., `my_string[2:5]` will extract characters from the 2nd to the 4th position.
- String interpolation: Python supports various ways to format strings, including f-strings (f"...{variable}..."), %-formatting ("%s %d" % ("string", 42)), and `str.format()`.

Example:
text = 'learn python'
num = 20
print(f"{text} in {num}")   or   print("{} in {}".format(text, num))  or  print("%s in %d"%(text, num))
%s - string, %d - integer

- Escape sequences: Special characters like newline (\n), tab (\t), and others are represented using escape sequences.
\n: Represents a newline character.
\t: Represents a tab character.
\r: Represents a carriage return character. The carriage return character (\r) is an escape sequence used in strings to instruct the output device to return the cursor to the beginning of the current line. When encountered in a string, it moves the cursor to the beginning of the line, allowing subsequent characters to overwrite the existing characters from the start of the line.
\\: Represents a backslash character.
\": Represents a double quote character within a double-quoted string.
\': Represents a single quote character within a single-quoted string.

Example:
text = '''learn python'''
num = 20
print(text + '\n' + "quickly")    ---> learn python
                                        quickly 
print(text + '\t' + "quickly")    ---> learn python    quickly
print(text + '\r' + "quickly")    --> quicklyython
print(text + '\\' + "quickly")   ---> learn python\quickly
print(text + '\"' + "quickly")   ---> learn python"quickly
print(text + '\'' + "quickly")   ---> learn python'quickly

- String methods: Python provides many built-in methods for string manipulation, such as `split()`, `join()`, and `startswith()`.
Example:
text = 'learn python'
print(text.split(" "))   ---> ['learn', 'python']
print(text.split(" ")[0]) ---> learn
print(text.join("st"))  ---> slearn pythont
print(text.join("str"))  --> slearn pythontlearn pythonr
print(text.startswith("l"))   --> True
print(text.startswith("L"))   ---> False    --- because it is case sensitive
print(text.startswith("p"))   ---> False
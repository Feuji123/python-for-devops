# Numberic Data Type

**1. Numeric Data Types in Python (int, float):**

- Python supports two primary numeric data types: `int` for integers and `float` for floating-point numbers.
- Integers are whole numbers, and floats can represent both whole and fractional numbers.
- You can perform arithmetic operations on these types, including addition, subtraction, multiplication, division, and more.
- Be aware of potential issues with floating-point precision, which can lead to small inaccuracies in calculations.
- Python also provides built-in functions for mathematical operations, such as `abs()`, `round()`, and `math` module for advanced functions.

Example:
num = -5
print(abs(num))    ---> 5
num = 5.87453045934
print(round(num))  ---> 6
num = 5.47453045934
print(round(num))    ---> 5
print(round(num,2))   ---> 5.47

import math
print(math.sqrt(16))  ---> 4.0
print(math.pi)   ----> 3.141592653589793
print(math.sin(math.pi/2))  ---> 1.0

import math as m
print(m.factorial(5))   --> 120
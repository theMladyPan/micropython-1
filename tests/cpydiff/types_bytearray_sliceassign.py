"""
categories: Types,bytearray
description: Array slice assignment with unsupported RHS
cause: Unknown
workaround: Unknown
"""

b = bytearray(4)
b[:1] = [1, 2]
print(b)

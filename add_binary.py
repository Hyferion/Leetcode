"""Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"


Constraints:

Each string consists only of '0' or '1' characters.
1 <= a.length, b.length <= 10^4
Each string is either "0" or doesn't contain any leading zero."""


def addBinary(a, b):
    llen = max(len(a), len(b))
    diff = abs(len(a) - len(b))
    carry = 0
    result = ""
    if len(a) > len(b):
        b = ''.join(('0' * (diff), b))  # Insert '0' at the beginning of the string
    elif len(a) < len(b):
        a = ''.join(('0' * (diff), a))
    for i in range((llen - 1), -1, -1):
        if (int(a[i]) + int(b[i]) + carry) == 2:
            result = ''.join(('0', result))
            carry = 1
        elif (int(a[i]) + int(b[i]) + carry) == 3:
            result = ''.join(('1', result))
            carry = 1
        elif (int(a[i]) + int(b[i]) + carry) == 1:
            result = ''.join(('1', result))
            carry = 0
        elif (int(a[i]) + int(b[i]) + carry) == 0:
            result = ''.join(('0', result))
            carry = 0
    if carry == 1:
        result = ''.join(('1', result))
    return result if len(result) else "0"


addBinary("1010", "1011")

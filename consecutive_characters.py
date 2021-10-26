"""
Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.

Return the power of the string.
"""


def maxPower(s):
    max_Power = 1
    curr_power = 1

    for index, char in enumerate(s):
        print(char)
        if index + 1 < len(s):
            if char == s[index + 1]:
                curr_power = curr_power + 1
            else:
                curr_power = 1

            if curr_power > max_Power:
                max_Power = curr_power
    return max_Power


maxPower("cc")

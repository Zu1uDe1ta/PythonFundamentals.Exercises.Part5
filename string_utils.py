
"""
Given a string parameter, this function should return the length of the parameter.
"""
def str_len(str_in: str) -> str:
    return len(str_in)

"""
Given a string parameter, this function should return the first letter of the parameter.
"""
def first_char(str_in: str) -> str:
    return str_in[0]

"""
Given a string parameter, this function should return the last letter of the parameter..
"""
def last_char(str_in: str) -> str:
    return str_in[-1]


"""
This function determines if the substring exists within the string. Returns True or False.
"""
def input_has_substring(str_in: str, sub_str_in: str) -> bool:
    if str_in.find(sub_str_in) >= 0:
        return True
    elif input_has_substring.find() == -1:
        return False



"""
Returns the substring of a string.

Keyword arguments:
str_in -- the string in which to generate a substring from
start -- starting position of the input parameter to start the substring (inclusive)
stop -- stopping position of the input parameter to stop the substring (exclusive)
"""
def substring(str_in: str, start: int, stop: int) -> str:
    return substring(str_in, 0, -1)


"""
Given a string parameter, this function returns the same string back with each letter having the opposite case.
Example:
When input = "Python" the function returns "pYTHON"
"""
def opposite_case(str_in: str) -> str:
    result = []
    for letter in str_in:
        if letter.isupper():
            result.append(letter.lower())
        else:
            result.append(letter.upper())
    return "".join(result)
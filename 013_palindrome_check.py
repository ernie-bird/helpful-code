import string
def pal(x=None):
    if x is None:
        return ValueError("Missing argument")
    n = str(x)
    if n == "":
        return True
    for char in n:
        if char in string.punctuation:
            return ValueError("Punctuation not allowed")
    if n == n[::-1]:
        return True
    return False

pal("aba")

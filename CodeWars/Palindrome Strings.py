def is_palindrome(string):
    string = list(str(string))
    return string[::] == string[::-1]


print(is_palindrome("anna"))
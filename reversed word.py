
def reverse_words(s):
    s = s.split(" ")
    reverse = " ".join(reversed(s))
    return reverse



print(reverse_words("hello world!"))
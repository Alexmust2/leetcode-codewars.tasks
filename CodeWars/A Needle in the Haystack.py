def find_needle(haystack):
    needle = "needle"
    if needle in haystack:
        index = haystack.index("needle")
        return f"found the needle at position {index}"



print(find_needle(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]))
def ensure_question(s):
    if "?" not in s:
        return s+"?"
    return s


print(ensure_question("Yes"))
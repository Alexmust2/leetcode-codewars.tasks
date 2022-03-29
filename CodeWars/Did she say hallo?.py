def validate_hello(greetings):
    if "salut" in greetings.lower():
        return True
    if "hello" in greetings.lower():
        return True
    if "ciao" in greetings.lower():
        return True
    if "hallo" in greetings.lower():
        return True
    if "hola" in greetings.lower():
        return True
    if "ahoj" in greetings.lower():
        return True
    if "czesc" in greetings.lower():
        return True
    return False
print(validate_hello('hallo, salut'))
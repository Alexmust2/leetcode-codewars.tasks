def validate_usr(username):
    if len(username) < 4 or len(username) > 16 or username.lower() != username or " " in username or ",.'" in username:
        return False
    return True


print(validate_usr("________"))
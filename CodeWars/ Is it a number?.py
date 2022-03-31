def isDigit(string):
    if string == "" or string == " ":
        return False
    if "-" == string[0] or "-" == string[0] and "." in string or "." in string:
        string = string.replace(".","")
        return string[1:].isdigit()
    return string.isdigit()
    
        
    



print(isDigit("3.0"))
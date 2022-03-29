def html_special_chars(data):
    for i in data:
        if i == "<":
            data = data.replace("<", "&lt;")
        if i == ">" :
            data = data.replace(">", "&gt;")
        if i == '"':
            data = data.replace('"', "&quot;")
        if i == "&":
            data = data.replace("&", "&amp;")
    return data


print(html_special_chars(("<h2>Hello World</h2>")))
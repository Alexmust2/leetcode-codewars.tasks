def to_freud(sentence):
    ls = ["sex"]
    sentence = sentence.split()
    if len(sentence) > 0:
        return " ".join(ls * len(sentence))




print(to_freud("This is a test"))
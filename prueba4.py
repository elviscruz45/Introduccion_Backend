def alphabet_position(text):
    alp = "abcdefghijklmnopqrstuvwxyz"
    return " ".join([str(alp.find(c) + 1) for c in text.lower() if c in alp])



text="The sunset sets at twelve o' clock."
alp = "abcdefghijklmnopqrstuvwxyz"
string=[str(alp.find(c) + 1) for c in text.lower() if c in alp]

string1=" ".join([str(alp.find(c)+1) for c in text.lower() if c in alp])

print(string1)
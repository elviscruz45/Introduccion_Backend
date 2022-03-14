def get_count(sentence):
    lista=["a","e","i","o","u"]
    dic=[sentence.count(i) for i in set(sentence) if i in lista]
    return(sum(dic))

print(get_count("holaaaaoouue"))
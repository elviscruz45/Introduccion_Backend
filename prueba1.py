def disemvowel(string):
    caract=["a","e","i","o","u","A","E","I","O","U",]
    string1=list(string)
    string2=[]
    for i in string1:
        if i not in caract:
            string2.append(i)
        
            
    string3="".join(string2)
    
    return string3


print(disemvowel("This website is for losers LOL!"))

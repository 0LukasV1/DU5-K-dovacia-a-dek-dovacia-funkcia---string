# sifrovanie
def sif(t,pos):
    a=""
    for i in range(0,len(t)):
        if t[i] != " ":
            x=ord(t[i])
            y=((((x-97)+pos)%26)+97)
            a+=chr(y)
        else:
            a+=" "
    return a

print(sif("ahoj mato",1))

#desifrovanie
def desif(text):
    a=""
    for i in range(1,26):
        for h in range(0,len(text)):
            if text[h] != " ":
                x = ord(text[h])
                y = ((((x - 97) + i) % 26) + 97)
                a += chr(y)
            else:
                a+=" "
        print(a,end="\n")
        a=""

print(desif(sif("ahoj mato",5)))

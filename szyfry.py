def cezar(tekst, przesuniecie):
    alfabet ="abcdefghijklmnoprsuvz" #napisz tu dokladny alfabet :D
    koncowy_tekst =""
    for i in tekst.lower():
        koncowy_tekst+=(alfabet[alfabet.index(i)+przesuniecie])
    return koncowy_tekst
def podstawieniowy(tekst, alfabet_2):
    alfabet ="abcdefghijklmnoprsuvz" #napisz tu dokladny alfabet :D
    koncowy_tekst=""
    for i in tekst.lower():
        koncowy_tekst+=alfabet_2[alfabet.index(i)]
    return koncowy_tekst
def deZKluczem(kod, klucz):
    alfabet ="abcdefghijklmnoprsuvz" #napisz tu dokladny alfabet :D
    deszyfr =""
    tmp =0
    tab =[]
    for i in klucz.lower():
        tab.append(alfabet.index(i))
    for i in kod.lower():
        deszyfr+=alfabet[alfabet.index(i)-1 - tab[tmp]]
        tmp = tmp+1
    return deszyfr
        
        
        
        
masz =cezar("ab",2)
print(masz)
masz =podstawieniowy("ab","asddsfghialmnossuvsz")
print(masz)
masz =deZKluczem("ce", "ac")
print(masz)

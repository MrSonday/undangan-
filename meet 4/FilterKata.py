newWord = []

kataKata = [ "kami","kita","kalian","mereka","kamu","anda"]
jumlah = 0
for kata in kataKata : 
    if kata[:1] == "k":
        newWord.append(kata)

print( newWord )
arquivo_entrada = open('letra.txt','r')
for i in arquivo_entrada:
    linha = i.rstrip()
    print(counter(linha,"A"))

def counter(word,letter):
    count = 0
    for l in word:
        if l == letter:
            count = count + 1
    return count


friends = ["jose", 'maria', 'pedro']

for friend in friends:
    print ('Happy new year', friend)


for i in range (len(friends)) : 
    friend  = friends [i]
    print ("Happy new year", friend)


## monta uma lista de palavras sem repetição a partir do arquivo

fname = input("Enter file name: ")
fh = open(fname)
palavras = []

for line in fh:
    partes = line.split()
    for palavra in partes:
        if palavra not in palavras:
            palavras.append(palavra)

palavras.sort()
print(palavras)

# Filtra apenas linhas que começam com "From ", ignora o resto com continue, usa split() para pegar o e-mail (posição 1) e conta quantas linhas válidas existem

fname = input("Enter file name: ")
fh = open(fname)
count = 0

for line in fh:
    line = line.rstrip()
    if not line.startswith("From "):
        continue
    partes = line.split()
    count = count + 1

    print(partes[1])


print("There were", count, "lines in the file with From as the first word")

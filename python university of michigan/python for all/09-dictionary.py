# Tenta pegar a chave 'candy' no dicionário.
# Se a chave não existir, o método get() retorna o valor padrão (-1).
# Como o dicionário está vazio e 'candy' não existe, o resultado será -1.

stuff = dict()
print(stuff.get("candy", -1))


# Criando um dicionário com chaves (nomes) e valores (números)
jjj = {"chuck": 1, "fred": 42, "jan": 100}

# list(jjj) retorna apenas as chaves do dicionário
print(list(jjj))

# keys() também retorna todas as chaves do dicionário
print(list(jjj.keys()))

# values() retorna apenas os valores
print(list(jjj.values()))

# items() retorna pares (chave, valor) em forma de tuplas
print(list(jjj.items()))


counts = dict()

names = ["csev", "cwen", "csev", "zqian", "cwen"]

for name in names:
    counts[name] = counts.get(name, 0) + 1

print(counts)
# get() pega o valor da chave no dicionário sem dar erro se ela não existir (pode retornar um valor padrão)


# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = input("Enter file:")
handle = open(name)
dicionario = {}
for line in handle:
    if not line.startswith("From "):
        continue
    partes = line.split()
    mail = partes[1]
    dicionario[mail] = dicionario.get(mail, 0) + 1
bigcount = None
bigmail = None
for mail, count in dicionario.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigmail = mail
print(bigmail, bigcount)
# Programa lê um arquivo de email (mbox) e conta quantas mensagens cada remetente enviou.
# Usa um dicionário onde a chave é o email e o valor é a quantidade de mensagens.
# Depois percorre o dicionário para encontrar o remetente com o maior número de emails.
# Por fim imprime o email com a maior contagem.

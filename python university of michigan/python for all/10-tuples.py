# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.                     From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008                                                                                  Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
handle = open(name)
counts = dict()
for line in handle:
    if not line.startswith("From "):
        continue

    partes = line.split()
    horario = partes[5]
    horario = horario.split(":")
    counts[horario[0]] = counts.get(horario[0], 0) + 1


lst = list()
for key, val in counts.items():
    tupla = (key, val)
    lst.append(tupla)

for val, key in sorted(lst):
    print(val, key)


# Este programa lê um arquivo de emails e analisa apenas as linhas que começam com "From ".
# A partir dessas linhas, ele extrai o horário de envio da mensagem (formato HH:MM:SS),
# separa apenas a hora (HH) e conta quantas vezes cada hora aparece usando um dicionário.
# Depois converte o dicionário em uma lista de tuplas (hora, quantidade),
# ordena os resultados e imprime quantos emails foram enviados em cada hora do dia.

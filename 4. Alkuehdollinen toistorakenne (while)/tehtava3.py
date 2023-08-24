list = []
while True:
    luku = input("Anna luku: ")
    if luku == "":
        break
    else:
        list.append(luku)

for i in range(0, len(list)):
    list[i] = int(list[i])
pienin = min(list)
suurin = max(list)
print("Pienin luku " + str(pienin))
print("Suurin luku " + str(suurin))
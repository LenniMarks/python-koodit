leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

lasku_vaihe1 = leiviskat * 20
lasku_vaihe2 = lasku_vaihe1 + naulat
lasku_vaihe3 = lasku_vaihe2 * 32
lasku_vaihe4 = lasku_vaihe3 + luodit
lasku_vaihe5 = lasku_vaihe4 * 13.3

kilot = int(lasku_vaihe5 // 1000)
grammat = lasku_vaihe5 % 1000
grammat = "%.2f" % round(grammat, 2)
print(str(kilot) + " kilogrammaa ja " + str(grammat) + " grammaa.")



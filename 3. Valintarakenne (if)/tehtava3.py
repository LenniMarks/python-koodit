sukupuoli = input("Anna sukupuolesi: ")
gl = int(input("Anna hemoglobiini arvosi: "))

if sukupuoli == "Mies" and gl > 133 and gl < 197:
    print("Hemoglobiini arvosi on normaali")
elif sukupuoli == "Mies" and gl < 134:
    print("Hemoglobiini arvosi on alhainen")
elif sukupuoli == "Mies" and gl > 196:
    print("Hemoglobiini arvosi on korkea")
elif sukupuoli == "Nainen" and gl > 116 and gl < 176:
    print("Hemoglobiini arvosi on normaali")
elif sukupuoli == "Nainen" and gl < 117:
    print("Hemoglobiini arvosi on alhainen")
elif sukupuoli == "Nainen" and gl > 175:
    print("Hemoglobiini arvosi on korkea")



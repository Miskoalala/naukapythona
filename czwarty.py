samochody = ["syrena", "opel","mazda"]
print(samochody[2])
print(samochody[0])
print(samochody[1])

for s in samochody:
    print(s)

for idx in range(len(samochody)):
    print("idx" + str(idx) + ":" + samochody[idx])

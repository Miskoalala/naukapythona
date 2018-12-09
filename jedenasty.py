samolot = {"name": "boeing",
           "przebieg": 10000,
           "type": "pasazerski"}
print(samolot["name"])
for key, value in samolot.iteritems():
    print("{0}:{1}".format(key, value))

print(samolot["nieznany_klucz"])

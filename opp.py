class Hayvon:
    def __init__(self, laqabi, turi, yoshi):
        self.laqabi = laqabi
        self.turi = turi
        self.yoshi = yoshi

    def __str__(self):
        return f"Laqabi:{self.laqabi} Turi: {self.turi} Yoshi : {self.yoshi}"

h1 = Hayvon("bo'rivoy", "It", 12)
h2 = Hayvon("momiqvoy", "mushuk", 10)
h3 = Hayvon("firdavs", "yo'lbars", 9)
h4 = Hayvon("qirol", "sher", 15)
h5 = Hayvon("abdurahmon", "maymun", 3)

print(h1)
print(h2)
print(h3)
print(h4)
print(h5)

class Car:
    def __init__(self, nomi, padidsiyai, turi):
        self.nomi = nomi
        self.padidsiyai = padidsiyai
        self.turi = turi

    def __str__(self):
        return f"Nomi:{self.nomi} Padidsiyasi: {self.padidsiyai} Turi : {self.turi}"

h1 = Car("lanborghini aventador", "sport", "lanborghini")
h2 = Car("porsche 911", "sport", "porsche")
h3 = Car("land cruser", "lux", "tayota")
h4 = Car("palisade", "full", "hyundai")
h5 = Car("malibu", "lux", "chevrolet")

print(h1)
print(h2)
print(h3)
print(h4)
print(h5)

class Tel:
    def __init__(self, nomi, turi):
        self.nomi = nomi
        self.turi = turi

    def __str__(self):
        return f"Nomi:{self.nomi} Turi : {self.turi}"

h1 = Tel("a12", "samsung",)
h2 = Tel("iphone 13 pro", "iphone")
h3 = Tel("xiomi note12t", "redmi")
h4 = Tel("reno 7 lite", "oppo")
h5 = Tel("p59 pro", "xuawei")

print(h1)
print(h2)
print(h3)
print(h4)
print(h5)







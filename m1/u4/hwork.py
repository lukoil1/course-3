class Converter:
    def __init__(self):
        kurs = int(input("Введіть курс долара"))
        suma = int(input("Введіть суму для обміну"))
        vubir = int(input("1 - долари у гривні / 2 - гривні у долари "))
        if vubir == 1:
            finish1 = suma* kurs
            print(finish1)
        else:
            finish2 = suma/ kurs
            print(finish2)
            
converter = Converter()
            
        
def hello(name ,  birthday):
    print("Hello", name, birthday )
    year_old = 2024 - birthday
    return year_old
    
    
lukian = hello("Lukian", 2008)
Vova = hello("Vova", 2003)
print(lukian)
print(Vova)
print(lukian + Vova)

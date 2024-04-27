balans = int(input("Введіть поточний баланс картки"))
pokupka = input("Хочете зробити покупку?")
while pokupka == 'так':
    price = int(input("Введіть ціну"))
    if balans >= price:
        balans = balans - price
        print("Сума", price, "грн. списана з рахунку.")
    else:
        print("На вашому рахунку недостатньо коштів")
    pokupka = input("Хочете зробити покупку?")
print("Дякуємо що користувались peoplebank!")
    
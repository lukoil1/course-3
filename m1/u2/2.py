password = 'World_of_Code'
data = '_1234567890AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
for symbol in password:
    pos = data.find(symbol) + 1
    print('Код символу', symbol, '-', pos)
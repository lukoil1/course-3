def function(start, finish):
    for i in range(start, finish+1): 
        
        
        if i%2  == 1:
            print(i, "― міжнародний конкурс «Стартап року»")
        else:
            print(i, "cерії конференцій та круглих столів з експертами")



start = int(input("Рік початку співпраці з фондом"))
finish = int(input("Рік закінчення співпраці з фондом"))
function(start, finish)
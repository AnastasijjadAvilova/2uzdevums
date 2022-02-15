summa = 0
x = int(input("Введите количество нечетных чисел для суммы: "))
for y in range(1,x+1):
 print( (2*y - 1))
 summa += (2*y - 1) 
print("Cумма равна: " + str(summa))
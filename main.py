x = int(input("Введи целое положительное число: "))
if x<0:
    print("Неправильно введено число")
for i in range(x):
    i+=1
    if i%2==0:
       print ("Четные числа: ",i)
     


#Daniel Frolov TA-20V
# Номер задачи: 7.2, Номер страници: 114, Номер варианта: 7
# Назвние задачника: СБОРНИК ЗАДАЧ ПО ПРОГРАММИРОВАНИЮ
""" Текст задачи: Определить, есть ли в заданной строке символ цифра.
Вывести сообще-ние об этом."""


y = open("ZADA4A_DANIEL_FROLOV.txt")
a = y.read()
n = 0
for i in a: # При  помощи цикла for проходимся по тексту 
    if i.isdigit(): # Если в тексте находится цифра, то к n прибавляеться 1
        n = n + 1

if n >= 1:  # Если n больше или равно 1 то в тексте есть цифры.
    print("В тексте есть цифры(а), их кол-во = ",  n)
else:
    print("В тексте не имееться цифр")
        

#Пробовал на текстах с большим колвом цифр и без цифр

            
        
    
    
    

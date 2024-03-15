import random

def get_numbers_ticket(min, max, quantity):
    #Перевіряємо коректність вхідних даних
    if not (1 <= min <= max <= 1000 and 1 <= quantity <= (max - min + 1)):
        return[]
    
    #Генеруємо унікальні випадкові числа у вказаному діапазоні
    numbers = random.sample(range(min, max + 1), quantity)
    #Сортуємо числа
    numbers.sort()
    return numbers


#Приклад використання 
# lottery_numbers = get_numbers_ticket(1, 49, 6)
# print("Ваші лотерейні числа:", lottery_numbers)

lottery_numbers = get_numbers_ticket(1, 36, 5)
print("Ваші лотерейні числа:", lottery_numbers)

def solve(numheads, numlegs):
   
    rabbits = (numlegs - (numheads * 2)) // 2
   
    chickens = numheads - rabbits
    
   
    if chickens < 0 or rabbits < 0 or (2 * chickens + 4 * rabbits != numlegs):
        return "Нет решения"
    
    return chickens, rabbits


numheads = int(input("Введите количество голов: "))
numlegs = int(input("Введите количество ног: "))


result = solve(numheads, numlegs)
print("Ответ:", result)

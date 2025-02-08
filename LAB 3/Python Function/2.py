def fartocel(F):
    
    cel = (5/9) * (F - 32)
    return cel  

F = float(input()) 
cel_value = fartocel(F)

print(cel_value)

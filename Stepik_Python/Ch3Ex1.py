x = input()

def f(x):
    y = float(x)
    if y <= -2:
        return 1 - (y + 2)**2
    elif -2 < y <= 2:
        return -(y / 2)
    elif y > 2:
        return (y -2) ** 2 + 1

f(x) 

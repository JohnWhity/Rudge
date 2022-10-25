file = open("Numbers", 'r')
try:
    while True:
        x = int(file.readline())
        y = x**2
        print(y)
        if x == "":
            break
except(ValueError):
    print()
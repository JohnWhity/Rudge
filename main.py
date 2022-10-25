file = open("Numbers", 'r')
c = 0
try:
    while True:
        x = int(file.readline())
        y = x**2
        print(y)
        c += 1
        if x == "":
            break
except(ValueError):
    print(c)


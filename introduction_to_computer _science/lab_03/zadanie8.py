import random
if __name__ == '__main__': 

g = int(input("Podaj prosze jaka wysokosc ma miec twoja choinka: "))

# b - choinka

for i in range(g):
    for _ in range(g-i):
        print(" ", end="")
    for _ in range(2*i+1):
        print("*", end="")
    print()
print()

# c ozdoby
for i in range(g):
    for a in range(g-i):
        print(" ", end="")
    for b in range(2*i+1):
        if i == 0:
            print("X", end='')
            continue
        else:
            losowa = random.randrange(1, i+1)
            if(losowa == b):
                print("o", end="")
            print("*", end="")
    print()
print()
# d ozdoby  pień

for i in range(g):
    for a in range(g-i):
        print(" ", end="")
    for b in range(2*i+1):
        if i == 0:
            print("X", end='')
            continue
        else:
            losowa = random.randrange(1, i+1)
            if(losowa == b):
                print("o", end="")
            print("*", end="")
    print()
for i in range(g):
    print(" ", end="")
print("U")


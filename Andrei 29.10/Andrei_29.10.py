a = [0]*4 
import random
for i in range (4):
    ver = 0
    while (ver==0):
        player = int(input("1 - kivi, 2 - käärid, 3 - paaber. "))
        if (player == 1 or player == 2 or player == 3):
            ver = 1
    a[i] = player     
    if player == 1:
        print("Olete valinud kivi.")
    if player == 2:
        print("Sa valisid käärid.")
    if player == 3:
        print("Valisite paberi.")
    comp = random.randint(1,3)
    if comp == 1:
        print("Arvuti valis kivi.")
    if comp == 2:
        print("Arvuti valis käärid.")
    if comp == 3:
        print("Arvuti valitud paber.")
    if player == comp:
        win = 0
    if player == 1 and comp == 2:
        win = 1 
    if player == 1 and comp == 3:
        win = 2
    if player == 2 and comp == 1:
        win = 2
    if player == 2 and comp == 3:
        win = 1
    if player == 3 and comp == 1:
        win = 1
    if player == 3 and comp == 2:
        win = 2
    if win == 0:
        print("viik!")
    if win == 1:
        print("Võitis mängija!")
    if win == 2:
        print("Võitnud arvuti!")
print (a)
k = 0
n = 0
b = 0
for i in range (4):
    if a[i] == 1:
        k = k+1
    if a[i] == 2:
        n = n+1
    if a[i] == 3:
        b = b+1
ver = 0
comp = 1
if k>2:
    comp=3
if n>2:
    comp = 1
if b>2:
    comp = 2
    
while (ver==0):
    player = int(input("1 - kivi, 2 - käärid, 3 - paaber. "))
    if (player == 1 or player == 2 or player == 3):
        ver = 1
if player == 1:
        print("Olete valinud kivi.")
if player == 2:
        print("Olete valinud käärid.")
if player == 3:
        print("Oled valinud oma paber")
if comp == 1:
        print("Arvuti valis kivi.")
if comp == 2:
        print("Arvuti valis käärid.")
if comp == 3:
        print("Arvuti valis paber.")
if player == comp:
        win = 0
if player == 1 and comp == 2:
        win = 1 
if player == 1 and comp == 3:
        win = 2
if player == 2 and comp == 1:
        win = 2
if player == 2 and comp == 3:
        win = 1
if player == 3 and comp == 1:
        win = 1
if player == 3 and comp == 2:
        win = 2
if win == 0:
        print("viik!")
if win == 1:
        print("Võitis mängija!")
if win == 2:
        print("Võitnud arvuti!")



v1=["kivi, käärid, paber"]
v2=["kivi, käärid, paber"]
if m==1:
    while True:
        print("Kas mängime? esc välja, enter-mangime")
        if read_key()=="esc":
            break
        elif read_key()=="enter":
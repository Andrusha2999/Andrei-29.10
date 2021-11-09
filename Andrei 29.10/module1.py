from keyboard import *
from random import *
from module1 import *
def start():
            """Teeme valik kellega mängime 
            Tagastame m muutuja int formaadis
 
            :rtype: int 
            """
            print("kivi, käärid, Paber")
            m=3
            while m not in [1,2]:
                try:
                    m=int(input("kellega mängime?\n1-botid \n2-robotiga"))
                except:
                    ValueError
            return m
 

def bot_vs_bot (v1:list,v2:list):
    """Robotie mäng
    tagastame m muutuja int formaadis
    :param list v1:jarjend esimese roboti jäoks
    :param list v1:jarjend teine roboti jäoks
            """ 
    while True:
        print("Играем? esc= выходим, enter= играем")
        if read_key()=="esc":
            break
        elif read_key()=="enter":
            p1=choice(v1)
            print("Первый Бот: ",p1)
            p2=choice(v2)
            print("Второй Бот: ",p2)
            if p1==p2:
                print("Ничья")
            elif p1==v1[0] and p2==v2[1] or p1==v1[2] and p2==v2[0] or p1==v1[1] and p2==v2[2]:
                print("Выйграл 1")
            else:
                print("Выйграл 2")

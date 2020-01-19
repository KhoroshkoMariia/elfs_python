import uuid
from elf import Elf
from gift import Gift
import random
christmasCoin = 100
elves_list = []
gift_list = []

level = 1
def add_elf():
    global elves_list
    id = str(uuid.uuid4())
    name = str(input("podaj imie elfa \n "))
    elf = Elf(id, name, level)
    elves_list.append(elf)
    print("Dodano : " + str(elf))
    menu()

def show_elf():
    a = 0
    for i in range(len(elves_list)):
        print(str(elves_list[i]) + str(" numer Elfa: ") + str(a))
        a = a + 1


def upgrade_elf():
    global christmasCoin
    global elves_list
    print(" Wybierz numer Elfa dla Ulepszenai: \n")
    show_elf()
    choice_elf = int(input(" Wybierz Elfa, ktorego chcesz ulepszyc : \n"))
    number = random.randint(7, 8)
    print("wylosowano liczbe " + str(number))
    if elves_list[choice_elf].level <= 4 and christmasCoin > 10:
        elves_list[choice_elf].level += 1
        christmasCoin = - 10
        print("Poziom elfa zmieniono na: " + str(elves_list[choice_elf].level))
    elif elves_list[choice_elf].level > 4 and christmasCoin > 15:
        elves_list[choice_elf].level += 1
        christmasCoin = - 15
        print("Poziom elfa zmieniono na: " + str(elves_list[choice_elf].level))
    else:
        print(" Niewystarczajaca ilosc christmasCoin ")




def produce_gift():
    global christmasCoin
    global gift_list
    global elves_list
    name = input(" Wprowadz nazwe prezentu: \n ")
    difficulty = int(input(" podaj poziom trudnosci prezentu\n"))
    gift = Gift(name, difficulty)
    sum =0
    for i in range(len(elves_list)):
        sum = sum + int(elves_list[i].level)
        print("suma leveli : " +str(sum))
        if (difficulty <= sum) and ((christmasCoin - difficulty * 3) >= 0):
            christmasCoin -= difficulty * 3
            gift_list.append(gift)
            print("Wyprudukowano prezent " + name)

        else:
            print("Niewystarczajco srodkow albo poziomu elfow dla wyprodukowania prezentu")

    menu()

def list_of_produced_gifts():
    for i in range(len(gift_list)):
        print(str(gift_list[i]))
    menu()


def menu():
    print("""==================Menu======================
1. Dodaj Elfa
2. Wyświetl Elfy
3. Ulepsz elfa
4. Wyprodukuj prezent
5. Lista wytworzonych prezentów \n""")

    choise = int(input())

    if (choise == 1):
        add_elf()
    elif (choise == 2):
        show_elf()
    elif (choise == 3):
        upgrade_elf()
    elif (choise == 4):
        produce_gift()
    elif (choise == 5):
        list_of_produced_gifts()
    menu()

menu()









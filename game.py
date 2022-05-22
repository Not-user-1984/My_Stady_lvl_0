import random

while True:
    user = input('Играем, Твой ход: камень, бумага, ножницы:  ')
    comp_list = ["камень","бумага","ножницы"]
    comp_rand = random.choice(comp_list)
    print(f"\nТвой ход {user}, Я выбрал {comp_rand}.")

    if user == comp_rand:
        print(f'Ты {user} и я {comp_rand} ,Ничья!!')

    elif user == "камень":
        if comp_rand == "ножницы":
            print("Камень сточил мои ножницы,Ты выиграл!!")
        else:
            print("Я обернул твой Камень,ТЫ лось")

    elif user == "бумага":
        if comp_rand == "камень":
            print("Бумага обернула мой Камень,Ты выиграл!!")
        else:
            print("Чик Чик твою Бумагу,Ты лось")    

    elif user == "ножницы":
        if comp_rand == "бумага":
            print("Чик Чик мою Бумагу,Ты выиграл!!")
        else:
            print("Тупые ножницы не дело,ТЫ лось")

    play_roud = ''
    play_roud = input('Еще? Д/Н  ')
    if  play_roud.lower() != 'д':
        break
print("0")

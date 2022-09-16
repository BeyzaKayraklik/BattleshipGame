import random
import os
import time


def menu():
    choice = question()
    processing(choice)
def processing(choice):
    shot = 0
    # for f in choice:
    if choice == "1":
        game(shot, choice)
    elif choice == "2":
        print("Not active yet")
    elif choice == "3":
        game(shot, choice)
    elif choice == "4":
        shot = 100
        game(shot, choice)
        print("easy")
    elif choice == "5":
        shot = 25
        game(shot, choice)
        print("middle")
    elif choice == "6":
        shot = 2
        game(shot, choice)
        print("hard")
    return shot and choice


def question():
    while True:
        # choice = ()
        print("==Welcome To BattleShip Game =====")
        print("  1, for Play Game;")
        print("  2, for High Score;")
        print("  3, for Version 2;")
        print(" Settings ")
        print("  |---> 4, for Easy Mode;(40 shot)")
        print("  |---> 5, for Middle Mode;(25 shot)")
        print("  |---> 6, for Hard Mode;(10 shot)")
        choice = input("-->", )
        print(f"choice: {choice}")
        if choice[0] >= "1" and choice[0] <= "7" and len(choice) == 1:
            break
        print("Choice must be, between 1-7, not ", choice + ".")
        print("Try again.")
        print()

    print()
    return choice


def game(shot, choise):
    rows, cols = 10, 10

    my_matrix = [(["_"] * cols) for i in range(rows)]
    counter = 0
    score = 1

    def print_board(my_matrix):
        for i in range(0, 10):
            print(i, end=" ")
        print()
        for i in my_matrix:
            print(" ".join(i))

    def ship_create(ship_size):
        shplist = []
        rand = random.choice([True, False])

        if rand:
            col = random.randint(0, len(my_matrix) - 1)  # 0 dahil !
            row = random.randint(0, len(my_matrix) - ship_size - 1)
        else:
            col = random.randint(0, len(my_matrix) - ship_size - 1)
            row = random.randint(0, len(my_matrix) - 1)

        for i in range(ship_size):
            if rand:
                shplist.append((row + i, col))
            else:
                shplist.append((row, col + i))
        return shplist

    def unique(shplist):
        unique_list = []
        for x in shplist:
            if x not in unique_list:
                unique_list.append(x)
            else:
                print(x)
                return x

        return len(unique_list)

    def control(counter, shot):
        start_timer = time.time()
        while True:
            guessed_row = int(input("Please enter a row:"))
            guessed_col = int(input("Please enter a col:"))
            tuple_guess = (guessed_row - 1, guessed_col - 1)
            # if len(tuple_guess) != 2:
            #     continue

            os.system("cls")

            # shiplistte bulunduğu matrise karşılık gelen değer

            if tuple_guess in shplist:
                my_matrix[guessed_row][guessed_col] = "X"
                shplist.remove(tuple_guess)

                print(shplist)

                print_board(my_matrix)
                counter += 1
                shot -= 1
                print(f"Game Step:: {counter} ")

                if shot == 0:
                    os.system("cls")
                    print("!!Game Over!!")

                    end_timer = time.time()
                    game_time = end_timer - start_timer
                    print(f"Game Time :: {format(end_timer - start_timer, '.0f')}s ")

                    print(f"Game Step :: {counter}")
                    score = (1 / game_time) * (1 / counter) * 100
                    print(f"Score ::{format(score, '.0f')}")

                    again = str(input("Do you want to play again (type yes or no): "))
                    if again == "yes":
                        os.system("cls")
                        game(shot, choise)
                    else:
                        os.system("cls")
                        menu()
                    break
            else:
                if 0 < guessed_row > 10 or 0 < guessed_col > 10:

                    print("Out-of-field values entered")
                else:
                    my_matrix[guessed_row][guessed_col] = "/"

                    print_board(my_matrix)
                    counter += 1
                    shot -= 1
                    if shot == 0:
                        os.system("cls")
                        print("!!Game Over!!")
                        end_timer = time.time()
                        game_time = end_timer - start_timer
                        print(f"Game Time :: {format(end_timer - start_timer, '.0f')}s ")

                        print(f"Game Step :: {counter}")
                        score = (1 / game_time) * (1 / counter) * 100
                        print(f"Score ::{format(score, '.0f')}")

                        again = str(input("Do you want to play again (type yes or no): "))
                        if again == "yes":
                            os.system("cls")
                            game(shot, choise)
                        else:
                            os.system("cls")
                            menu()
                        break
                    print("==FAILED SHOT==")
                    print(f"Game Step :: {counter}")

            if len(shplist) == 0:

                print("♛♛♛CONGRATULATIONS YOU SINK ALL SHIPS♛♛♛")
                end_timer = time.time()
                game_time = end_timer - start_timer
                print(f"{format(end_timer - start_timer, '.0f')}s")
                print(counter)
                score = (1 / game_time) * (1 / counter) * 100
                print(score)
                print("=" * 25)
                again = str(input("Do you want to play again (type yes or no): "))
                if again == "yes":
                    os.system("cls")
                    # return 4
                    game(shot, choise)
                else:
                    os.system("cls")
                    menu()
                break

    def control_2(choise):
        while True:
            guessed_row = int(input("Please enter a row:"))
            guessed_col = int(input("Please enter a col:"))
            tuple_guess = (guessed_row - 1, guessed_col - 1)

            # shiplistte bulunduğu matrise karşılık gelen değer

            if tuple_guess in shplist:
                if tuple_guess in ship2:
                    for i in ship2:
                        my_matrix[i[0]][i[1]] = "X"
                        shplist.remove(i)
                    print(shplist)

                    print_board(my_matrix)

                    print("tebrikler 1 . gemiyi batırdınız")

                if tuple_guess in ship3:
                    for i in ship3:
                        shplist.remove(i)
                    print(shplist)
                    print(my_matrix[guessed_col][guessed_row])
                    print("tebrikler 2 . gemiyi batırdınız")

                if tuple_guess in ship4:
                    for i in ship4:
                        shplist.remove(i)

                    print(shplist)

                    print(my_matrix[guessed_col][guessed_row])
                    print("tebrikler 3 . gemiyi batırdınız")

                # del shplist[]

            else:
                if guessed_row > 10 and guessed_col > 10:
                    print("alan dışı değerler girildi")

                else:
                    print("vuramadın")
                    if len(shplist) == 0:
                        print("tebrikler tüm gemileri batırdınız")
                        break

    print_board(my_matrix)

    ship2 = ship_create(ship_size=2)
    ship3 = ship_create(ship_size=3)
    ship4 = ship_create(ship_size=4)


    # ship2 = [(5, 6), (1, 6)]
    # ship3 = [(5, 5), (6, 6), (5, 7)]
    # ship4 = [(8, 2), (6, 6), (8, 4), (8, 5)]


    shplist = ship4 + ship3 + ship2
    print(ship2)
    print(ship3)
    print(ship4)
    print(shplist)



    while unique(shplist) != len(shplist):
        print("çakışma var")
        # shplist.clear()
        # shplist = []
        if unique(shplist) in ship2:
            ship2 = ship_create(ship_size=2)
        elif unique(shplist) in ship3:
            ship3 = ship_create(ship_size=3)
        elif unique(shplist) in ship4:
            ship4 = ship_create(ship_size=4)


        shplist = ship4 + ship3 + ship2
        print(ship2)
        print(ship3)
        print(ship4)
        print(shplist)

    if choise == "3":
        control_2(choise)
    else:
        control(counter, shot)

    unique(shplist)


if __name__ == '__main__':
   menu()

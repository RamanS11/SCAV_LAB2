from get_rel_info import get_info
from rename_video import rename_video
from resize import resize
from codec_change import change


def print_menu():

    print('What you want to do?')
    print(30 * "-", "MENU", 30 * "-")
    print("1. Get relevant information.")
    print("2. Rename quality cuts.")
    print("3. Resize video quality.")
    print("4. Change codec")
    print("5. Exit")
    print(67 * "-")

    while True:
        try:
            y = input()
            res = int(y)
            print("Option selected: ", res)
        except ValueError:  # just catch the exceptions you know!
            print('That\'s not a number!')
        else:
            if 1 <= res <= 5:  # this is faster
                break
            else:
                print('Out of range. Try again')
    return res

def lab2():

    loop = True
    while loop:  # While loop which will keep going until loop = False
        choice = print_menu()  # Displays menu
        print('escogido: '+str(choice))

        if choice == 1:
            print("1. Get relevant information.")
            get_info()
        elif choice == 2:
            print("2. Rename quality cuts.")
            rename_video()
        elif choice == 3:
            print("3. Resize video quality.")
            resize()
        elif choice == 4:
            print("4. Change codec")
            change()
        elif choice == 5:
            loop = False  # This will make the while loop to end as not value of loop is set to False
        else:
            print("Wrong option selection. Enter any key to try again..")


if __name__ == '__main__':
    lab2()

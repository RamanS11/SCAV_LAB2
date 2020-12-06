import os

def compute(quality, in_file, out_file):

    os.system(" ffmpeg -i " + in_file + " -filter:v scale=" + quality + ":-1 -c:a copy " + out_file + '.mp4')


def resize():

    print("\nSelect the video you want to resize:")

    direc = '.'
    allfiles = os.listdir(direc)
    aux = 1
    names = []

    for f_name in allfiles:
        if f_name.endswith('.mp4'):
            names.append(f_name)
            print(aux, f_name)
            aux = aux + 1

    while True:
        try:
            x = int(input('Pick a video >>> '))
        except ValueError:  # just catch the exceptions you know!
            print('That\'s not a number!')
        else:
            if 1 <= x < len(names):  # this is faster
                break
            else:
                print('Out of range. Try again')
    in_name = names[int(x)-1]

    print('Introduce the new width (one resolution component): ')
    y = input()
    try:
        res = int(y)
        print("New resolution selected: ", res)
    except ValueError:
        print(
            "This is not a valid number. Better luck next time!")

    print('Introduce the new video name: ')
    z = input()
    try:
        out_name = str(y)
        print("New video: ", out_name)
    except ValueError:
        print(
            "This is not a valid number. Better luck next time!")

    compute(y, in_name, z)


if __name__ == '__main__':
    resize()

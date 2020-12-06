import os

def compute(select, in_file, out_file, codec):

    # os.system('ffmpeg -i ' + in_file + ' -c:v libvpx-vp9 -b:v 2M -pass 1 -an -f null /dev/null && '
    #          'ffmpeg -i ' + in_file + ' -c:v libvpx-vp9 -b:v 2M -pass 2 -c:a libopus ' + out_file)

    if select:
        os.system('ffmpeg -i ' + in_file + ' -c:v ' + codec + ' ' + out_file)
    else:
        os.system('ffmpeg -i ' + in_file + ' -c:a ' + codec + ' ' + out_file)


def change():

    while True:
        try:
            sel = int(input('Which type of codec you want to change? 1: Audio, 2: Video \n'))
        except ValueError:  # just catch the exceptions you know!
            print('That\'s not a number!')
        else:
            if 1 <= sel <= 2:  # this is faster
                break
            else:
                print('Out of range. Try again')

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

    vid_codecs = ['vp3', 'vp8', 'vp9', 'av1']
    aud_codecs = ['mp3', 'libvorbis', 'libopus']

    print('Introduce the codec you want to use: ')
    aux = 1

    if sel == 1:

        selector = True
        for f_name in aud_codecs:
            print(aux, f_name)
            aux = aux + 1

        while True:
            try:
                x = int(input('Select codec >>> '))
            except ValueError:  # just catch the exceptions you know!
                print('That\'s not a number!')
            else:
                if 1 <= x <= len(aud_codecs):  # this is faster
                    break
                else:
                    print('Out of range. Try again')
        codec = aud_codecs[int(x) - 1]

    else:

        selector = True
        for f_name in vid_codecs:
            print(aux, f_name)
            aux = aux + 1

        while True:
            try:
                x = int(input('Select codec >>> '))
            except ValueError:  # just catch the exceptions you know!
                print('That\'s not a number!')
            else:
                if 1 <= x <= len(vid_codecs):  # this is faster
                    break
                else:
                    print('Out of range. Try again')
        codec = vid_codecs[int(x) - 1]

    print('Introduce the new video name (remember to add the extension, e.g. if you want to change the audio codec to '
          'mp3, output name: MP3_codec_change.mp4) >>> ')
    out_name = input()

    compute(selector, in_name, out_name, codec)


if __name__ == '__main__':
    change()

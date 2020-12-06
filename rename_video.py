import os

def rename(name, quality):
    # Create aux variables needed.
    direc = '.'
    allfiles = os.listdir(direc)
    files = [fname for fname in allfiles if fname.endswith('.mp4')]

    for i in files:
        # Create info.txt file with the info of the video.
        os.system('touch info.txt')
        os.system('ffmpeg -i ' + i + ' 2> info.txt')

        # Open the file with all the video information.
        file = open('info.txt', 'r')
        z = 'Duration'
        x = 'Stream #0:0'
        dur = ''
        qua = ''

        # Find relevant information related to Duration, bit rate ... by searching the line that starts with 'Duraton'.
        for line in file:
            if z in line:
                # Copy the information in the text file that store this information
                d = line.split(',')[0]
                dur = d.split()[1]
            elif x in line:
                q = line.split(',')[2]
                qua = q.split(' ')[1]
        # Close the information file.
        # print('Dur: '+dur+' duration_string: '+'00:00:10.07'+' qua: '+qua+' Quality_original: '+quality)
        if dur == '00:00:10.07' and qua == quality:
            print(os.getcwd() + '/' + name+'.mp4')
            os.rename(os.getcwd() + '/' + i, os.getcwd() + '/' + name+'.mp4')
            break

        file.close()
        os.system('rm info.txt')

def rename_video():

    # Create arrays to iterate over them.
    scale = '1280x720,640x480,360x240,160x120'
    # Force the user to select one option.
    while True:
        try:
            x = int(input('Which video quality you want to rename?: 1: 1280x720, 2: 640x480, 3: 360x240, 4: 160x120 \n'))
        except ValueError:  # just catch the exceptions you know!
            print('That\'s not a number!')
        else:
            if 1 <= x < 4:  # this is faster
                break
            else:
                print('Out of range. Try again')
    # Get the output name from the user.
    y = input('With what name?: \n')
    print(scale.split(',')[int(x)-1])
    rename(y, scale.split(',')[int(x)-1])


if __name__ == '__main__':
    rename_video()

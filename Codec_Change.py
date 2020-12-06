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
import os

def get_codecs(video_info, summary):
    # Open the file with all the video information.
    file = open(video_info, 'r')
    z = 'Stream'
    summary.write("Codecs used in the video :\n")

    # Find the codecs used by searching where the line starts with a 'Stream' string.
    for line in file:
        if z in line:
            # Copy the information in the text file that store this information
            summary.write(line)
    # Close the information file.
    file.close()


def get_info(video_info, summary):
    # Open the file with all the video information.
    file = open(video_info, 'r')
    z = 'Duration'
    summary.write("Other relevant information:\n")

    # Find relevant information related to Duration, bit rate ... by searching the line that starts with 'Duraton'.
    for line in file:
        if z in line:
            # Copy the information in the text file that store this information
            summary.write(line)
            break

    # Close the information file.
    file.close()


def store_info(vid_name, file):
    # Create a file that stores all the video information.
    os.system('ffmpeg -i ' + vid_name + ' 2> ' + file)


def get_rel_info():
    vid_name = 'BBB.mp4'
    out_file = 'info_BBB.txt'
    summary_file = 'summary_info.txt'

    # Call the function that creates the information file.
    store_info(vid_name, out_file)
    # Create a file where we will store a short version of the video information.
    os.system("touch " + summary_file)

    # Open the file previously created and fill with the important information
    summary = open(summary_file, 'w')
    get_codecs(out_file, summary)
    get_info(out_file, summary)
    # Close the file.
    summary.close()

    # Delate the large text file with all the video information.
    os.system("rm " + out_file)


if __name__ == '__main__':
    get_rel_info()

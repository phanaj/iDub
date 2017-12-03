from speech import *
from download import *

'''
  Given YouTube URL and directory `person`, updates the global dict with new mappings
'''
def addToDict(url, person):
    curr_dir = "/home/ubuntu/workspace/Voices/"
    new_dir = curr_dir + person

    makeandmove(new_dir)
    makedir(new_dir + "/Videos")
    makedir(new_dir + "/Audio")

    # saves YouTube video in "Videos"
    downloadVideo(url, new_dir + "/Videos")

    # converts all .mp4's in "Videos" to .wav files in "Audio"
    toWav(new_dir+"/Videos", new_dir+"/Audio")

if __name__ == "__main__":
    print(os.getcwd())
    url = "https://www.youtube.com/watch?v=HN0HoiZ3Q6U"
    addToDict(url, "yale")
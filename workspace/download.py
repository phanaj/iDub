import glob, os
import subprocess
from speech import *
from pytube import YouTube

def makedir(new_dir):
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)

def makeandmove(new_dir):
    makedir(new_dir)
    os.chdir(new_dir)

def downloadVideo(url, outDir):
    """ Downloads a video from youtube as an webm into the current working directory when given the url. """

    # Moves to given directory
    os.chdir(outDir)

    # Create a YouTube object
    yt = YouTube(url)

    # Filters to find only mp4 streams
    #yt.streams.filter(mime_type="video/mp4").all()

    #print(yt.streams)

    # Filters to find only mp4 streams
    # Take the first mp4 video
    stream = yt.streams.filter(mime_type="video/mp4").first()
    stream.download()
    print(os.getcwd())
    for file in glob.glob("*.mp4"):
        if len(file) > 7:
            file_num = len(os.listdir(outDir)) - 1
            os.rename(file, str(file_num) + ".mp4")

def extractWav(file):
    """ Input file in the format of FILENAME.mp4 and it'll output it as FILENAME.wav """
    """ Output file has no spaces. """
    print(os.getcwd())
    #file_num = len(os.listdir(outDir))
    newfile = file.replace(" ", "\ ")
    newfile = "~/workspace/Videos/" + newfile
    print(file)
    filename = find_between(newfile, "~/workspace/Videos/", ".mp4")
    print(newfile)
    newfilename = str(file_num)

    #command = 'ffmpeg -i ' + newfile + ' -ab 160k -ac 2 -ar 44100 -vn '+ newfilename +'.wav'
    command = 'ffmpeg -i ' + newfile + ' -ab 160k -ac 1 -ar 44100 -vn -nostats -loglevel 0 '+ newfilename +'.wav'
    subprocess.call(command, shell=True)

# Converts all .mp4 files in `dir` to .wav
def toWav(inDir, outDir):
    os.chdir(inDir)
    file_num = len(os.listdir(outDir))
    for file in glob.glob("*.mp4"):
        if int(os.path.splitext(file)[0]) < file_num:
            continue
        fileName = os.path.splitext(file)[0]
        inFile = os.getcwd() + "/" + fileName
        print("Out: " + outDir)
        print("Num: " + str(file_num))

        makeandmove(outDir+"/"+str(file_num))
        outFile = os.getcwd() + "/" + fileName + '.wav'

        command = 'ffmpeg -y -i "' + inFile + '.mp4" -ab 160k -ac 1 -ar 44100 -vn -nostats -loglevel 0 "'+ outFile +'"'
        subprocess.call(command, shell=True)
        dict_dir = "/home/ubuntu/workspace/Voices/" + outDir.split("/")[5] + "/dict.txt"
        print(dict_dir)
        wavToDict(outFile, dict_dir, file_num)


def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

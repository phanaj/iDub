from ffmpy import FFmpeg
import os
from collections import defaultdict
import pickle
import string
from postvideo import *

def load_dict(voice):
    dict_dir = "/home/ubuntu/workspace/Voices/" + voice + "/dict.txt"
    try:
        with open(dict_dir, 'rb+') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return dict()

'''
  Add Clips of each word to Working folder
'''
def addstitch(inputseg, outputsegct, startstamp, timefromstart):
    ff = FFmpeg(
        inputs={inputseg: None},
        outputs={outputsegct: '-ss '+ (str) (startstamp) + ' -t ' + (str) (timefromstart) + ' -vcodec libx264 -crf 23 -avoid_negative_ts 1 -c:a copy -bsf:v h264_mp4toannexb -f mpegts -y'}
    )
    ff.cmd
    ff.run()
    return

'''
  Mixes the word-videos together into a single bigmeme
'''
def concatout(vidct):
    outstr = "-i 'concat:"
    fcmplx = ""
    for i in range(0, vidct):
        outstr = outstr+"Working/intermed"+(str)(i)+".ts"
        if(i < vidct - 1):
            outstr = outstr+"|"
        else:
            outstr = outstr+"'"
    os.system("ffmpeg " + outstr + " -c copy -bsf:a aac_adtstoasc -y Output/bigmeme.mp4")
    return

'''
  Produces a video featuring the desired meme sentence in the chosen voice
'''
def makememe(voice, saythis):
    vidinputs = load_dict(voice)
    print(vidinputs)
    vidcount = 0
    corrfactor = 0.05
    for segct in range(0, len(saythis)):
        thisword = vidinputs.get(saythis[segct])
        if (thisword != None):
            startcode = thisword[0][1]
            endcode = thisword[0][2]
            addstitch("Voices/" + (str) (voice) + "/Videos/"+ (str) (thisword[0][0]) + ".mp4", "Working/intermed" + (str) (segct) +".ts", (str) (startcode), (str) (endcode + corrfactor - startcode))
        else:
            bing = "Videos/trumpbingbong.mp4"
            #Expansion Possibility: Randomly pick a Bing to insert
            startcode = 40.25
            endcode = 40.75
            addstitch(bing, "Working/intermed" + (str) (segct) +".ts", (str) (startcode), (str) (endcode - startcode))
        vidcount = vidcount + 1
    concatout(vidcount)
    postVideo("bigmeme.mp4")

#{'did': [[0, 0.0, 0.2]], 'everybody': [[0, 0.2, 0.5], [0, 2.1, 3.0]], 'see': [[0, 0.5, 0.8]], 'the': [[0, 0.8, 0.9], [0, 1.6, 1.7000000000000002], [0, 21.3, 22.3], [0, 37.2, 37.3]], "president's": [[0, 0.9, 1.3]], 'State': [[0, 1.3, 1.5]], 'of': [[0, 1.5, 1.6], [0, 28.9, 29.0]], 'Union': [[0, 1.7000000000000002, 2.0], [0, 29.2, 29.3]], 'Address': [[0, 2.0, 2.1]], 'I': [[0, 7.2, 7.5], [0, 8.7, 8.8], [0, 9.4, 9.4], [0, 11.1, 11.3], [0, 13.7, 14.0], [0, 20.3, 20.6], [0, 24.4, 24.4], [0, 26.2, 26.5]], 'thought': [[0, 7.5, 7.8]], 'it': [[0, 7.8, 7.9], [0, 10.9, 11.1], [0, 11.7, 11.8], [0, 12.1, 12.1]], 'was': [[0, 7.9, 8.0], [0, 9.4, 9.5], [0, 11.8, 11.9], [0, 12.1, 12.3], [0, 14.0, 14.7]], 'fantastic': [[0, 8.0, 8.7]], "haven't": [[0, 8.8, 9.3]], 'said': [[0, 9.3, 9.4]], 'a': [[0, 9.5, 9.5]], 'little': [[0, 9.5, 9.6]], 'surprised': [[0, 9.6, 10.1], [0, 14.7, 15.2]], 'by': [[0, 10.1, 10.3]], 'how': [[0, 10.3, 10.5]], 'he': [[0, 10.5, 10.7], [0, 15.3, 15.5]], 'ended': [[0, 10.7, 10.9]], "don't": [[0, 11.3, 11.4], [0, 36.7, 36.8]], 'know': [[0, 11.4, 11.6]], 'if': [[0, 11.6, 11.7]], 'cuz': [[0, 11.9, 12.1]], 'his': [[0, 12.3, 12.4]], 'last': [[0, 12.4, 12.7]], 'one': [[0, 12.7, 13.2]], 'but': [[0, 13.2, 13.5]], 'boy': [[0, 13.5, 13.7]], 'when': [[0, 15.2, 15.3]], "doesn't": [[0, 15.5, 15.8]], 'care': [[0, 15.8, 15.9]], 'anymore': [[0, 15.9, 16.1]], "he's": [[0, 16.1, 16.5], [0, 16.5, 16.6]], 'done': [[0, 16.6, 16.9]], 'now': [[0, 16.9, 17.0]], 'so': [[0, 17.0, 17.3]], 'strange': [[0, 17.3, 19.7]], 'because': [[0, 19.7, 20.3]], 'believe': [[0, 20.6, 21.0]], 'in': [[0, 21.0, 21.1]], 'you': [[0, 21.1, 21.3], [0, 36.6, 36.7]], 'American': [[0, 22.3, 22.7]], 'people': [[0, 22.7, 23.2]], 'and': [[0, 23.2, 23.8]], "that's": [[0, 23.8, 24.0]], 'why': [[0, 24.0, 24.4]], 'stand': [[0, 24.4, 24.8]], 'here': [[0, 24.8, 25.0]], 'as': [[0, 25.0, 25.3], [0, 26.1, 26.2]], 'confident': [[0, 25.3, 26.1]], 'have': [[0, 26.5, 26.7]], 'ever': [[0, 26.7, 26.9]], 'been.': [[0, 26.9, 28.3]], 'The': [[0, 28.3, 28.5]], 'state': [[0, 28.5, 28.9]], 'our': [[0, 29.0, 29.2]], 'is': [[0, 29.3, 30.7]], 'strong': [[0, 30.7, 31.1]], "what's": [[0, 35.8, 36.4]], 'up': [[0, 36.4, 36.6]], 'take': [[0, 36.8, 37.2]], 'money': [[0, 37.3, 37.5]], 'Minecraft': [[0, 43.3, 44.3]]}
# saythis = ['the', 'president\'s', 'little', 'ugagaga', 'boy', 'thought', 'everybody', 'was', 'fantastic', 'confident', 'see', 'Union', 'uggagag']

#Local Test Code
# memeMissile = "Let's have an intellectual experience at bedtime"
# memeMissile = memeMissile.lower()   ### Transform Intended Message to List
# exclude = string.punctuation
# exclude = exclude.replace("'", "")
# memeMissile = ''.join(ch for ch in memeMissile if ch not in exclude)
# print(memeMissile)
# memeMessageList = memeMissile.split(' ')
# print(memeMessageList)
# makememe("Malan", memeMessageList)
# postVideo("bigmeme.mp4")
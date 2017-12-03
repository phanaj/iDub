import json
import io, os
import pickle
import subprocess
import soundfile as sf
from google.cloud import speech
from google.cloud.speech import types
from google.cloud.speech import enums


def save_dict(dic, dict_dir):
    with open(dict_dir, 'wb+') as f:
        pickle.dump(dic, f, pickle.HIGHEST_PROTOCOL)

def load_dict(dict_dir):
    try:
        with open(dict_dir, 'rb+') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return dict()

def wavToDict(audioFile, dict_dir, file_num):
    if not os.path.exists("Clips"):
        os.makedirs("Clips")

    # import dictionary
    data = load_dict(dict_dir)

    client = speech.SpeechClient()

    start = 0
    clip_num = 0
    wav = sf.SoundFile(audioFile)

    # length of audio file, in seconds
    wav_len = len(wav) / wav.samplerate

    # split into one-minute clips
    while start < wav_len:

        outputDir = "Clips/minute" + str(clip_num) + ".wav"
        command = 'ffmpeg -ss ' + str(start) + ' -i ' + audioFile + ' -t 55 -ab 160k -ac 1 -ar 44100 -vn -nostats -loglevel 0 '+ outputDir
        subprocess.call(command, shell=True)
        start += 55
        clip_num += 1

    for i in range(clip_num):
        fileDir = "Clips/minute" + str(i) + ".wav"

        # with io.open(audioFile, 'rb') as audio:
        audio = io.open(fileDir, 'rb')
        content = audio.read()
        audio = types.RecognitionAudio(content=content)

        config = types.RecognitionConfig(
            encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=44100,
            language_code='en-US',
            enable_word_time_offsets=True)

        # print("Hey just checking in, hope everything's okay")

        # run Google's speech recognition
        operation = client.long_running_recognize(config, audio)
        response = operation.result(timeout=900)

        # print(response)

        # store each word's timestamps in `data`
        for result in response.results:
            print(result)
            for word in result.alternatives[0].words:
                clip_offset = i * 55
                if word.word in data:
                    data[word.word].append([file_num, word.start_time.seconds + word.start_time.nanos*1e-9 + clip_offset,
                                          word.end_time.seconds + word.end_time.nanos*1e-9 + clip_offset])
                else:
                    data[word.word] = [[file_num, word.start_time.seconds + word.start_time.nanos*1e-9 + clip_offset,
                                          word.end_time.seconds + word.end_time.nanos*1e-9 + clip_offset]]
    print(data)
    save_dict(data, dict_dir)
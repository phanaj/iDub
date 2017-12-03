import requests
import os


def postVideo(path):
    """ Input a string in the format of blah.mp4 and it will post it the page in facebook. """
    """ It will look for the video is the directory /Output """
    """ Returns 0 if successful. Otherwise return 1. """
    # Post a video to the facebook page.

    access = "EAAHuZA9kshqsBAI9LiZCTMFpVZBo62DXFtr0dQ0dkZAeR18LsYjLJgox2dLeg9ADJSld9GUenRepWXYgijqmuxopm3hAO0RYPAa3GjNZAIO6k48aKYe8g4t4eokfSABDEWMl91woZA8KmAKXTnMoBcwDZAvaTBcZCSgZD"

    # Send a graph api request to post a video to the page 1814432035521430 with our access token.
    url='https://graph-video.facebook.com/1814432035521430/videos?access_token='+str(access)

    # Change directory to output
    os.chdir("Output")

    # The path is the file we want to post in Output

    files={'file':open(path,'rb')}

    # Send post request
    flag=requests.post(url, files=files).text

    # See if there is an error message or someting
    print (flag)
    if "error" in flag:
        return 1

    return 0


#if __name__ == "__main__":
#    print(postVideo("bigmeme.mp4"))
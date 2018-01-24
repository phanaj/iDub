# iDub
iDub is a service that allows users to generate auto-edited dub videos. A dictionary of words that a person can say is made for each individual based off of training videos.
To query iDub, the user simply sends a message to the Wubba Lubba Dubz facebook page in accordance with the format prescribed by the iDub facebook messenger bot.
In a few minutes, an auto-generated video, per the user's instructions, will be posted on the iDub community page.

## Installation
Run `pip install -r requirements.txt`. 
To use the Google Cloud API, `export GOOGLE_APPLICATION_CREDENTIALS=envir.json`.

## Usage
To add more videos to the training set, edit `url` and `person` in `main.py`, and run `python main.py`.
Open `flask run` to check Facebook submissions.



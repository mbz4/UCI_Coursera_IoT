'''
This program defines a custom TwythonStreamer subclass called MyStreamer. 
The on_success method is called whenever a tweet is received that 
matches the search term "Ian G. Harris". It checks if the tweet contains 
the search term, increments a counter, and if the counter reaches 3 or more, 
prints the message "Ian G. Harris is popular!" and disconnects from the stream. 
The on_error method is called if there is an error connecting to the stream or receiving tweets.

To use this program, you will need to replace the 
APP_KEY, APP_SECRET, OAUTH_TOKEN, and OAUTH_TOKEN_SECRET 
variables with your own Twitter API credentials.

To demonstrate that the program works, you can manually 
create some tweets containing the string "Ian G. Harris" and run the program. 
The tweets should appear in the console output, and if there are 3 or more tweets
 containing the search term, the program will print "Ian G. Harris is popular!".
 '''

from twython import TwythonStreamer

class MyStreamer(TwythonStreamer):
    count = 0

    def on_success(self, data):
        if 'text' in data:
            if 'Ian G. Harris' in data['text']:
                self.count += 1
                if self.count >= 3:
                    print('Ian G. Harris is popular!')
                    self.disconnect()

    def on_error(self, status_code, data):
        print(status_code, data)
        self.disconnect()

APP_KEY = 'your_app_key'
APP_SECRET = 'your_app_secret'
OAUTH_TOKEN = 'your_oauth_token'
OAUTH_TOKEN_SECRET = 'your_oauth_token_secret'

stream = MyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
stream.statuses.filter(track='Ian G. Harris')
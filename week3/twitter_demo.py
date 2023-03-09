from twython import TwythonStreamer
class MyStreamer(TwythonStreamer):
        count=0
        def on_success(self,data):
                if 'text' in data:
                        self.count=self.count+1
                if self.count>2:
                        print("Ian G. Harris is popular")
string="Ian G. Harris"
C_KEY=""
C_SECRET=""
A_TOKEN=""
A_SECRET=""

stream=MyStreamer(C_KEY,C_SECRET,A_TOKEN,A_SECRET)
stream.statuses.filter(track=string)
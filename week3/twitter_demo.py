# from twython import TwythonStreamer
# class MyStreamer(TwythonStreamer):
#         count=0
#         def on_success(self,data):
#                 if 'text' in data:
#                         self.count=self.count+1
#                 if self.count>2:
#                         print("Ian G. Harris is popular")
# string="Ian G. Harris"
# C_KEY=""
# C_SECRET=""
# A_TOKEN=""
# A_SECRET=""

# stream=MyStreamer(C_KEY,C_SECRET,A_TOKEN,A_SECRET)
# stream.statuses.filter(track=string)

from twython import TwythonStreamer
class MyStreamer(TwythonStreamer):
        count=0
        def on_success(self,data):
                if 'text' in data:
                        self.count=self.count+1
                if self.count>2:
                        print("Ian G. Harris is popular")
string="Ian G. Harris"
C_KEY="2aiLH5K4v0wcpDXu3nujLTn9J"
C_SECRET="9mmE7AoMcLZbHn1YYMIB8cOax3fVDvKrwJCfMTpV00XBRkjyUz"
A_TOKEN="1015534523847606273-ube7Xh0azaGsQ9OgiLntTu0fggFKwQ"
A_SECRET="zHg2OBUIifwf2yD06QuoLYV3qReWYXbCihL1B0CyW8A8B"

stream=MyStreamer(C_KEY,C_SECRET,A_TOKEN,A_SECRET)
stream.statuses.filter(track=string)
'''
This code establishes an HTTPS connection to www.uci.edu 
using HTTPConnection. 
It then sends a GET request for the top-level page (/). 
After receiving the response, it extracts the content using the 
read() method of the response, which returns a byte string that needs
 to be decoded into a regular string using the decode() method.
Finally, the code splits the content into lines and prints the first 3 lines using a loop.
'''

import http.client

# establish connection
conn = http.client.HTTPSConnection("www.uci.edu")
conn.request("GET", "/")

# get response and extract content
res = conn.getresponse()
content = res.read().decode('utf-8')

# print first 3 lines
lines = content.split('\n')
for i in range(3):
    print(lines[i])
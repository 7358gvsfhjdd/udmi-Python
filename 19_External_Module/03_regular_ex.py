import re

#https://regexr.com
text = "The quick brown focx jum over the lazy  brown"

#Search for pattern 

match = re.search("brown", text)
print(match)
if match:
    print("Match found!")
    print("Start index:", match.start())
    print("End index:", match.end())
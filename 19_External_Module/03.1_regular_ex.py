import re
text = "The quick brown focx jum over the lazy  brown"

matches = re.findall("the", text, re.IGNORECASE)
print("Matches:",matches)

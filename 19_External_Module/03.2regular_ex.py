import re
text = "The quick brown focx jum over the lazy  brown"

new_text = re.sub("fox", "cat", text)
print("New text:", new_text)
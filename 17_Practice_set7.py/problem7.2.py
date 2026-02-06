words = ["python", "rocks" "ai"]

length = [n for w in words if (n := len(w))>4]

print(length)
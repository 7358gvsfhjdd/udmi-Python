class book:
    def __init__(self, title,author):
        self.title = title
        self.author = author
        
    def __str__(self):
        return f"{self.title} by {self.author}"
        
    def __len__(self):
        return len(self.title)
    
b = book("Java in one hour", "John")
print(b)
print(len(b))

b1 = book("Python in one hour", "Smith")
print(b1)
print(len(b1))

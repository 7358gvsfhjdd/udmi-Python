def print_detail(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        
        
print_detail(name = "Alice", age = 25, city ="Delhi")
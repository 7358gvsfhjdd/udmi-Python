def marks(**kwargs):
    #kwargs  is dictonary withh all the key value pairs which where passed to marks.
    for item in kwargs.keys():
        print(f"The mark of {item} is {kwargs[item]}")
        
marks(shubham = 34, vikrant = 54, jack = 34, priya = 45)
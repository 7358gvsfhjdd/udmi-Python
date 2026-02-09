#f = open("18_file/sam.txt", "r")
#content = f.read()
#print(content)
#f.close()
with open("18_file/sam.txt", "r") as f:
    content = f.read()
    print(content)
    #no need to write f.close(because file is alredy chosenby default)
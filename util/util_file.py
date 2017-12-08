

def write_lines(filename, lines=[]):
    file = open(filename, 'w')
    for l in lines :
        file.write(l+"\n")
    file.close()
    
def read_lines(filename):
    file = open(filename, 'r')
    content = file.readlines()
    file.close()
    content =[i.rstrip("\n") for i in content ]
    return content

def append_lines(filename, lines=[]):
    with open(filename, 'a+') as file:
        for l in lines :
            file.write("\n"+l)
        file.seek(0)
        return file.read()  #no need to close the file
        

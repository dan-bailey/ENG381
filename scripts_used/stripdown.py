## Used to strip out punctuation from a file

filename = input("Enter filename: ")
 
def remove_punc(string):
    punc = '''!()-[]{};:'"\,	<>.•+=“”/?@#$%^&*_~'''
    for ele in string:  
        if ele in punc:  
            string = string.replace(ele, "") 
    return string
 
 
try:
    with open(filename,'r',encoding="utf-8") as f:
        data = f.read()
    with open(filename,"w+",encoding="utf-8") as f:
        f.write(remove_punc(data))
    print("Removed punctuations from the file", filename)
except FileNotFoundError:
    print("File not found")
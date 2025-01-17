

def replaceAll(targrt_str , find_str ,replace_str):
    temp=''
    i=0
    for char in targrt_str :
        if char==find_str :
            temp+=find_str
        else :
            temp+=char
    return temp
        
        
        
print(replaceAll("hbnm","n","t"))
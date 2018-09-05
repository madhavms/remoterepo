file_handle1=open('/home/madhav/PycharmProjects/hello.txt',"r")
file_handle2=open('/home/madhav/PycharmProjects/paste.txt',"w")
sentence=file_handle1.read()
str=""
for ch in sentence:
    if ch == 'A' or ch=='a':
        str=str+" \ "+ch
    else:
        str=str+ch
print str
file_handle2.write(str)
file_handle1.close()
file_handle2.close()
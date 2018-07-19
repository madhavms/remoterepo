file_handle1=open('/home/madhav/PycharmProjects/words.txt',"r")
sent=file_handle1.read()
ls=sent.split(' ')
d={x.rstrip():ls.count(x) for x in ls}
print d
print "THE TOTAL NUMBER OF WORDS IN FILE ARE:"+" "+str(len(ls))



"""THIS IS 1st COMMIT"""""





"""THIS IS 2nd COMMIT"""""

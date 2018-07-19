import random
a=['TRIVANDRUM','TRANSMITTER','TYRANNY','CASTLE']
b=random.choice(a) #choose a random word from list
ls2=[]
ls=[]
for ch in b:
    ls2.append(ch) #store letters of word in list ls2
n=10  #count of number of tries left
x=True #condition for while
print b
l=len(b) #length of word to be found
print "THE WORD CONSISTS OF:"
for i in range(l):
    print '_',  #print the word as blank space for user to know length
print " ",     #use travelling commas to print on same line
for i in range(0,l):
    ls.append('_')


while (x):
    ch=raw_input("ENTER THE LETTER YOU THINK IS IN THE WORD:")
    n=n-1  #count for number of tries left
    i=0  #count to check all the letters of has been compared
    flag=0 #count to check letter found or not
    for ch1 in b:


        if ch1==ch:
            flag=flag+1
            if flag==1:
                print " "
                print "THE LETTER HAS BEEN FOUND:"+" "+str(n)+" "+"CHANCES ARE LEFT"
            ls[i]=ch  #replace '_' with ch ,at position where the letter is found
            i=i+1  #count that keeps position of new entry in ls

        else:
            i=i+1
    if (i==(len(b)) and flag == 0):#if the whole word searched and no alphabet was found
        print " "
        print "THE LETTER NOT FOUND:" + " " + str(n) + " " + "CHANCES ARE LEFT"

    print " "
    print ' '.join(ls) #forms a word from alphabets in list
    print ' '
    if ls2 != ls and n==0: #checks whether intended word found or not after all tries
        x=False
        print "FAILED: 10 CHANCES HAVE BEEN EXHAUSTED"
        

    elif ls2 == ls: #checks whether intended word found or not after all tries
        print "CONGRATS! THE WORD IS FOUND"
        break

""""HELLO THIS IS A PYTHON CODE""""



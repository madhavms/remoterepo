import re

x=True
while (x):
    password =raw_input("ENTER THE PASSWORD:")
    l = len(password)
    if(l <6 or l>12):
        print " "
        print ("PASSWORD LENGTH SHOULD BE BETWEEN 6 and 12")
        print " "

    elif not(re.search("[a-z]",password)):
        print " "
        print ("PASSWORD MUST CONTAIN A SMALL LETTER")
        print " "
    elif not(re.search("[A-Z]",password)):
        print " "
        print ("PASSWORD MUST CONTAIAN A CAPITAL LETTER")
        print " "

    elif not(re.search("[@#$]",password)):
        print " "
        print ("PASSWORD MUST CONTAIN SPECIAL CHARACTERS LIKE @,#,$")
        print " "

    elif not(re.search("[0-9]",password)):
        print " "
        print ("PASSWORD MUST CONTAIN A NUMBER IN 0-9")
        print " "

    else:

        print " "
        print ("PASSWORD VALID")
        x=False
        break
















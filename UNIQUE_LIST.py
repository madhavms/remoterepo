def unique(s):

    ls=s.split(",")
    new_ls=[]
    for l in ls:
        if l not in new_ls:
            new_ls.append(l)

    return new_ls
s=raw_input("Enter the words separated by commas:")
print unique(s)

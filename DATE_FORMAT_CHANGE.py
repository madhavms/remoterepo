a=raw_input("INPUT DATE IN FORMAT DD-MM-YY:")

date=a.split('-')

b=date[1].lstrip('0')
ls=['JANUARY','FEBRUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SPETEMBER','OCTOBER','NOVEMBER','DECEMBER']
ls1=['1','2','3','4','5','6','7','8','9','10','11','12']
dictionary=dict(zip(ls1,ls))

print date[0].lstrip('0')+" "+dictionary[b]+" "+str(20)+date[2]
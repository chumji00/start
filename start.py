data= 'From stephen.marquardi@cst.ac.za.sat jun 5 09:14: 16 2008'
atpos=data.find('@')
print(atpos)
sppos = data.find(' ', atpos)
print(sppos)
host = data[atpos+1 : sppos]
print(host)


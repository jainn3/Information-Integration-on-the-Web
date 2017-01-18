import os
import re
import csv
def validNumber(phone_nuber):
    pattern = re.compile("^[\dA-Z]{3}[-\/][\dA-Z]{3}-[\dA-Z]{4}$", re.IGNORECASE)
    return pattern.match(phone_nuber) is not None

with open('fodors.txt') as f:
    content = f.readlines()

f = open('fodors.csv', 'wb')
writer = csv.writer(f)
writer.writerow(["row_num","r_name","r_address","r_number","r_type"])

rname = ""
raddress = ""
rnumber = ""
rtype = ""

nfound = True
afound = False
numfound =False
typefound = False

count = 0
for line in content:
    if count == 110:
        break
    line = line.strip()
    words = line.split()
    for word in words:
        if word.isdigit():
            nfound = False
            afound = True
        elif validNumber(word):
            rnumber = word
            afound = False
            nfound = False
            typefound = True
            continue
        if typefound:
            rtype +=word + " "
        if afound:
            raddress +=word + " "
        if nfound:
            rname += word + " "
    rtype = rtype.strip()
    rtype = rtype[:-1]
    if rname != "" and raddress != "" and rnumber != "" and rtype != "":
        count = count + 1
        writer.writerow( [count+1,rname.strip(),raddress.strip(),rnumber.strip(),rtype] )
    rname = ""
    raddress = ""
    rnumber = ""
    rtype = ""

    nfound = True
    afound = False
    numfound =False
    typefound = False

print rname
print raddress
print rnumber
rtype = rtype[:-1]
print rtype
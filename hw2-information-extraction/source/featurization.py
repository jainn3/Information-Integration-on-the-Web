import collections
import re
import nltk
import sys
from nltk.tokenize import word_tokenize
def feature_function7(token):

    return nltk.pos_tag(word_tokenize(token))

def feature_function6(token):
    try:
        if int(token)>=2015:
            return 1
        else:
            return 0
    except Exception as e:
        return 0



def feature_function5(token):
    vowels = "AEIOUaeiou"
    count = 0
    for v in vowels:
        count+=token.count(v)
    return count


def feature_function4(token):
    return len(token)


def feature_function3(token):
    pattern = re.compile('[^0-9a-zA-Z]+')
    res = pattern.match(token)
    if res:
        return 1
    else:
        return 0

# token contains numbers return 1 else return 0
def feature_function2(token):
    pattern = re.compile(r"[0-9]+")
    res = pattern.match(token)
    if res:
        return 1
    else:
        return 0

# token contains alphabet return 1 else return 0
def feature_function1(token):
    pattern = re.compile(r"[A-Za-z]+")
    res = pattern.match(token)
    if res:
        return 1
    else:
        return 0


def feature_function8(posdict, token):
    try:
        return posdict[dict][0][1]
    except Exception as e:
        return nltk.pos_tag([token])[0][1]
    pass

#helper function
'''
with open(r"C:\Users\Nimesh\Desktop\test-data.txt", "r") as ins:
    #print ins.readlines()
    for line in ins:
        print line.rsplit(' ', 1)[0].replace(" ", "\t").replace(",	,","")
        #print ''.join(ins.readlines()).replace(" ", "\t")

sys.exit(0)
'''
with open("C:\Users\Nimesh\Desktop\uniits-sentences.txt", "r") as ins:
    linedict = collections.OrderedDict()
    for line in ins:
        line = line.strip()
        tokenfeature = collections.OrderedDict()
        posdict = {}
        for x, y in feature_function7(line):
            posdict[x] = y
        for token in line.strip(' \t\n\r\.').split():
            tuple = ()
            tuple = tuple + (feature_function1(token),
            feature_function2(token),
            feature_function3(token),
            feature_function4(token),
            feature_function5(token),
            feature_function6(token),
            feature_function8(posdict,token)
            )
            tokenfeature[token] = tuple

        linedict[line] = tokenfeature

for sent,tokens in linedict.iteritems():
    for _token, _tuple in tokens.iteritems():
        print "irrelevant",
        for i,a in enumerate(_tuple):
            print a,
        print _token
    print ", , 0"

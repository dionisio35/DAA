
from time import time
from generator import generate_n



def LCS(a:str,b:str):
    better=""
    last=len(b)
    for i in range(len(a)):
        for j in range(last):
            if(a[i]==b[j]):
                temp = a[i] + LCS(a[i+1:], b[j+1:])
                if(len(temp)>len(better)):
                    better=temp
                last=j
    return better


def LCS2(a,b):
    if(len(a)==0 or len(b)==0):
        return ""
    if(a[0]==b[0]):
        return a[0]+LCS2(a[1:],b[1:])
    lcs1=LCS2(a[1:],b)
    lcs2=LCS2(a,b[1:])
    if(len(lcs1)>len(lcs2)):
        return lcs1
    return lcs2






t1=time()
a=LCS(")))((()()))","))()()(()()()()()()()()))")
t2=time()
print(a, t2-t1)
b=LCS2(")))((()()))","))()()(()()()()()()()()))")
t3=time()
print(b,t3-t2)


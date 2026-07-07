import os 
import copy
print("\033c\033[47;31m\give me a url ? \n")
a=input().strip()
curls="curl $1 -o /tmp/curl.bin"
os.system(curls.replace("$1",a))
f1=open("/tmp/curl.bin","r")
f=f1.read()
f1.close()
sss=f.find("<body")
if sss<0:
    sss=f.find("<BODY")
if sss>-1:
    f=f[sss:]
sss=f.find("</body")
if sss<0:
    sss=f.find("</BODY")
if sss>-1:
    f=f[:sss]
f=f.replace("\r\n","")
f=f.replace("\n","")
f=f.replace("\r","")
f=f.replace("  "," ")
f=f.replace("<br>","\r\n")
f=f.replace("<BR>","\r\n")
f=f.replace("<p","\r\n<")
f=f.replace("</p","\r\n<")
f=f.replace("<P","\r\n<")
f=f.replace("</P","\r\n<")
ff=f.split("<")
for d in ff:
    d=d.strip()
    dd=d.split(">")
    if len(dd)>1:
        if dd[1].strip()!="":
            print(dd[1].strip(),end=" ")
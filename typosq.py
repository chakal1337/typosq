import sys
import requests

r = requests.get(url="https://tld-list.com/df/tld-list-basic.txt")
tldlist = r.text.splitlines()

if len(sys.argv) < 2:
 print(f"./{sys.argv[0]} domain")
 sys.exit(0)
dom = sys.argv[1]

def shiftk(domainz, klet):
 domainz_new = ""
 for i in range(len(domainz)):
  if i == klet:
   domainz_new += chr(ord(domainz[i]) >> 1)
  else:
   domainz_new += domainz[i]
 return domainz_new

def addk(domainz, klet, knum):
 domainz_new = ""
 for i in range(len(domainz)):
  if i == klet:
   domainz_new += chr(ord(domainz[i]) + knum)
  else:
   domainz_new += domainz[i]
 return domainz_new

def addqwk(domainz, klet):
 domainz_new = ""
 for i in range(len(domainz)):
  if i == klet:
   domainz_new += chr(ord(domainz[i]) + 6)
  else:
   domainz_new += domainz[i]
 return domainz_new

def muta(domainz, klet):
 domainz_new = ""
 for i in range(len(domainz)):
  if not i == klet:
   domainz_new += domainz[i]
 return domainz_new

def rmsym(ph):
 strnew = ""
 for i in range(len(ph)):
  if ph[i].isalnum() or ph[i] == ".":
   strnew += ph[i]
 return strnew

def fn(dom):
 print(dom.split(".")[0]+"."+tld)

for i in range(len(dom.split(".")[0])):
 print(rmsym(addqwk(dom, i)))
for tld in tldlist:
 dataz = ""
 for i in range(len(dom.split(".")[0])):
  dataz = rmsym(muta(dom, i))
  fn(dataz)
 for i in range(len(dom.split(".")[0])):
  dataz = rmsym(shiftk(dom, i))
  fn(dataz)
 for i in range(len(dom.split(".")[0])):
  for knum in range(1, 13):
   dataz = rmsym(addk(dom, i, knum))
   fn(dataz)

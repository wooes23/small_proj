# python web2txt.py webpage output

import urllib
uname = raw_input("Enter webpage URL: ")
print uname
out_out = raw_input("Enter output file name: ")
uhand = urllib.urlopen(uname, "r")
url = uhand.read()
w = open(out_out, "w")
w.write(url)
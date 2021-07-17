#! /usr/bin/python
print "\nCisco IOU License Generator"
print "Use Wisely with your own responsibility"

import os
import socket
import hashlib
import struct

# get the host id and host name to calculate the hostkey
hostid=os.popen("hostid").read().strip()
hostname = socket.gethostname()
ioukey=int(hostid,16)
for x in hostname:
 ioukey = ioukey + ord(x)

# I Comment this syntax because this just for debuging. wkwkw IDK.
# print "hostid=" + hostid +", hostname="+ hostname + ", ioukey=" + hex(ioukey)[2:]

# create the license using md5sum
iouPad1='\x4B\x58\x21\x81\x56\x7B\x0D\xF3\x21\x43\x9B\x7E\xAC\x1D\xE6\x8A'
iouPad2='\x80' + 39*'\0'
md5input=iouPad1 + iouPad2 + struct.pack('!L', ioukey) + iouPad1
iouLicense=hashlib.md5(md5input).hexdigest()[:16]

# add license info to $HOME/iourc.txt
print "DONE and then manually copy the text from $HOME/iourc.txt to your GNS3/EVE-NG\n"
print "[license]\n" + hostname + " = " + iouLicense + ";"
with open("iourc.txt", "wt") as out_file:
   out_file.write("[license]\n" + hostname + " = " + iouLicense + ";\n")

print "\nCisco IOU License Generator - Kal 2011"
print "Python port of 2006 C version"
print "Edited by kk42id - 2021"
print "\n"
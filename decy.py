#!/usr/bin/env python3
import subprocess

publickey = "hello"
dir = "demoCA" #where everything is kept
Certs_dir = dir + "/" + "certs" # Where the issued certs are kept
crl_dir = dir + "/" + "crl" # Where the issued crl are kept
new_certs_dir = dir + "/" + "newcerts" # default place for new certs.
database = dir + "/" + "index.txt" # database index file.
opensslcnf = "/etc/ssl/openssl.cnf"
home = "/usr/home/ampshock/demo"
print (publickey)
#use K&R style of bracketing: place the opening brace at the end of the construct
#that controls the block. then start the contents of the lock on the next line,
#and indent those contents by one indentation level,
#finally place the closing brace on a separate line
#indent with spaces not tabs
#trailing commas at the end of lists
#separate complex keys or indicies 
#78 line length
#Never place two statements on the same line
#code in Paragraphs 
#-------------------
output_file = open( 'malsaleh.pub', 'w')
#extract public key
subprocess.call([
    "openssl",
    "x509",
    "-in",
    "malsaleh.crt",
    "-pubkey",
    "-noout",
    ],
    shell=False,
    stdout=output_file,)
output_file.close()

#decrypt the message with a private key
subprocess.call([
    "openssl",
    "rsautl",
    "-decrypt",
    "-inkey",
    "apeplins.key",
    "-in",
    "msg-c1",
    "-out",
    "hacking.txt",
])

#sign the MCA with private key
subprocess.call([
    "openssl",
    "dgst",
    "-sha256",
    "-sign",
    "apeplins.key",
    "-out",
    "MCA-c2",
    "hacking.txt",
])

#encrpyt with the public key
subprocess.call([
    "openssl",
    "rsautl",
    "-encrypt",
    "-inkey",
    "malsaleh.pub",
    "-pubin",
    "-in",
    "-hacking.txt",
    "-out",
    "hacking",
])

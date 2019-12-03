#!/usr/bin/env python3
import subprocess


dir = "demoCA" #where everything is kept
Certs_dir = dir + "/" + "certs" # Where the issued certs are kept
crl_dir = dir + "/" + "crl" # Where the issued crl are kept
new_certs_dir = dir + "/" + "newcerts" # default place for new certs.
database = dir + "/" + "index.txt" # database index file.
opensslcnf = "/etc/ssl/openssl.cnf"
home = "/home/remnux/demo"

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
#Create directory structure 
subprocess.call([
    "mkdir",
    "demoCA",
])

subprocess.call([
    "mkdir", 
    Certs_dir,
])

subprocess.call([
    "mkdir",
    crl_dir,
])

subprocess.call([
    "mkdir", 
    new_certs_dir,
])

subprocess.call([
    "touch",
    database,
])

filehandle = open( dir + "/" + "serial", 'w')

filehandle.write( "1000" ) # The current serial number

filehandle.close()

subprocess.call(["cp",
    opensslcnf, 
    home,
])

subprocess.call([
    "openssl",
    "req", 
    "-new", 
    "-x509", 
    "-keyout", 
    "ca.key", 
    "-out", 
    "ca.crt", 
    "-config", 
    "openssl.cnf",
])

#Now that we have created a root CA, we are ready to sign digital certificates for 
#customer. In this lab, you  will be a  customer  for the  root  CA  you  just 
# created  and use  it to  create  and  sign  your personal digital certificate. 
#There are three steps required to create a certificate for the customer:
#Step 1: Generate public/private key pair. 
#The customer needs to first create apublic/private key pair.
#We  can  run the  following  command  to  generate  an  RSA  key pair  (both 
# private  and  public keys). You will be required to provide a password to protect 
#the keys. The keys will be stored in the file your-emich-id.key(use your emich ID 
#for the file, all small caps and no dashes):
subprocess.call([
    "openssl",
    "genrsa", 
    "-aes128", 
    "-out", 
    "apeplins.key", 
    "1024",
])


subprocess.call([
    "openssl", 
    "req",
    "-new", 
    "-key", 
    "apeplins.key", 
    "-out", 
    "mycertreq.csr", 
    "-config", 
    "openssl.cnf",
])


#Step 3: Generate a Certificate.The CSR file must be signed by the CA to
# form a certificate. In the real world, the CSR files are usually sent to a 
#trusted CA for their signature. In this lab, we will use our own CA to generate
# certificates:
subprocess.call([
    "openssl", 
    "ca", 
    "-in", 
    "mycertreq.csr", 
    "-out", 
    "apeplins.crt", 
    "-cert", 
    "ca.crt", 
    "-keyfile", 
    "ca.key", 
    "-config", 
    "openssl.cnf",
])

#If OpenSSL refuses to generate certificates, it is very likely that the names in
# your requests do not match  with  those  of  CA.  The  matching  rules  are  
#specified  in  the  configuration  file  (look  at  the [policymatch]sectionin  
#the openssl.cnffile).  You  can  change  the  names  of  your  requests  to comply
# with the policy, or you can change the policy. The configuration file also includes 
#another policy (called policyanything), which is less restrictive. You can choose 
#that policy by changing the following line:
#"policy = policy_match" change to "policy = policy_anything"

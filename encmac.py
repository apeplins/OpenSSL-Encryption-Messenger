#!/usr/bin/env python
import subprocess
import shlex


dir = "demoCA" #where everything is kept
Certs_dir = dir + "/" + "certs"
crl_dir = dir + "/" + "crl"
new_certs_dir = dir + "/" + "newcerts"
database = dir + "/" + "index.txt"
opensslcnf = "/etc/ssl/openssl.cnf"
home = "/Users/alex/Documents"
proc = subprocess.Popen(["echo", "1000", ">>", "serial"], stdout=subprocess.PIPE)
subprocess.call(["mkdir", "demoCA"])
subprocess.call(["mkdir", Certs_dir])
subprocess.call(["mkdir", crl_dir])
subprocess.call(["mkdir", new_certs_dir])
subprocess.call(["touch", database])
filehandle = open(dir + "/" + "serial", 'w') # write 
filehandle.write("1000")
filehandle.close()
subprocess.call(["cp", opensslcnf, home])
subprocess.call(["openssl", "req", "-new", "-x509", "-keyout", "ca.key", "-out", "ca.crt", "-config", "openssl.cnf"])
subprocess.call(["openssl", "genrsa", "-aes128", "-out", "apeplins.key", "1024"])
subprocess.call(["openssl", "req", "-new", "-key", "apeplins.key", "-out", "mycertreq.csr", "-config", "openssl.cnf"])
subprocess.call(["openssl", "ca", "-in", "mycertreq.csr", "-out", "apeplins.crt", "-cert", "ca.crt", "-keyfile", "ca.key", "-config", "openssl.cnf"])
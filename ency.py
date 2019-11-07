#!/usr/bin/env python3
import subprocess

dir = "demoCA" #where everything is kept
Certs_dir = dir + "/" + "certs"
crl_dir = dir + "/" + "crl"
new_certs_dir = dir + "/" + "newcerts"
database = dir + "/" + "index.txt"
serial = dir + "/" + "serial"
opensslcnf = "/usr/lib/ssl/openssl.cnf"
home = "/home/remnux"
subprocess.call(["mkdir", "demoCA"])
subprocess.call(["mkdir", Certs_dir])
subprocess.call(["mkdir", crl_dir])
subprocess.call(["mkdir", new_certs_dir])
subprocess.call(["touch", database])
#subprocess.call(["echo", "1000"+ >> + serial])
subprocess.call(["cp", opensslcnf, home])

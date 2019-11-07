#!/usr/bin/env python3
import subprocess

dir = "demoCA" #where everything is kept
#Certs_dir = dir/certs
#crl_dir = dir/crl
#new_certs_dir = dir/newcerts
#database = dir/index.txt
#serial = dir /serial
subprocess.call(["mkdir", "demoCA"])
subprocess.call(["mkdir", dir+ "/" +"certs"])
subprocess.call(["mkdir", dir+"/" +"newcerts"])

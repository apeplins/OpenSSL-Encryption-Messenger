## OpenSSL-Encryption-Messenger 
  
## About 
This program attempts to preserves the integrity, confidentiality, and authenticity. 
This program is an attempt at a secure chat by using public key infrastructure (PKI) and certificates by becoming a root Certificate Authority. Then it uses the CA to issue certificates for others. 
The program will automate some of the steps to become a Certificate Authority and will prompt you for a password and you will also be asked to fill in the Country Name, Common Name, etc. 
The output of the program generates two files: ca.key and ca.crt. The file ca.key contains the CA’s private key, while ca.crt contains the public key certificate. 
The program will also use a Message Authentication Code (MAC) to confirm the message has not been changed and if it came from the sender. 
Currently the code generates the MAC digest based on the answered message and encrypts the answered message using the instructor’s public key. 
 

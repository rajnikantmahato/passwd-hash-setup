
#import requests
#from termcolor import colored, cprint
# import simplehacker1 


# init()


# sita = input("Inter Your Password :   ")
# if sita == "rajni":
#     print ("test")
#     # import simplehacker1
    


# elif sita == "password":
#     print("TIme pasasss")
#     def logo():

#     import simplehacker1


# else:
#     print("eroro 333332")

import hashlib

password = input("inter your username\n")
password1 = "0dd37e8afec6c9e180c3d8ca1d9783f9"
password2 = "803205ab3f1b9b6fa6990393f5ac6b58"
password3 = "f6775b164d70b37a191d2ab5e24ce427"

#Finally, validate that the two passwords are the same
if (hashlib.md5(password.encode()).hexdigest() == password1):
   print("Authentication success")
else:
   print("Bad login or password")

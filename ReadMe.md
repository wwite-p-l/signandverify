Open Source code Qbl-Scanfile Description

This software module provides functionality for creating public & private keys and generate self signed certificates.
It can be used to sign and verify the .
It uses Python libraries 
opensource
It is liceneced under the MIT opensource licence terms.

*********************************************
Copyright 2025 <COPYRIGHT wwite p/l>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
*********************************************


Prerequisite Installation in windows Windows:

1. Install python 3.13 
    https://www.python.org/downloads/

2. Install pip
using 
    option 1) py -m ensurepip --upgrade
    option 2)py get-pip.py 




Install the following libraries
cryptography

In windows use the command 
py -m pip install cryptography

How to use

Following are the values which will used to create certificate 

it can be updated in certificateconfig.py

    COUNTRY = "AU"
    STATE = "Victoria"
    CITY = "Melbourne"
    ORGANISATION = "example org"
    DOMAIN = "example.com"
    ALTERNATENAME = "localhost"

Generate public private key and Self signed certificate
---------------------------------------------------------

py ./certificate privatekeyfile publickeyfile certificatefilename

Output:
    Private and public keys generated and saved.
    Self-signed certificate generated and saved.

Sign a message
--------------

py .\sign.py "privatekey.pem" "Hello World"
 
Output:
    b'Hello World'
    Signature
    8d249566ee8419bc52b92e009afd672d1ec9e0e92b17cba2c2f3e66976348813395e691cb237b325f2a7aeeae839fb2b476bbb0b07459d1c59da4ed28b4c76a2d0444e34c355183a9afa275073ff00a625df2f49346faccdf340b11c62aedcb5262afb7e973d0cdfb17d577d6b4372d2e240362bf4c35c7af1f2003253747593138c7e82784d8b2561679e5f0f7d45a62fdbe7679719f0843c7c76b6cb5c3e7309b93ff58d89dcdd2b05102dfbf95a380c9fec84a65bbf5b1336c298a9ca008f938abc3f7cc5d8c32ea4321f70a2c7e785e5b9af69cc2cdca319a774d38daaaef091dc57d7fd40aa95cb113dc985c42689d876a11a26207fb6a4d282bec80aa3

Verify a Message
----------------

py .\verify.py "publickey.pem" "Hello World"  "8d249566ee8419bc52b92e009afd672d1ec9e0e92b17cba2c2f3e66976348813395e691cb237b325f2a7aeeae839fb2b476bbb0b07459d1c59da4ed28b4c76a2d0444e34c355183a9afa275073ff00a625df2f49346faccdf340b11c62aedcb5262afb7e973d0cdfb17d577d6b4372d2e240362bf4c35c7af1f2003253747593138c7e82784d8b2561679e5f0f7d45a62fdbe7679719f0843c7c76b6cb5c3e7309b93ff58d89dcdd2b05102dfbf95a380c9fec84a65bbf5b1336c298a9ca008f938abc3f7cc5d8c32ea4321f70a2c7e785e5b9af69cc2cdca319a774d38daaaef091dc57d7fd40aa95cb113dc985c42689d876a11a26207fb6a4d282bec80aa3"
 
Output:

     Signature is valid. Message is authentic.

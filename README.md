## **gooQR**
##### goo[gle]+QR
# **Offline** __Google Authenticator__ QR Code Creator

A python *3* program that creates QR codes based on your secret keys from Google Authenticator. I made this because one of my Google Authenticator codes was around 65 characters long and thumb-typing that in sounded just awful.

I found a couple solutions that did this exact request already (convert long strong to Google Auth QR code), but they were hosted on web pages. I knew with just a little JavaScript or sleight-of-hand my codes could be transmitted to an attacker without my knowledge. So rather than worrying if a web page does that very thing I created this client-side Python program.

This program is really, really tiny too so it's easy to look at every single line and double check that no funny business is happening. 

---

## **Implementation**

**ONLY** 1 file:
* gooQR.py (~70 lines)
  - We ever want the solution to be big and bulky. We need it to be small enough so that tech saavy users (including those who may not know Python as their first language) can open the source code themselves and verify that no lines look malicious.

---

## **How does it work?**

The format the Google Authenticator application expects QR data to be stored

> otpauth://totp/Example:alice@google.com?secret=JBSWY3DPEHPK3PXP&issuer=Example&digits=9&period=60

We take that string and use it as the seed for our QR code. All QR codes can be converted from strings and back.

Use the **Online Tool** (only to test/understand!) linked below to experiment with how each variable plays a part in the overall string. Here's an example I was using while testing:

![Example - alice@google.com][online-tool-example.png]

---

## **Requirements**

* Python 3
  * https://www.python.org/downloads/ 
* qrcode
  * pip install qrcode
* image
  * pip install image

---

## **Questions**

If you were shared this code and did not download it via GitHub please let me know.

---

## **Online Tool**

I used this tool to create my own application. Thanks, Dan Hersam!
- https://dan.hersam.com/tools/gen-qr-code.html

---

## **TODO**
* Fix this readme up
* Make it clearer why this code exists?
* Open .png file after execution (before program ends)
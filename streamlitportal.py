import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import threading
import time 

# DAzzuD2gaf6jHrjP1pTG

credi = {
  "type": "service_account",
  "project_id": "mini-project-c1e46",
  "private_key_id": "2796e3cddd8c84090691bfca5139d7332edee931",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCm2fNPXFbyZrJ8\neQSAuaIg4KBuriEZ6Gk29Caxdb93OUavDvO69wXOMeYPMS7aYmhOvc6FGjymtRIY\n3UfW75oKmnTgBXGA47hPp+PCVMRH90YPCI6FV8HEFDMOFMFVl2I4h8J4qWaz/k8l\nOW1nBtzhYk4gkJbLCs4sOpkRGcoqdQBUvjrsh08GQ3bnJr3ss9ueKsBhESxQ/gWS\nJKPcLxxP7z+98lsl1EknyJK7eXoMUMftB8Hk7vTsy+VHqErolXWN1RsqReXCGhgE\nIsZ4PSri3AUsP0MUGb7l5B5uIigr37QwIeCdOhJZfuuY5AUWcq0JQjQ6PI89g1ir\nWe1OGbhZAgMBAAECggEAPhqKw0PKAyCxl74NrIIr9BPX80px/KwymWdIDa6XrR9P\nDXLBypoOeaC+EnKKj3OogoKIn6dT4vMrwMCAcGKvkfnKveWYyVI5dMC3eEpH4seJ\ntqfHMJ+o+jxQgpG8Iokd4I+7lWDsXtuuBtt4uqvlxChsjxdyYTHs6q6G8cQJKULY\ncgocIg9MWEHUhvvMa/avQ3XRzR2I+Zga7DjIEA/HSba6qBWAhFKH1Xa3b49ofito\nN/25poLmiM6+jqV8q/OJiOr+nQ6h5xbNbD+keVs/KAv+lKEX73Lf7if6lSV5cVzu\nhLy7O3ens1jw2HJxay+43glAxi8Y2GLFtuUKfDaQrwKBgQDYI+8pTrvhrlzTgymr\npBZqEEFHQOTBSZcsQeBQVZd7HwKOAV9T/BT2crgQlJXpJGZg5hIDfVo8IFi/RVWP\ngI58g1swAyqS5yeX4GdtQFOD0O7t+ngveR54venjDdFUHVjkcP+cZ1H3tbN2LGz4\nzXtP83K9XZRFvDSD32Ler62xZwKBgQDFnxCFlc3Ar4YUZ1PiPJOblWzeNzCcFv2a\nhrNC/j+GGXFXlbCvRcyGDVriepshuwaqY0lpFL8dRDjDYHGKdc9IixD2NVGvpBRQ\nY3xfkqmVPJMZG8C+DugozsTiqKjfMXblz0r8XiI1/RzhBqdl5EzzpgPzJReqfxJE\nDwiK2JJwPwKBgAezaA8BtiH5U2dZ0f9CjmXjBGBkiIH2fENgaXyTQB1r4mxq0hms\n7pZFSheVI6411Mv5BoVHTxK7WE4gS0ccnncDOxl/02F+iOOZZDX5R8B3jju+Y8/V\nMee9ZHrpgB7OGN+ywviwmbQIrkc0mAFZWN5lXx4uGl1NslVMfTpP6hFbAoGAC9wQ\n5MNptp+R/1V4HkKeZR7hirBrNWLX01c0GNgjPcv3FleAY/RfYsgYZTEQcETGEKGm\nvSymj34RngACsFmDmAnoea4Xed/x7CUcSKwHi1I4TbBxr7Y7Tn+iJywR/lr8lKwN\nBvorOWw4OHTqxN2flJuo7wWR1wSLNxRj4dk/aIcCgYEAqVXw55mywwBFPsScPvYQ\nkmucWjhjwlYyBBQWJCp6EBwvDe2h92s/AtLt8q3zts77issnMP5nByiYsLbE0vTG\nBcvOxoVGgwqIuEgkLX9jr8udTm/xJT/JxBYemWIF8YkVdIHXy4t3xtRbAvJ3cfkd\n7UnxHGxcEPajkQtfem599Do=\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-5f7fy@mini-project-c1e46.iam.gserviceaccount.com",
  "client_id": "100984101555160239752",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-5f7fy%40mini-project-c1e46.iam.gserviceaccount.com"
}
global cred
cred = credentials.Certificate(credi)
# app = firebase_admin.initialize_app(cred)
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

db = firestore.client()
global users_ref
users_ref = db.collection(u'Rover').document(u'DAzzuD2gaf6jHrjP1pTG')
d = users_ref.get()
if d.exists:
    print(f"{d.to_dict()}")
   
# print(d)



def dir_forward (fwd):
    users_ref.update({u'forward': fwd})
    print("Done")


def dir_backward (bwd):
    users_ref.update({u'backward': bwd})
    print("Done")


def dir_left (lt):
    users_ref.update({u'left': lt})
    print("Done")    


def dir_right (rt):
    users_ref.update({u'right': rt})
    print("Done")

def stop():
    fwd , bwd , lt , rt = False,False,False,False
    users_ref.update({u'forward': fwd})
    users_ref.update({u'backward': bwd})
    users_ref.update({u'left': lt})
    users_ref.update({u'right': rt})

if d.exists:
    print(f"{d.to_dict()}")


# f = bool(input())
# b = bool(input())
# l =bool(input())
# r = bool(input())

# check(f,b,l,r)


st.title("Mini Project")
st.header("Obstacle Detection and Surveillance Rover")

if st.button('Forward'):
    fwd = True
    dir_forward (fwd)
    print(f"{d.to_dict()}")
else:
    fwd = False
    dir_forward (fwd)

if st.button('Backward'):
    fwd = True
    dir_backward (fwd)
    print(f"{d.to_dict()}")
else:
    fwd = False
    dir_backward (fwd)

if st.button('Right'):
    fwd = True
    dir_right (fwd)
    print(f"{d.to_dict()}")
else:
    fwd = False
    dir_right (fwd)

if st.button('Left'):
    fwd = True
    dir_left (fwd)
    print(f"{d.to_dict()}")
else:
    fwd = False
    dir_left (fwd)

if st.button('Stop'):
    stop()


# if d.exists:
#     print(f"{d.to_dict()}")
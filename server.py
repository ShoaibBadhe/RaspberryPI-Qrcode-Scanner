import cv2
from pyzbar.pyzbar import decode
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
s.bind(('127.0.0.1',5000))
s.listen(15)
conn,addr = s.accept()
print(addr)

def scan():
    cap = cv2.VideoCapture(0)
    i=0
    global a
    while i<1:
        _,frame = cap.read()
	
        decodeobj = decode(frame)
        for obj in decodeobj:
            a=obj.data
            i+=1
        cv2.imshow('Frame',frame)
        cv2.waitKey(5)
        
scan()
conn.send(a)
print(conn.recv(1024))

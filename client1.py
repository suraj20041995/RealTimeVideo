import cv2,numpy,socket

host='127.0.0.1'
port=5858

cap=cv2.VideoCapture(0)
while (True):
    r,fr=cap.read()
    #r,fr1=cap.read()
    #cv2.imshow("remote webcame",fr)
    rval,img=cv2.imencode('.jpg',fr,[1,90])
    data=numpy.array(img)
    stringdata=data.tostring()

    s=socket.socket()
    s.connect((host,port))
    s.sendall(stringdata)
    s.close()

    

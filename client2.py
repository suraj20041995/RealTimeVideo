import cv2,numpy,socket

host='127.0.0.1'
port1=5859

cap1=cv2.VideoCapture(1)
while (True):

    #cv2.imshow("remote webcame",fr1)

    r1,fr1=cap1.read()
    rval1,img1=cv2.imencode('.jpg',fr1,[1,90])
    data1=numpy.array(img1)
    stringdata1=data1.tostring()

    s1=socket.socket()
    s1.connect((host,port1))
    s1.sendall(stringdata1)
    s1.close()

    

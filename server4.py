#import socket,cv2,numpy

host=''
port=5858
port1=5859
bf1=[]
bf2=[]
c1=0
c2=0

import socket,cv2,numpy
#import numpy as np
import cv2
import Tkinter as tk
from PIL import Image, ImageTk

#Set up GUI
window = tk.Tk()  #Makes main window
window.wm_title("Digital Microscope")
window.config(background="#FFFFFF")

#Graphics window
imageFrame = tk.Frame(window, width=300, height=300)
imageFrame.grid(row=0, column=0, padx=10, pady=2)


#display1 = tk.Label(imageFrame,height=200,width=200)
#display1.grid(row=0, column=1, padx=10, pady=2)  #Display 1
#display2 = tk.Label(imageFrame,height=300,width=200)
#display2.grid(row=0, column=0) #Display 2




def moveforward():
	print("Going Forward")

def movebackward():
	print("Going backward")

def moveleft():
	print("Going left")
	
def moveright():
	print("going Right")
	
#Slider window (slider controls stage position)


#toggle_screen.i=0


		  
		  
		  
		  

#display1 = tk.Label(imageFrame,height=200,width=200)
#display1.grid(row=0, column=1, padx=10, pady=2)  #Display 1
#display2 = tk.Label(imageFrame,height=300,width=580)
#display2.grid(row=0, column=0) #Display 2


f = tk.Button(window, text="F", bg="blue", width =5, height = 2, command=moveforward)
f.grid(row = 1 , column = 2 )

b = tk.Button(window, text="B", bg="blue", width =5, height = 2, command=movebackward)
b.grid(row = 4 , column = 2 )


l = tk.Button(window, text="L", bg="green", width =5, height = 2, command=moveleft)
l.grid(row =  2, column = 1 )


r = tk.Button(window, text="R", bg="green", width =5, height = 2, command=moveright)
r.grid(row =  2, column = 3 )



def show():
    print 'server 1'
    s=socket.socket()
    print 'server 2'
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    print 'server 3'
    s.bind((host,port))
    print 'server 4'
    s.listen(1)
    
    print 'server 01'
    s1=socket.socket()
    print 'server 02'
    s1.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    print 'server 03'
    s1.bind((host,port1))
    print 'server 04'
    s1.listen(1)

    print 'server 5'
    conn,addr=s.accept()
    print 'connecting'
    message=[]
    while True:
        data=conn.recv(1024*1024)
        if not data:break
        else:message.append(data)
    print 'data recieved'
    data=''.join(message)
    stringdata=numpy.fromstring(data,numpy.uint8)

    decimg=cv2.imdecode(stringdata,1)
#    cv2.imshow("remote webcame",decimg)

 #   print 'server 05'
    conn1,addr1=s1.accept()
  #  print 'connecting'
    message1=[]
    while True:
        data1=conn1.recv(1024*1024)
        if not data1:break
        else:message1.append(data1)
    print 'data  2 recieved'
    data1=''.join(message1)
    stringdata1=numpy.fromstring(data1,numpy.uint8)

    decimg1=cv2.imdecode(stringdata1,1)
    #  cv2.imshow("remote webcam1",decimg)
    
    cv2image = cv2.cvtColor(decimg, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    #cv2.imshow("remote webcam1",imgtk)
    display1.imgtk = imgtk
    display1.configure(image=imgtk)
   
    cv2image1 = cv2.cvtColor(decimg1, cv2.COLOR_BGR2RGBA)
    img1 = Image.fromarray(cv2image1)
    imgtk1 = ImageTk.PhotoImage(image=img1)
    #cv2.imshow("remote webcam1",imgtk)
    display2.imgtk = imgtk1
    display2.configure(image=imgtk1)
    
    window.after(10,show) 
    #if cv2.waitKey(5) == 27:

	
	
def toggle_screen():
    if toggle_screen.i == 0:
        display2.config(height=20,width=20)
        display1.config(height=300,width=580)
        toggle_screen.i=1;
    else:
        display1.config(height=20,width=20)
        display2.config(height=200,width=200)
        toggle_screen.i=0;
          

def dual_screen():
	display1.config(height=300,width=580)
	display2.config(height=300,width=580)

	
	
	
toggle_screen.i=0
display1 = tk.Label(imageFrame,height=200,width=200)
display1.grid(row=0, column=1, padx=10, pady=2)  #Display 1
display2 = tk.Label(imageFrame,height=20,width=20)
display2.grid(row=0, column=0) #Display 2
	
toggle = tk.Button(window,text="Toggle",bg="yellow",width=5,height=2,command=toggle_screen)
toggle.grid(row=7,column=0)


dual = tk.Button(window,text="Dual",bg="yellow",width=5,height=2,command=dual_screen)
dual.grid(row=8,column=0,padx = 10)
	
	

show() #Display
#toggle_screen.i=0
window.mainloop()  #Starts GUI
	
#cv2.destroyAllWindows()


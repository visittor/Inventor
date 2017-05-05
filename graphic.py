import numpy as np
import cv2
import threading
import pygame
import subprocess
import time
def create_Gradient(size):
	lookup = np.ones(size,dtype = np.uint8)
	for i in range(0,size[0]):
		lookup[i,:size[1],2] = ((239-229)*i)/size[0] + 229
		lookup[i,:size[1],1] = ((155*i)/size[0])
		lookup[i,:size[1],0] = (35*i)/size[0]
	return lookup 

def mouse_callback(event,x,y,flags,params):
	if event == cv2.EVENT_LBUTTONDOWN:
		print (y,x)

class Bar(object):

	def __init__(self,lookup,startPoint,width,maxHeight):
		self.__lookup = lookup
		self.__startPoint = startPoint
		self.__width = width
		self.__maxHeight = maxHeight

	def create_bar(self,percentage,img):
		percentage = 1.5 if percentage>1.5 else percentage
		# print self.__startPoint[0] - int(self.__maxHeight*percentage)
		img[self.__startPoint[0] - int(self.__maxHeight*percentage):self.__startPoint[0],self.__startPoint[1]:self.__startPoint[1]+self.__width,:] = self.__lookup[0:int(self.__maxHeight*percentage),0:self.__width,:] 


class Polygon(object):

	def __init__(self,centerPoint,vertices):
		self.__centerPoint = np.array(centerPoint,dtype = np.float32)
		self.__vertices = np.array(vertices,dtype = np.float32)

	def create_Polygon(self,percentage,img,color = (0,255,0)):
		for i in percentage:
			i[0] = 1.5 if i[0]>1.5 else i[0]
			i[1] = 1.5 if i[1]>1.5 else i[1]
		v = self.__centerPoint + (self.__vertices-self.__centerPoint)*percentage
		v = v.reshape((-1,1,2))

		# cv2.polylines(img,[v.astype(int)],True,color)
		cv2.fillPoly(img,[v.astype(int)],color)

class Energy_Bar(object):
	def __init__(self,lookup,startPoint,width,maxHeight):
		self.__lookup = lookup
		self.__startPoint = startPoint
		self.__width = width
		self.__maxHeight = maxHeight
	def create_energy_bar(self,percentage,img):
		percentage = 1.5 if percentage>1.5 else percentage
		percentage = 0.01 if percentage<=0 else percentage
		img_temp = img[self.__startPoint[0] - int(self.__maxHeight*percentage):self.__startPoint[0],self.__startPoint[1]:self.__startPoint[1]+self.__width,:]
		gradient = self.__lookup[0:int(self.__maxHeight*percentage),0:self.__width,:] 
		# b,_,_ = cv2.split(img_temp)
		_,mask = cv2.threshold(img_temp,127,255,cv2.THRESH_BINARY_INV)
		bit_or = cv2.bitwise_or(img_temp.copy(),gradient,mask = mask[:,:,0])
		img_temp = cv2.bitwise_or(img_temp.copy(),bit_or)
		# img_temp = cv2.bitwise_or(img_temp,bit_or)
		img[self.__startPoint[0] - int(self.__maxHeight*percentage):self.__startPoint[0],self.__startPoint[1]:self.__startPoint[1]+self.__width,:] = img_temp

		
class Sound(threading.Thread):
	def __init__(self,track_name):
		threading.Thread.__init__(self)
		self.track_name = track_name

	def run(self):
		pygame.mixer.init()
		pygame.mixer.music.load(self.track_name)
		pygame.mixer.music.play()

		while pygame.mixer.music.get_busy() == True:
		    continue

def Non_thr_sond(track_name,time_play = 3):
	player = subprocess.Popen(["omxplayer","-o","local",track_name],stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	print "play_Sound"
	time.sleep(time_play+2)
	# player.stdin.write("q")
	# while pygame.mixer.music.get_busy() == True and exitFlag == 0:
	# while pygame.mixer.music.get_busy() == True:
	#     continue

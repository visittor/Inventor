import numpy as np

def create_Gradient(size):
	lookup = np.ones(size,dtype = np.uint8)
	for i in range(0,size[0]):
		lookup[i,:size[1],2] = ((239-229)*i)/size[0] + 229
		lookup[i,:size[1],1] = ((155*i)/size[0])
		lookup[i,:size[1],0] = (35*i)/size[0]
	return lookup 

class Bar(object):

	def __init__(self,lookup,startPoint,width,maxHeight):
		self.__lookup = lookup
		self.__startPoint = startPoint
		self.__width = width
		self.__maxHeight = maxHeight

	def create_bar(self,percentage,img):
		img[self.__startPoint[0] - self.__maxHeight*percentage:self.__startPoint[0],self.__startPoint[1]:self.__startPoint[1]+self.__width,:] = self.__lookup[0:self.__maxHeight*percentage,0:self.__width,:] 
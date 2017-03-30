import cv2
import numpy as np

def create_LookUpTable(size):
	lookup = np.ones(size,dtype = np.uint8)
	for i in range(0,size[0]):
		lookup[i,:size[1],2] = ((239-229)*i)/size[0] + 229
		lookup[i,:size[1],1] = ((155*i)/size[0])
		lookup[i,:size[1],0] = (35*i)/size[0]
	return lookup 

def apply_LookUp(source,lookup,dst):
	if lookup is None:
		return

	dst[:] = lookup[source]

class Bar(object):

	def __init__(self,lookup,startPoint,width,maxHeight):
		self.__lookup = lookup
		self.__startPoint = startPoint
		self.__width = width
		self.__maxHeight = maxHeight

	def create_bar(self,percentage,img):
		img[self.__startPoint[0] - self.__maxHeight*percentage:self.__startPoint[0],self.__startPoint[1]:self.__startPoint[1]+self.__width,:] = self.__lookup[0:self.__maxHeight*percentage,0:self.__width,:] 

class Bar1(Bar):

	def __init__(self,lookup):
		Bar.__init__(self,lookup,(314,5),30,300)
		pass

class Bar2(Bar):

	def __init__(self,lookup):
		Bar.__init__(self,lookup,(314,105),30,300)
		pass

class Bar3(Bar):

	def __init__(self,lookup):
		Bar.__init__(self,lookup,(314,205),30,300)
		pass

class Food(object):
	def __init__(self,name,protein,carb,fat,energy,vitA=0,vitD=0,vitE=0,vitK=0,vitC=0,vitB=0):
		self._name = name
		self._protein = protein
		self._carb = carb
		self._fat = fat
		self._energy = energy
		self._vitA = vitA
		self._vitD = vitD
		self._vitE = vitE
		self._vitK = vitK
		self._vitC = vitC
		self._vitB = vitB
	@property
	def name(self):
		a = self._name
		return a
	@property
	def protein(self):
		a = self._protein
		return a
	@protein.setter
	def protein(self,x):
		pass
	@property
	def carb(self):
		a = self._carb
		return a
	@property
	def fat(self):
		a = self._fat
		return a
	@property
	def energy(self):
		a = self._energy
		return a
	@property
	def vitA(self):
		a = self._vitA
		return a
	@property
	def vitD(self):
		a = self._vitD
		return a
	@property
	def vitE(self):
		a = self._vitE
		return a
	@property
	def vitK(self):
		a = self._vitK
		return a
	@property
	def vitC(self):
		a = self._vitC
		return a
	@property
	def vitB(self):
		a = self._vitB
		return a

class FoodQ(Food):
	def __init__(self):
		Food.__init__(self,"q",10,0,0,1000)
class FoodW(Food):
	def __init__(self):
		Food.__init__(self,"w",0,10,0,1000)
class FoodE(Food):
	def __init__(self):
		Food.__init__(self,"e",0,0,10,1000)

class Body(object):
	def __init__(self,name,Adeprotien,Adecarb,Adefat,Adeenergy,AdevitA=0,AdevitD=0,AdevitE=0,AdevitK=0,AdevitC=0,AdevitB=0):
		self._name = name
		self._protein = 0
		self._carb = 0
		self._fat = 0
		self._energy = 0
		self._vitA = 0
		self._vitD = 0
		self._vitE = 0
		self._vitK = 0
		self._vitC = 0
		self._vitB = 0
		self._Adeprotein = Adeprotien
		self._Adecarb = Adecarb
		self._Adefat = Adefat
		self._Adeenergy = Adeenergy
		self._AdevitA = AdevitA
		self._AdevitD = AdevitD
		self._AdevitE = AdevitE
		self._AdevitK = AdevitK
		self._AdevitC = AdevitC
		self._AdevitB = AdevitB
	@property
	def name(self):
		a = self._name
		return a
	@property
	def protein(self):	return self._protein
	@protein.setter
	def protein(self,x):
		print "setter"
		if x<self._Adeprotein:
			self._protein = x 
		else:
			self._protein = self._Adeprotein

	@property
	def carb(self):	return self._carb
	@carb.setter
	def carb(self,x):self._carb = x if x<=self._Adecarb else self._Adecarb

	@property
	def fat(self):	return self._fat
	@fat.setter
	def fat(self,x):self._fat = x if x<=self._Adefat else self._Adefat

	@property
	def energy(self):	return self._energy
	@energy.setter
	def energy(self,x):self._energy = x if x<=self._Adeenergy else self._Adeenergy

	@property
	def vitA(self):	return self._vitA
	@vitA.setter
	def vitA(self,x):self._vitA = x if x<=self._vitA else self._vitA

	@property
	def vitD(self):	return self._vitD
	@vitD.setter
	def vitD(self,x):self._vitD = x if x<=self._vitD else self._vitD

	@property
	def vitE(self):	return self._vitE
	@vitE.setter
	def vitE(self,x):self._vitE = x if x<=self._vitE else self._vitE

	@property
	def vitK(self):	return self._vitK
	@vitK.setter
	def vitK(self,x):self._vitK = x if x<=self._vitK else self._vitK

	@property
	def vitC(self):	return self._vitC
	@vitC.setter
	def vitC(self,x):self._vitC = x if x<=self._vitC else self._vitC

	@property
	def vitB(self):	return self._vitB
	@vitB.setter
	def vitB(self,x):self._vitB = x if x<=self._vitB else self._vitB

	@property
	def Adeprotein(self):
		a = self._Adeprotein
		return a
	@property
	def Adecarb(self):
		a = self._Adecarb
		return a
	@property
	def Adefat(self):
		a = self._Adefat
		return a
	@property
	def Adeenergy(self):
		a = self._Adeenergy
		return a
	@property
	def AdevitA(self):
		a = self._AdevitA
		return a
	@property
	def AdevitD(self):
		a = self._AdevitD
		return a
	@property
	def AdevitE(self):
		a = self._AdevitE
		return a
	@property
	def AdevitK(self):
		a = self._AdevitK
		return a
	@property
	def AdevitC(self):
		a = self._AdevitC
		return a
	@property
	def AdevitB(self):
		a = self._AdevitB
		return a


""" main here """
#############################################################################################################################################################################################
img = cv2.imread("Template_draft1.png")
dst =np.zeros((480,640,3),dtype = np.uint8)
lookup = create_LookUpTable(img.shape)

bar1 = Bar1(lookup)
bar2 = Bar2(lookup)
bar3 = Bar3(lookup)

# bar1.create_bar(0.2,img)
# bar2.create_bar(0.1,img)
# bar3.create_bar(0.75,img)

foodq = FoodQ()
foodw = FoodW()
foode = FoodE()

body = Body("New",100,100,100,1000)

while True:
	out = img
	print body.protein

	bar1.create_bar(float(body.protein)/float(body.Adeprotein),out)
	# bar1.create_bar(1,out)
	bar2.create_bar(float(body.carb)/float(body.Adecarb),out)
	bar3.create_bar(float(body.fat)/float(body.Adefat),out)


	cv2.imshow('img',out)
	k = cv2.waitKey(1)
	if k == ord("q"):
		# print type(foodq.protein),foodq.protein,body.Adeprotein
		body.protein +=  foodq.protein
		body.carb += foodq.carb
		body.fat += foodq.fat
	elif k == ord("w"):
		body.protein += foodw.protein 
		body.carb += foodw.carb
		body.fat += foodw.fat
		body.energy += foodw.energy
	elif k == ord("e"):
		body.protein += foode.protein
		body.carb += foode.carb
		body.fat += foode.fat
		body.energy += foode.energy
	elif k == ord("b"):
		break

cv2.destroyAllWindows()
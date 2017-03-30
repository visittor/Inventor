try:
	from ConfigParser import ConfigParser
except ImportError:
	from configParser import ConfigParser #ver. > 3

class Food(object):
	# def __init__(self,name,protein,carb,fat,energy,vitA=0,vitD=0,vitE=0,vitK=0,vitC=0,vitB=0):
	def __init__(self,**kwargs):
		self._name = kwargs['name']
		self._code = kwargs['code']
		self._protein = float(kwargs['protein'])
		self._carb = float(kwargs['carb'])
		self._fat = float(kwargs['fat'])
		self._energy = float(kwargs['energy'])
		self._vitA = float(kwargs['vita'])
		self._vitD = float(kwargs['vitd'])
		self._vitE = float(kwargs['vite'])
		self._vitK = float(kwargs['vitk'])
		self._vitC = float(kwargs['vitc'])
		self._vitB = float(kwargs['vitb'])
	@property
	def name(self):
		a = self._name
		return a
	@property
	def code(self):
		a = self._code
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




class Body(object):
	# def __init__(self,name,Adeprotien,Adecarb,Adefat,Adeenergy,AdevitA=0,AdevitD=0,AdevitE=0,AdevitK=0,AdevitC=0,AdevitB=0):
	def __init__(self,**kwargs):
		self._name = kwargs['name']
		self._code = kwargs['code']
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
		self._Adeprotein = float(kwargs['adeprotein'])
		self._Adecarb = float(kwargs['adecarb'])
		self._Adefat = float(kwargs['adefat'])
		self._Adeenergy = float(kwargs['adeenergy'])
		self._AdevitA = float(kwargs['adevita'])
		self._AdevitD = float(kwargs['adevitd'])
		self._AdevitE = float(kwargs['adevite'])
		self._AdevitK = float(kwargs['adevitk'])
		self._AdevitC = float(kwargs['adevitc'])
		self._AdevitB = float(kwargs['adevitb'])
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
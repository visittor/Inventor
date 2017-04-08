try:
	from ConfigParser import ConfigParser
except ImportError:
	from configParser import ConfigParser #ver. > 3

def make_meal(*args):
	p = 0
	c = 0 
	f = 0 
	en = 0
	A = 0
	D = 0
	E = 0
	K = 0
	C = 0
	B = 0
	for i in args:
		if i.__class__ == Food:
			p += i.protein
			c += i.carb
			f += i.fat
			en += i.energy
			A += i.vitA
			D += i.vitD
			E += i.vitE
			K += i.vitK
			C += i.vitC
			B += i.vitB
		else:
			pass
	dic = {"protein":p,"carb":c,"fat":f,"energy":en,"vita":A,"vitd":D,"vite":E,"vitk":K,"vitc":C,"vitb":B}
	return Food(dic)

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

		self._protein = [0]
		self._carb = [0]
		self._fat = [0]
		self._energy = [0]
		self._vitA = [0]
		self._vitD = [0]
		self._vitE = [0]
		self._vitK = [0]
		self._vitC = [0]
		self._vitB = [0]

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

		self._illness = None

		self._report = {"protein":0.8,"carb":0.8,"fat":0.8,"energy":0.8,"vitA":0.8,"vitD":0.8,"vitE":0.8,"vitK":0.8,"vitC":0.8,"vitB":0.8}

	def eat(self,food):
		if food.__class__ != Food:
			pass
		else:
			self._protein.append(food.protein)
			self._carb.append(food.carb)
			self._fat.append(food.fat)
			self._vitA.append(food.vitA)
			self._vitD.append(food.vitD)
			self._vitE.append(food.vitE)
			self._vitK.append(food.vitK)
			self._vitC.append(food.vitC)
			self._vitB.append(food.vitB)
		self.__digest()
			

	def __digest(self):
		if len(self._protein) > 5:
			self._protein.pop(0)
		if len(self._carb) > 5:
			self._carb.pop(0)
		if len(self._fat) >5:
			self._fat.pop(0)
		if len(self._energy) > 5:
			self._energy.pop(0)
		if len(self._vitA) > 5:
			self._vitA.pop(0)
		if len(self._vitD) > 5:
			self._vitD.pop(0)
		if len(self._vitE) > 5:
			self._vitE.pop(0)
		if len(self._vitK) > 5:
			self._vitK.pop(0)
		if len(self._vitC) > 2:
			self._vitC.pop(0)#vitC and vitB should always have len == 2 before pop. Always append b4 pop.
		if len(self._vitB) > 2:#Note: vitC and vitB dissolve by water.Body cant store it.
			self._vitB.pop(0)
		
	@property
	def name(self): return self._name

	@property
	def protein(self):	return sum(self._protein)/len(self._protein)

	@property
	def carb(self):	return sum(self._carb)/len(self._carb)

	@property
	def fat(self):	return sum(self._fat)/len(self._fat)
	
	@property
	def energy(self):	return sum(self._energy)/len(self._energy)
	
	@property
	def vitA(self):	return sum(self._vitA)/len(self._vitA)
	
	@property
	def vitD(self):	return sum(self._vitD)/len(self._vitD)
	
	@property
	def vitE(self):	return sum(self._vitE)/len(self._vitE)
	
	@property
	def vitK(self):	return sum(self._vitK)/len(self._vitK)
	
	@property
	def vitC(self):	return sum(self._vitC)/len(self._vitC)
	
	@property
	def vitB(self):	return sum(self._vitB)/len(self._vitB)
	
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

	@property
	def report(self):
		self._report = {}
		self._report["vitA"] = sum(self._vitA)/(len(self._vitA)*self._AdevitA)
		self._report["vitD"] = sum(self._vitD)/(len(self._vitD)*self._AdevitD) 
		self._report["vitE"] = sum(self._vitE)/(len(self._vitE)*self._AdevitE)
		self._report["vitK"] = sum(self._vitK)/(len(self._vitK)*self._AdevitK)
		self._report["vitC"] = sum(self._vitC)/(len(self._vitC)*self._AdevitC)
		self._report["vitB"] = sum(self._vitB)/(len(self._vitB)*self._AdevitB)

		min = 1
		minKey = None
		for key,value in self._report.items():
			if value < min:
				min = value
				minKey = key
		self._report['lack_vit'] = minKey
		self._report["protein"] = sum(self._protein)/(len(self._protein)*self._Adeprotein)
		self._report["carb"] = sum(self._carb)/(len(self._carb)*self._Adecarb)
		self._report["fat"] = sum(self._fat)/(len(self._fat)*self._Adefat)
		self._report["energy"] = sum(self._energy)/(len(self._energy)*self._Adeenergy)
		return self._report

	@property
	def is_illness(self):
		if self._illness is None:
			return False
		else:
			return True

	def get_illness(self,inhibitor):
		if self._illness is not None:
			return self._illness(inhibitor)
		return None

	def set_illness(self,x):
		if callable(x):
			self._illness = x
		elif x is None:
			self._illness = None
		else:
			pass

class Diseas(object):

	# def __init__(self,attackPoint,symtom = None):
	def __init__(self,**kwargs):
		self._symtom = eval(kwargs['symtom'])
		self._attackPoint = kwargs['attackpoint']
	
	def attack(self,body):
		if body.report['lack_vit'].lower() == self._attackPoint:
			if body.is_illness == False :
				body.set_illness(self._symtom)

def symtomA(inhibitor):
	if inhibitor['vitA'] < 0:
		print "I'm lack of vitamin A"
	return "vitA"

def symtomD(inhibitor):
	if inhibitor['vitD'] < 0:
		print "I'm lack of vitamin D"
	return "vitD"

def symtomE(inhibitor):
	if inhibitor['vitE'] < 0:
		print "I'm lack of vitamin E"
	return "vitE"

def symtomK(inhibitor):
	if inhibitor['vitK'] < 0:
		print "I'm lack of vitamin K"
	return "vitK"

def symtomC(inhibitor):
	if inhibitor['vitC'] < 0:
		print "I'm lack of vitamin C"
	return "vitC"

def symtomB(inhibitor):
	if inhibitor['vitB'] < 0:
		print "I'm lack of vitamin B"
	return "vitB"



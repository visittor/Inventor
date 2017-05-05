from symtom import *
from body_shape import *
def make_meal(foodList):
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
	for i in foodList:
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
	dic = {"protein":p,"carb":c,"fat":f,"energy":en,"vita":A,"vitd":D,"vite":E,"vitk":K,"vitc":C,"vitb":B,"name":'all',"code":"code"}
	return Food(**dic)

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

		self._protein = []
		self._carb = []
		self._fat = []
		self._energy = []
		self._vitA = []
		self._vitD = []
		self._vitE = []
		self._vitK = []
		self._vitC = []
		self._vitB = []

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
		self._bodyShape = eval(kwargs['body_shape_function'])

		self._report = {"protein":0,"carb":0,"fat":0,"energy":0,"vitA":0,"vitD":0,"vitE":0,"vitK":0,"vitC":0,"vitB":0}

	def eat(self,food):
		if food.__class__ != Food:
			pass
		else:
			self._protein.append(food.protein)
			self._carb.append(food.carb)
			self._fat.append(food.fat)
			self._energy.append(food.energy)
			self._vitA.append(food.vitA)
			self._vitD.append(self._AdevitD*1.3)
			self._vitE.append(food.vitE)
			self._vitK.append(food.vitK)
			self._vitC.append(food.vitC)
			self._vitB.append(food.vitB)
		self.__digest()
		self.__update_report()
			

	def __digest(self):
		if len(self._protein) > 10:
			self._protein.pop(0)
		if len(self._carb) > 10:
			self._carb.pop(0)
		if len(self._fat) >10:
			self._fat.pop(0)
		if len(self._energy) > 10:
			self._energy.pop(0)
		if len(self._vitA) > 10:
			self._vitA.pop(0)
		if len(self._vitD) > 10:
			self._vitD.pop(0)
		if len(self._vitE) > 10:
			self._vitE.pop(0)
		if len(self._vitK) > 10:
			self._vitK.pop(0)
		if len(self._vitC) > 4:
			self._vitC.pop(0)#vitC and vitB should always have len == 2 before pop. Always append b4 pop.
		if len(self._vitB) > 4:#Note: vitC and vitB dissolve by water.Body cant store it.
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

	def __update_report(self):
		self._report = {}
		self._report["vitA"] = sum(self._vitA)/(len(self._vitA)*self._AdevitA) if len(self._vitA) != 0 else 0
		self._report["vitD"] = sum(self._vitD)/(len(self._vitD)*self._AdevitD) if len(self._vitD) != 0 else 0
		self._report["vitE"] = sum(self._vitE)/(len(self._vitE)*self._AdevitE) if len(self._vitE) != 0 else 0
		self._report["vitK"] = sum(self._vitK)/(len(self._vitK)*self._AdevitK) if len(self._vitK) != 0 else 0
		self._report["vitC"] = sum(self._vitC)/(len(self._vitC)*self._AdevitC) if len(self._vitC) != 0 else 0
		self._report["vitB"] = sum(self._vitB)/(len(self._vitB)*self._AdevitB) if len(self._vitB) != 0 else 0

		min = 1
		minKey = None
		for key,value in self._report.items():
			if value < min:
				min = value
				minKey = key
		self._report['lack_vit'] = minKey
		self._report["protein"] = sum(self._protein)/float(len(self._protein)*self._Adeprotein) if len(self._protein) != 0 else 0
		self._report["carb"] = sum(self._carb)/(len(self._carb)*self._Adecarb) if len(self._carb) != 0 else 0
		self._report["fat"] = sum(self._fat)/(len(self._fat)*self._Adefat) if len(self._fat) != 0 else 0
		self._report["energy"] = sum(self._energy)/(len(self._energy)*self._Adeenergy) if len(self._energy) != 0 else 0
	
	@property
	def report(self):
		return self._report

	@property
	def is_illness(self):
		if self._illness is None:
			return False
		else:
			return True

	def get_illness(self):
		if self._illness is not None:
			return self._illness
		return None

	def set_illness(self,x):
		if x.__class__ == Diseas:
			self._illness = x
		elif x is None:
			self._illness = None
		else:
			pass

	def show_illness(self):
		if self._illness is not None:
			self._illness.symtom(self._report)

	def get_bodyShape(self):
		if self._bodyShape is not None:
			return self._bodyShape(self._report)
		return None

	def set_bodyshape_function(self,x):
		if callable(x):
			self._bodyShape = x
		elif x is None:
			self._bodyShape = None
		else:
			pass

class Diseas(object):

	# def __init__(self,attackPoint,symtom = None):
	def __init__(self,**kwargs):
		self.name = kwargs['name']
		self._symtom = eval(kwargs['symtom'])
		self._attackPoint = kwargs['attackpoint']
	
	def attack(self,body):
		if body.report['lack_vit'].lower() == self._attackPoint.lower():
			if body.is_illness == False :
				body.set_illness(self)

	@property
	def attackPoint(self):
		return self._attackPoint

	def symtom(self,inhibitor):
		self._symtom(inhibitor)


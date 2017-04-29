try:
	from ConfigParser import ConfigParser
except ImportError:
	from configParser import ConfigParser #ver. > 3
from model import *
from symtom import *
from Doctor import *
	
class Stock(object):
	def __init__(self,cfg_file = None,section = None,option = "one",Klass = None):
		self._cfg = ConfigParser()
		self._cfg.read(cfg_file)
		self._section = section
		self._Klass = Klass
		self._stock = {}
		#self.item if option == 'one'
		if option == "one":
			self.__create_stock_optionOne()
		elif option == "many":
			self.__create_stock_optionMany()

	def __create_stock_optionMany(self):
		n = 1
		while 1==1:
			if self._cfg.has_section(self._section + str(n)):
				list_ = self._cfg.items(self._section+str(n))
				dict_ = dict(list_)
				print dict_
				self._stock[dict_['code']] = self._Klass(**dict_)
			else:
				break
			n += 1
		print self._stock

	def __create_stock_optionOne(self):
		if self._cfg.has_section(self._section):
			list_ = self._cfg.items(self._section)
			dict_ = dict(list_)
			try:
				# self._stock[dict_['code']] = self._Klass(dict_)
				setattr(self,'item',self._Klass(**dict_))
			except KeyError:
				raise "Wrong config file style"
		else:
			pass

	def findFromCode(self,code):
		if type(code) == str:
			if code in self._stock:
				return [self._stock[code]]
		try:
			out = []
			for i in code:
				if i in self._stock:
					out.append(self._stock[i])
				else:
					pass
			return out
		except TypeError:
			if code in self._stock:
				return self._stock[code]
			else:
				pass

class FoodStock(Stock):
	def __init__(self):
		Stock.__init__(self,cfg_file = "Food.ini",section = "Food",option = "many",Klass = Food)

class BodyStock(Stock):
	def __init__(self):
		Stock.__init__(self,cfg_file = "Body.ini",section = "Body",option = "many",Klass = Body)

class DiseasStock(Stock):
	def __init__(self):
		Stock.__init__(self,cfg_file = "Diseas.ini",section = "Diseas",option = "many",Klass = Diseas)

class DoctorStock(Stock):
	def __init__(self):
		Stock.__init__(self,cfg_file = 'Diseas.ini',section = "Doctor",option = "one",Klass = Doctor)
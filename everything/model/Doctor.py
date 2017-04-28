class Doctor(object):
	
	def __init__(self,reportFunc = lambda x:x,**kwargs):

		self._illnessList = eval(kwargs['illnesslist'])
		self._rangeProtein = eval(kwargs['rangeprotein'])
		self._rangeCarb = eval(kwargs['rangecarb'])
		self._rangeFat = eval(kwargs['rangefat'])
		self._rangeEnergy = eval(kwargs['rangeenergy'])
		self._rangeVitA = eval(kwargs['rangevita'])
		self._rangeVitD = eval(kwargs['rangevitd'])
		self._rangeVitE = eval(kwargs['rangevite'])
		self._rangeVitK = eval(kwargs['rangevitk'])
		self._rangeVitC = eval(kwargs['rangevitc'])
		self._rangeVitB = eval(kwargs['rangevitb'])
		self._reportFunc = reportFunc

	def diagnose(self,body):
		diag_report = {}
		report = body.report
		if self._rangeProtein[0] < report['protein'] < self._rangeProtein[1]:
			diag_report["protein"] = 0
		else:
			diag_report['protein'] = 1 if report['protein'] > self._rangeProtein[1] else -1

		if self._rangeCarb[0] < report['carb'] < self._rangeCarb[1]:
			diag_report['carb'] = 0
		else:
			diag_report['carb'] = 1 if report['carb'] > self._rangeCarb[1] else -1

		if self._rangeFat[0] < report['fat'] < self._rangeFat[1]:
			diag_report['fat'] = 0
		else:
			diag_report['fat'] = 1 if report['fat'] > self._rangeFat[1] else -1

		if self._rangeEnergy[0] < report['energy'] < self._rangeEnergy[1]:
			diag_report['energy'] = 0
		else:
			diag_report['energy'] = 1 if report['energy'] > self._rangeEnergy[1] else -1

		if self._rangeVitA[0] < report['vitA'] < self._rangeVitA[1]:
			diag_report['vitA'] = 0
		else:
			diag_report['vitA'] = 1 if report['vitA'] > self._rangeVitA[1] else -1

		if self._rangeVitD[0] < report['vitD'] < self._rangeVitD[1]:
			diag_report['vitD'] = 0
		else:
			diag_report['vitD'] = 1 if report['vitD'] > self._rangeVitD[1] else -1

		if self._rangeVitE[0] < report['vitE'] < self._rangeVitE[1]:
			diag_report['vitE'] = 0
		else:
			diag_report['vitE'] = 1 if report['vitE'] > self._rangeVitE[1] else -1

		if self._rangeVitK[0] < report['vitK'] < self._rangeVitK[1]:
			diag_report['vitK'] = 0
		else:
			diag_report['vitK'] = 1 if report['vitK'] > self._rangeVitK[1] else -1

		if self._rangeVitC[0] < report['vitC'] < self._rangeVitC[1]:
			diag_report['vitC'] = 0
		else:
			diag_report['vitC'] = 1 if report['vitC'] > self._rangeVitC[1] else -1

		if self._rangeVitB[0] < report['vitB'] < self._rangeVitB[1]:
			diag_report['vitB'] = 0
		else:
			diag_report['vitB'] = 1 if report['vitB'] > self._rangeVitB[1] else -1
		
		diag_report['illness'] = body.get_illness().name

		self._cure(diag_report,body)
		final_report = self._reportFunc(diag_report)
		return final_report

	def _cure(self,diag_report,body):
		print diag_report['illness'],self._illnessList
		if self._illnessList.has_key(diag_report['illness']):

			if diag_report[self._illnessList[diag_report['illness']]] > -1:

				body.set_illness(None)
				diag_report['illness'] = 'Null'
		else:
			pass
		










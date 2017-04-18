from model import *
from Doctor import *
def create_test_config():
	body_config = {'name':'test','code':'code',
					'adeprotein':1,
					'adecarb':1,
					'adefat':1,
					'adeenergy':1,
					'adevita':1,
					'adevitd':1,
					'adevite':1,
					'adevitk':1,
					'adevitc':1,
					'adevitb':1,
					}

	food_config = {'name':'food_test','code':'code',
					'protein':10,
					'carb':10,
					'fat':10,
					'energy':10,
					'vita':10,
					'vitd':10,
					'vite':10,
					'vitk':10,
					'vitc':10,
					'vitb':10,
					}

	empty_food_config = {'name':'empty_food','code':'empty_code',
					'protein':0,
					'carb':0,
					'fat':0,
					'energy':0,
					'vita':0,
					'vitd':0,
					'vite':0,
					'vitk':0,
					'vitc':0,
					'vitb':0,
					}
	doctor_config = {'rangeprotein':'(0.8,1.2)',
					 'rangecarb':'(0.8,1.2)',
					 'rangefat':'(0.8,1.2)',
					 'rangeenergy':'(0.8,1.2)',
					 'rangevita':'(0.8,1.2)',
					 'rangevitd':'(0.8,1.2)',
					 'rangevite':'(0.8,1.2)',
					 'rangevitk':'(0.8,1.2)',
					 'rangevitc':'(0.8,1.2)',
					 'rangevitb':'(0.8,1.2)',
					 'illnesslist':"{'vitA':'vitA','vitD':'vitD','vitE':'vitE','vitK':'vitK','vitC':'vitC','vitB':'vitB'}",
					}
	return body_config,food_config,empty_food_config,doctor_config

def test_body():
	error = 0
	print 'begin body test'
	body_config,food_config,empty_food_config,_ = create_test_config()
	body = Body(**body_config)
	food = Food(**food_config)
	empty_food = Food(**empty_food_config)

	report = body.report
	for key,value in report.items():
		if key != 'lack_vit':
			if value != 0:
				error += 1
				print 'error at nutrient:\t',key,'\t\texpected 0 got ',value,'\tinstead'

	body.eat(food)
	report = body.report
	for key,value in report.items():
		if key != 'lack_vit':
			if value != 10:
				error += 1
				print 'error at nutrient:\t',key,'\t\texpected 10 got ',value,'\tinstead'

	for i in range(2,5):
		body.eat(empty_food)
		report = body.report
		for key,value in report.items():
			if key != 'lack_vit':
				if value != 10.0/float(i):
					error += 1
					print 'error at nutrient:\t',key,'\t\texpected ',10.0/float(i),'\tgot ',value,'\tinstead'
	for i in range(5,11):
		body.eat(empty_food)
		report = body.report
		for key,value in report.items():
			if key != 'lack_vit' and key != 'vitC' and key != 'vitB':
				if value != 10.0/float(i):
					error += 1
					print 'error at nutrient:\t',key,'\t\texpected ',10.0/float(i),'\tgot ',value,'\tinstead'

	body.eat(empty_food)
	report = body.report
	for key,value in report.items():
		if key != 'lack_vit':
			if value != 0:
				error += 1
				print 'error at nutrient:\t',key,'\t\texpected 0 got ',value,'\tinstead'

	check_minVit_config = food_config.copy()
	for key,value in empty_food_config.items():
		if key != 'lack_vit':
			pass
		else:
			check_minVit_config[key] = value
			body = Body(**body_config)
			body.eat(Food(**check_minVit_config))
			report = body.report
			if report['lack_vit'] != key.lower():
				error += 1
				print 'error lack_vit should be\t',key,'\t\tbut got\t',report['lack_vit'],'\tinstead'
			check_minVit_config = food_config.copy()

	print 'total body error is ', error,'\n'

def test_diseas():
	error = 0
	print "begin diseas test"
	body_config,food_config,empty_food_config,_ = create_test_config()
	food = Food(**food_config)
	for key,value in empty_food_config.items():
		check_minVit_config =food_config.copy()
		if key[:3] == 'vit':
			check_minVit_config[key] = value
			body = Body(**body_config)
			diseas = Diseas(symtom = 'symtom'+key[-1].upper(),attackpoint = key)

			body.eat(Food(**check_minVit_config))
			body.eat(Food(**check_minVit_config))
			# print body.report

			print 'attack body with symtom'+key[-1]
			diseas.attack(body)
			attack_at = body.get_illness()
			print 'if there are NO!! symtom show above this line, an error occure.'
			print 'attact at ',attack_at,'(',key,')'

			body.eat(food)
			body.eat(food)
			body.get_illness()
			print 'if there ARE!! symtom show above this line, an error occure.\n'
	print 'finish diseas test'

def test_doctor():
	error = 0
	print "begin doctor test\n"

	body_config,food_config,empty_food_config,doctor_config = create_test_config()
	food = Food(**food_config)
	for key,value in empty_food_config.items():
		check_minVit_config = food_config.copy()
		if key[:3] == 'vit':
			check_minVit_config[key] = value
			body = Body(**body_config)
			diseas = Diseas(symtom = 'symtom'+key[-1].upper(),attackpoint = key)
			doctor = Doctor(lambda x:x['illness'],**doctor_config)

			body.eat(Food(**check_minVit_config))
			print 'want to inflect at',key
			diseas.attack(body)
			print 'Now i am inflected'
			if doctor.diagnose(body).lower() != key.lower():
				error += 1
				print "[ inflect wrong target"

			body.eat(food)
			
			print "i get cure "
			if doctor.diagnose(body) != "Null":
				error += 1
				print "not get cure"
			print "\n"
	print "finish doctor test with error: ????",error

if __name__ == '__main__':
	test_body()
	test_diseas()
	test_doctor()
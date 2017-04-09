from model import *

def test_body():
	error = 0
	print 'begin body test'
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
	body = Body(**body_config)

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
	food = Food(**food_config)

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

	check_minVit_config = food_config
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
			check_minVit_config = food_config

	print 'total error is ', error


if __name__ == '__main__':
	test_body()
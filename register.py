try:
	from ConfigParser import ConfigParser,SafeConfigParser
except ImportError:
	from configParser import ConfigParser,SafeConfigParser #ver. > 3
from G6reader import *
import RPi.GPIO as GPIO
# parser =SafeConfigParser()
# RR = Read_RFID()

# while True:
# 	k = raw_input("r to add section, e to exit: ")
# 	if k =='r':
# 		k = raw_input("[Section number] = ")
# 		sec_name = 'Food'+str(k)
# 		try:
# 			parser.add_section(sec_name)
# 			uid = RR.get_uid()
# 			parser.set(sec_name,'code',str(uid))
# 			k = raw_input("Food name = ")
# 			parser.set(sec_name,'name',k)
# 			k = raw_input("Food protein = ")
# 			parser.set(sec_name,'protein',k)
# 			k = raw_input("Food carb = ")
# 			parser.set(sec_name,'carb',k)
# 			k = raw_input("Food fat = ")
# 			parser.set(sec_name,'fat',k)
# 			k = raw_input("Food energy = ")
# 			parser.set(sec_name,'energy',k)
# 			k = raw_input("Food vitA = ")
# 			parser.set(sec_name,'vitA',k)
# 			k = raw_input("Food vitD = ")
# 			parser.set(sec_name,'vitD',k)
# 			k = raw_input("Food vitE = ")
# 			parser.set(sec_name,'vitE',k)
# 			k = raw_input("Food vitK = ")
# 			parser.set(sec_name,'vitK',k)
# 			k = raw_input("Food vitC = ")
# 			parser.set(sec_name,'vitC',k)
# 			k = raw_input("Food vitB = ")
# 			parser.set(sec_name,'vitB',k)
# 		except DuplicateSectionError:
# 			uid = RR.get_uid()
# 			parser.set(sec_name,'code',str(uid))
# 			k = raw_input("Food name = ")
# 			parser.set(sec_name,'name',k)
# 			k = raw_input("Food protein = ")
# 			parser.set(sec_name,'protein',k)
# 			k = raw_input("Food carb = ")
# 			parser.set(sec_name,'carb',k)
# 			k = raw_input("Food fat = ")
# 			parser.set(sec_name,'fat',k)
# 			k = raw_input("Food energy = ")
# 			parser.set(sec_name,'energy',k)
# 			k = raw_input("Food vitA = ")
# 			parser.set(sec_name,'vitA',k)
# 			k = raw_input("Food vitD = ")
# 			parser.set(sec_name,'vitD',k)
# 			k = raw_input("Food vitE = ")
# 			parser.set(sec_name,'vitE',k)
# 			k = raw_input("Food vitK = ")
# 			parser.set(sec_name,'vitK',k)
# 			k = raw_input("Food vitC = ")
# 			parser.set(sec_name,'vitC',k)
# 			k = raw_input("Food vitB = ")
# 			parser.set(sec_name,'vitB',k)
# 	elif k == 'e':
# 		break

# with open("config.ini","a") as f:
# 	parser.write(f)
# GPIO.cleanup()
# print "[OK]"

with open("raw_data2.txt",'r') as f:
	data = []
	for line in f:
		data.append(line.strip("\n"))

parser =SafeConfigParser()
RR = Read_RFID()
count = 1
for i in data:
	option = i.split("\t")
	if len(option) == 11:
		sec_name = 'Food'+str(count)
		print sec_name," enter to confirm"
		raw_input()
		try:
			parser.add_section(sec_name)
			print "wait for rfid"
			uid = RR.get_uid()
			parser.set(sec_name,'code',str(uid))
			parser.set(sec_name,'name',option[0])
			parser.set(sec_name,'protein',option[1])
			parser.set(sec_name,'carb',option[2])
			parser.set(sec_name,'fat',option[3])
			parser.set(sec_name,'energy',option[10])
			parser.set(sec_name,'vitA',option[4])
			parser.set(sec_name,'vitD',option[5])
			parser.set(sec_name,'vitE',option[6])
			parser.set(sec_name,'vitK',option[7])
			parser.set(sec_name,'vitC',option[8])
			parser.set(sec_name,'vitB',option[9])
			print "name",option[0],"--->",str(uid)
		except DuplicateSectionError:
			print "Already have ",sec_name," waiting for rfid\n"
			uid = RR.get_uid()
			parser.set(sec_name,'code',str(uid))
			parser.set(sec_name,'name',option[0])
			parser.set(sec_name,'protein',option[1])
			parser.set(sec_name,'carb',option[2])
			parser.set(sec_name,'fat',option[3])
			parser.set(sec_name,'energy',option[10])
			parser.set(sec_name,'vitA',option[4])
			parser.set(sec_name,'vitD',option[5])
			parser.set(sec_name,'vitE',option[6])
			parser.set(sec_name,'vitK',option[7])
			parser.set(sec_name,'vitC',option[8])
			parser.set(sec_name,'vitB',option[9])
			print "name",option[0],"--->",str(uid)
	count += 1

with open("config.ini","w") as f:
	parser.write(f)
GPIO.cleanup()
print "[OK]"

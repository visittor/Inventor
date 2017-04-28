#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522
import signal
import time

class Read_RFID:
	def __init__(self):
		self.MIFAREReader = MFRC522.MFRC522()

	def get_uid(self,to=0):
		print 'Waiting for RFIDtag'
		# return uid in RFID
		rfid_uid = []
		# rfid_uid = [128,15,177,88]
		hex_uid = ''
		t = time.clock()
		if to != 0:
			print 'Set timeout to',to,'sec' 

		while True:
			(status,TagType) = self.MIFAREReader.MFRC522_Request(self.MIFAREReader.PICC_REQIDL)
			# If a card is found
			if status == self.MIFAREReader.MI_OK:
				print "RFIDtag detected"
            # Get the UID of the card
			(status,uid) = self.MIFAREReader.MFRC522_Anticoll()
            # If we have the UID, continue
			if status == self.MIFAREReader.MI_OK:
				rfid_uid = uid
				break
			if time.clock()-t >= to and to != 0:
				print 'Reached timeout',to,'sec'
				break
			#else:
				#print "I don't get UID"

        ###################
        # changes uid to hex number but on string
		for i in range(len(rfid_uid)):
			rfid_uid[i] = format(rfid_uid[i],'02x')

		for i in range(len(rfid_uid)):
			hex_uid = hex_uid + rfid_uid[i]
		return rfid_uid

		#return hex_uid
	def read_once(self):
		rfid_uid = []
		hex_uid = ''
		(status,TagType) = self.MIFAREReader.MFRC522_Request(self.MIFAREReader.PICC_REQIDL)
		# If a card is found
		if status == self.MIFAREReader.MI_OK:
			print "RFIDtag detected"
        # Get the UID of the card
		(status,uid) = self.MIFAREReader.MFRC522_Anticoll()
        # If we have the UID, continue
		if status == self.MIFAREReader.MI_OK:
			rfid_uid = uid
		# for i in range(len(rfid_uid)):
		# 	rfid_uid[i] = format(rfid_uid[i],'02x')
		return rfid_uid

	def end_read(self):
		GPIO.cleanup()

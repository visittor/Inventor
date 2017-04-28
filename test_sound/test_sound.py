import pygame
import threading

exitFlag = 0
class Sound(threading.Thread):

	def __init__(self,threadID,name):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
	def run(self):
		play_Sound()

def play_Sound():
	global exitFlag
	while exitFlag == 0:
		pygame.mixer.init()
		pygame.mixer.music.load("pause.mp3")
		pygame.mixer.music.play()

		while pygame.mixer.music.get_busy() == True and exitFlag == 0:
		    continue
	print "Exit Sound\n"

class DoSomething(threading.Thread):

	def __init__(self,threadID,name):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name

	def run(self):
		do_something()
		print "Exit do something\n"

def do_something():
	global exitFlag
	while True:
		a = raw_input("k to stop")
		if a == 'k':
			exitFlag = 1
			break


thread1 = Sound(1,"sound")
thread2 = DoSomething(2,"DoSomething")

thread1.start()
thread2.start()



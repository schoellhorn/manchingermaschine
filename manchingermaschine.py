#2.0
from tkinter import Y
from turtle import position
from cv2 import exp
from numpy import positive
import pyautogui as pt
from time import sleep
import pyperclip
import random
import win32gui, win32con
import time
import os

debuggerPrefix = "[ManchingerMaschine] "
correctHash = "NULL"
reboot = 1

def init():
	os.system("clear")
	print(debuggerPrefix + "Init")
	print(debuggerPrefix + "Made by JonschDEV -> Version: 1.0")
	print(debuggerPrefix + "Correct Hash " + correctHash + ", please check that this hash is correct!")
	print(debuggerPrefix + "You use this program at your own risk!!! I am not responsible for any damages!!!")
	time.sleep(2)
	print(debuggerPrefix + "Please dont do anything now, the program will do everything!")
	time.sleep(4)
	start()

def start():
	frfx = startFirefox()
	time.sleep(2)
	if(pyperclip.paste() == "187"):
		cleanup(frfx, 1)
	firstPhase(frfx)
	secondPhase(frfx)
	thirdPhase(frfx)
	votes = 1
	while(pyperclip.paste() != "187"):
		firstPhase(frfx)
		secondPhase(frfx)
		thirdPhase(frfx)
		votes+=1
		print(debuggerPrefix + "Votes: " + str(votes))
	cleanup(frfx, 1)

def otherWebsiteOpened(title, websiteID):
	validTitles = [ "Jetzt hier voten für: Realschule am Keltenwall Staatliche Realschule Manching | ANTENNE BAYERN - Mozilla Firefox", "Jetzt abstimmen für Realschule am Keltenwall Staatliche Realschule Manching | ANTENNE BAYERN - Mozilla Firefox", "Abstimmung Pausenhof-Konzerte | ANTENNE BAYERN - Mozilla Firefox" ]
	if(title == validTitles[websiteID]):
		return False
	return True

def startFirefox():
	os.system("\"C:\\Program Files\\Mozilla Firefox\\firefox.exe\" https://www.antenne.de/programm/aktionen/pausenhof-konzerte/schulen/oberbayern/realschule-am-keltenwall-staatliche-realschule-manching/")
	print(debuggerPrefix + "Waiting for firefox...")
	while(win32gui.FindWindow(None, "mozilla firefox") == 0):
		1 == 1
	firefox = win32gui.FindWindow(None, "mozilla firefox")
	if(firefox == 0):
		print("Error! Code: 187") #Window initializations error
		cleanup(firefox, 0)
	print(debuggerPrefix + "Firefox window registered!")
	time.sleep(4)
	win32gui.ShowWindow(firefox, win32con.SW_MAXIMIZE)
	win32gui.SetForegroundWindow(firefox)
	pt.press("f11")
	return firefox

def firstPhase(firefoxHandle):
	pt.hotkey("ctrl", "f")
	pt.typewrite("abstimmen")
	time.sleep(1)
	firstPhaseSecondPart(firefoxHandle)

def firstPhaseSecondPart(firefoxHandle):
	if win32gui.GetForegroundWindow() != firefoxHandle or otherWebsiteOpened(win32gui.GetWindowText(win32gui.GetForegroundWindow()), 0) == True:
		cleanup(firefoxHandle, 0)
	else:
		try:
			pos = pt.locateOnScreen("vote.png", confidence=.6)
			global x, y
			try:
				if pos is not None:
					x = pos[0] + 40
					y = pos[1] + 30
					pt.moveTo(int(x), int(y))
					pt.click()
					time.sleep(4)
					return
				else:
					return firstPhase(firefoxHandle)
			except(Exception):
				print(debuggerPrefix + "Error! Code: 387") #Image not found error
				cleanup(firefoxHandle, 0) #I dont know what this is yet
		except(Exception):
			print(debuggerPrefix + "Error! Code: 487") #Image not found error
			cleanup(firefoxHandle, 1)

def secondPhase(firefoxHandle): #This gets called
	pt.hotkey("ctrl", "f")
	pt.typewrite("stimme abgeben")
	time.sleep(1)
	secondPhaseSecondPart(firefoxHandle)

def secondPhaseSecondPart(firefoxHandle):
	if win32gui.GetForegroundWindow() != firefoxHandle or otherWebsiteOpened(win32gui.GetWindowText(win32gui.GetForegroundWindow()), 1) == True:
		cleanup(firefoxHandle, 0)
	else:
		try:
			pos = pt.locateOnScreen("second.png", confidence=.6)
			global x, y
			try:
				if pos is not None:
					x = pos[0] + 40
					y = pos[1] + 30
					pt.moveTo(int(x), int(y))
					pt.click()
					time.sleep(4)
					return
				else:
					return secondPhase(firefoxHandle)
			except(Exception):
				print(debuggerPrefix + "Error! Code: 587") #Idk what this is yet
				cleanup(firefoxHandle, 0)
		except(Exception):
			print(debuggerPrefix + "Error! Code: 687") #Image error
			cleanup(firefoxHandle, 1)

def thirdPhase(firefoxHandle): #This gets called
	pt.hotkey("ctrl", "f")
	pt.typewrite("teilen")
	time.sleep(1)
	thirdPhaseSecondPart(firefoxHandle)

def thirdPhaseSecondPart(firefoxHandle):
	if win32gui.GetForegroundWindow() != firefoxHandle or otherWebsiteOpened(win32gui.GetWindowText(win32gui.GetForegroundWindow()), 2) == True:
		cleanup(firefoxHandle, 0)
	else:
		try:
			pos = pt.locateOnScreen("third.png", confidence=.6)
			global x, y
			try:
				if pos is not None:
					x = pos[0] + 40
					y = pos[1] + 30
					pt.moveTo(int(x), int(y))
					pt.click()
					time.sleep(4)
					return
				else:
					return thirdPhase(firefoxHandle)
			except(Exception):
				print(debuggerPrefix + "Error! Code: 787") #Idk what this is yet
				cleanup(firefoxHandle, 0)
		except(Exception):
			print(debuggerPrefix + "Error! Code: 887") #Image error
			cleanup(firefoxHandle, 1)

def cleanup(frfxWindow, force):
	print(debuggerPrefix + "Shutdown request! Closing Firefox...")
	win32gui.PostMessage(frfxWindow,win32con.WM_CLOSE,0,0)
	print(debuggerPrefix + "Firefox closed, have a nice day and thanks for contributing!")
	if reboot == 1 and force == 0:
		init()
	exit()

init()

import sys
import serial
import time


def readState(txt):
	file = open(txt,'r')
	return file.read(1)

def writeState(txt,state):
        file = open(txt,'w')
	file.write(state)
#print  readState('state.txt')

writeState('state.txt','1')

ser = serial.Serial('/dev/ttyUSB0',9600)
while(readState('state.txt') == '1'):
	ser.write('1\r\n')
ser.close()
sys.exit()


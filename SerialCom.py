import serial

'''
Establishes a connection with tty0 and tty1. Both these
represent two way communication with the USB ports.
'''

# Creates two serial objects to communicate with the USB ports.


try:
    ser1 = serial.Serial("/dev/ttyACM1", 9600)  # check if ACM1 connects
except:
    print("Something went wrong ACM1")  # catch exception no connection available
    exit()

try:
    ser2 = serial.Serial("/dev/ttyACM3", 9600)  # check if ACM3 connects
except:
    print("Something went wrong ACM3")  # catch exception no connection available
    exit()


ser1.write("p")
if(ser1.readline()==1):
    mic1 = ser1
    mic2 = ser2
else:
    mic2 = ser1
    mic1 = ser2

def send1(val):
    mic1.write(val)

def send2(val):
    mic2.write(val)

def read1():
    mic1.readline()

def read2():
    mic2.readline()



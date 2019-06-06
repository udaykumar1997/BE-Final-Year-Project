# setup start

import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
from picamera import PiCamera
from time import sleep
import time, os, fnmatch, shutil, serial, csv
port = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=1)
camera = PiCamera()
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
TRIG = 38
ECHO = 40
i=0
GPIO.setwarnings(False)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

# setup over

def ic(): #image capture
    timestamp = time.strftime('%Y-%m-%d-%H%M%S', time.localtime());
    FILE_NAME = ("/home/pi/data/" + timestamp+'.png')
    camera.start_preview()
    camera.capture(FILE_NAME)
    sleep(1)
    camera.stop_preview()
    
def vc(): #video capture
    timestamp = time.strftime('%Y-%m-%d-%H%M%S', time.localtime());
    FILE_NAME = ("/home/pi/data/" + timestamp+'.h264')
    camera.start_preview()
    camera.start_recording(FILE_NAME)
    sleep(20)
    camera.stop_recording()
    camera.stop_preview()

def ld(): # location detection
    while 1:
        data = port.readline()
        if "$GPGGA" in data:
            #print(data)
            mylist=data.split(",")
            print(mylist[2]+' N', mylist[4]+' E')
            break

def dd(): #distance detection
    GPIO.output(TRIG, False)
    time.sleep(2)
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    while GPIO.input(ECHO)==0:
        pulse_start = time.time()
    while GPIO.input(ECHO)==1:
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance+1.15, 2)
    print(distance)

def aione(): #image capture, distance, location, all in one
    timestamp = time.strftime('%Y-%m-%d-%H%M%S', time.localtime());
    FILE_NAME = ("/home/pi/data/" + timestamp+'.png')
    camera.start_preview()
    camera.capture(FILE_NAME)
    sleep(1)
    datarow=[timestamp,FILE_NAME,'lat','long','dis','leafHealth','productCount']
    camera.stop_preview()
    while 1:
        data = port.readline()
        if "$GPGGA" in data:
            mylist=data.split(",")
            datarow[2]=mylist[2]+' N'
            datarow[3]=mylist[4]+' E'
            sleep(1)
            break
    GPIO.output(TRIG, False)
    time.sleep(2)
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    while GPIO.input(ECHO)==0:
        pulse_start = time.time()
    while GPIO.input(ECHO)==1:
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance+1.15, 2)
    datarow[4]=distance
    print(datarow);print('\n')
    with open('/home/pi/data/metadata.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(datarow)
    csvFile.close()
    

if __name__ == '__main__':
# all in one
    aione()

# 1 image
#    ic()

# gps
#    ld()

# untrasonic
#    dd()

# 6 images
#    ic();ic();ic();ic();ic();ic();

# 18 images
#    ic();ic();ic();ic();ic();ic();ic();ic();ic();ic();ic();ic();ic();ic();ic();ic();ic();ic();

# 1 video, 20 secs total
#    vc()

# 3 videos, 60 secs total
#    vc();vc();vc();


# a;echo 1;a;echo 2;a;echo 3;a;echo 4;a;echo 5;a;echo 6;a;echo 7;a;echo 8;a;echo 9;a;echo 10;

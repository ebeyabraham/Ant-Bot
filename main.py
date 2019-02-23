from utils import Bot
import serial
import time

#parameters for PID
position = 0
setpoint = 50.0
error = 0
sum_error = 0
last_error = 0
kp = 0.25
kd = 4.0
ki = 0.0
motor_speed = 0
base_speed = 80

ser = serial.Serial("/dev/ttyUSB0", 9600)
#time.sleep(0.5)
serial_output = 1

prev_reading = ''
node_count = 0

bot = Bot()
#bot.forward(50,50)
'''
while node_count < 2:
    serial_output = str(ser.readline())
    serial_output = serial_output[2:-5]
    #print(serial_output)
    try:
        position = int(serial_output)
        error = setpoint - position
        #sum_error += error
        motor_speed = kp * error + kd*(error - last_error) 
        last_error = error
        left_motor_speed = base_speed - motor_speed
        right_motor_speed = base_speed + motor_speed
        print(left_motor_speed,right_motor_speed)
        bot.forward(left_motor_speed, right_motor_speed)
    except Exception as e:
        if serial_output == 'N' and prev_reading != 'N':
            print("[NODE]")
            node_count += 1
        #else:
            #print(e)
    prev_reading = serial_output
'''

serial_output = str(ser.readline())
serial_output = int(serial_output[2:-5])

while serial_output>=-1 and serial_output <=50:
    bot.right(40,40)
    serial_output = str(ser.readline())
    try:
         serial_output = int(serial_output[2:-5])
    except Exception as e:
         print(e)

while serial_output>50:
    bot.right(40,40)
    serial_output = str(ser.readline())
    try:
        serial_output = int(serial_output[2:-5])
    except Exception as e:
        print(e)

bot.stop()

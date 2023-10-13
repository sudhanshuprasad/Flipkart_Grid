import serial
import time

arduino = serial.Serial(port='COM11', baudrate=2000000, timeout=0.1)

def goto_box(x, y):
    # x=y=0
    # arm_id = 3
    # box_id = 4
    box = [0,0]
    # arm = [0,0]
    offset = [0,0]
    box =[x,y]
    target = [box[0]-offset[0], box[1]-offset[1]]

    value = (write_read(str(target[0])+" "+str(target[1])))
    print("Response: " + value)
    if target[0]<70 and target[1]<70 :
        return True
    else:
        return False
    # return True


def grab_box():
    return True


def place_box():
    return True

# ----------------------------------------------------------------#

def write_read(x):
    arduino.write(bytes(str(x), 'utf-8'))
    # arduino.write('x')
    time.sleep(0.05)
    data = arduino.readline().decode('utf-8')
    return data


# while True:
#     num = input("Enter a number: ")  # Taking input from user
#     value = write_read("o")
#     print(value)  # printing the value
# write_read("on")
# time.sleep(1)
# for i in range(10):
value = write_read("on")
time.sleep(0.5)
value = write_read("off")
time.sleep(0.5)
value = write_read("on")
time.sleep(0.5)
value = write_read("off")
time.sleep(0.5)
value = write_read("on")
time.sleep(0.5)
value = write_read("off")
time.sleep(0.5)
print(value)
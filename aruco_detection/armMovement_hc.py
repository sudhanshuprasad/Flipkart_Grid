import serial
import time
time.sleep(20)

arduino = serial.Serial(port='COM11', baudrate=2000000, timeout=0.1)

def write_read(x):
    arduino.write(bytes(str(x), 'utf-8'))
    # arduino.write('x')
    time.sleep(0.05)
    data = arduino.readline().decode('utf-8')
    return data

# home || move up
for i in range(20):
    print(write_read('114 160 140 100 83 0'))
    time.sleep(0.04)

# time.sleep(1)

# move to the side
# for i in range(20):
#     print(write_read('114 160 140 100 83 60'))
#     time.sleep(0.04)

# time.sleep(1)
def movement():
    # # move down
    for i in range(20):
        print(write_read('30 140 150 100 93 0'))
        time.sleep(0.01)

    # # time.sleep(1)


    # # grab
    for i in range(10):
        print(write_read('20 110 128 100 93 0'))
        time.sleep(0.01)

    for i in range(10):
        print(write_read('20 110 128 100 93 0'))
        time.sleep(0.001)
    for i in range(10):
        print(write_read('20 110 128 100 30 0'))
        time.sleep(0.001)
    time.sleep(0.5)

    # # move up
    for i in range(10):
        print(write_read('134 160 140 100 30 0'))
        time.sleep(0.01)

    time.sleep(1)

    # rotate
    for i in range(10):
        print(write_read('134 160 140 100 30 90'))
        time.sleep(0.01)

    # # move down
    for i in range(10):
        print(write_read('64 165 130 100 30 90'))
        time.sleep(0.01)

    time.sleep(1)

    # # move down
    for i in range(10):
        print(write_read('64 165 130 100 95 90'))
        time.sleep(0.01)

    # # time.sleep(1)
    # home
    for i in range(20):
        print(write_read('114 160 140 100 83 0'))
        time.sleep(0.04)


if __name__ == '__main__':
    movement()
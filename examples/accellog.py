# log the accelerometer values to a .csv-file on the SD-card

import pyb

accel = pyb.Accel()  # create object of accelerometer
blue = pyb.LED(4)  # create object of blue LED

with open("/sd/log.csv", "w") as log:
    blue.on()  # turn on blue LED

    # do 100 times (if the board is connected via USB, you can't write longer because the PC tries to open the filesystem which messes up your file.)
    for _ in range(100):
        t = pyb.millis()  # get time since reset
        x, y, z = accel.filtered_xyz()  # get acceleration data
        log.write(f"{t},{x},{y},{z}\n")

blue.off()  # turn off LED

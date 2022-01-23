import sys
sys.path.append("./SDL_Pi_GroveI2CMotorDrive")

import sdl_Pi_GroveI2CMotorDrive
import time

# "0b1010" defines output polarity
# "10" means the M+ is "positive" while the M- is "negative"

MOTOR_FORWARD = 0b1010
MOTOR_BACKWARD = 0b0101

try:
    m = SDL_Pi_GroveI2CMotorDrive.motor_drive()
    # Forward
    print("Forward")
    # defines the sped of motor 1 and motor 2
    m.MotorSpeedSetAB(100, 100)
    time.sleep(2)
    
    # stop
    print("Stop")
    m.MotorSpeedSetAB(0,0)
    time.sleep(1)
    
    # Increase speed
    for i in range (100):
        print("Speed: ", i)
        m.MotorSpeedSetAB(i, i)
        time.sleep(0.02)
    print("Stop")
    m.MotorSpeedSetAB(0,0)
    
except IOError:
    print("Unable to find the I2C motor drive")

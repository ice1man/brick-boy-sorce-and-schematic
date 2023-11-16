import random
import machine
import time
import rpi
import snake
import code
#import max7219
from LiquidCrystal import LiquidCrystal
# Define display pins
SPI_CLOCK = 18
SPI_MOSI = 19
SPI_CS = 5
DISPLAY_DC = 23
DISPLAY_RESET = 17

# Initialize display
#display_dot = machine.ILI9341(SPI_CLOCK, SPI_MOSI, SPI_CS, DISPLAY_DC, DISPLAY_RESET)
#display_dot.init()


RS = machine.Pin(4)
EN = machine.Pin(5)
RW = machine.Pin(3)
D4 = machine.Pin(6)
D5 = machine.Pin(7)
D6 = machine.Pin(8)
D7 = machine.Pin(9)

display_text = LiquidCrystal(4, 5, 3, 6, 7, 8, 9)
time.sleep(0.01)
display_text.begin(16, 2)  # Set the number of columns and rows

# Define GPIO pin numbers for buttons
BUTTON_A_PIN = 15
BUTTON_B_PIN = 14
BUTTON_C_PIN = 13
BUTTON_D_PIN = 12

# Initialize display


# Initialize buttons
button_a = machine.Pin(BUTTON_A_PIN, machine.Pin.IN, machine.Pin.PULL_DOWN)
button_b = machine.Pin(BUTTON_B_PIN, machine.Pin.IN, machine.Pin.PULL_DOWN)
button_c = machine.Pin(BUTTON_C_PIN, machine.Pin.IN, machine.Pin.PULL_DOWN)
button_d = machine.Pin(BUTTON_D_PIN, machine.Pin.IN, machine.Pin.PULL_DOWN)

display_text.print("press a for rock b=snake c=code")
display_text.setCursor(1, 0)
#display_text.print("b=snake c=code")

while True:
    if button_a.value() == 1:
        display_text.clear()
        rpi.rps()
    if button_b.value() == 1:
        display_text.clear()
        snake()
    if button_c.value() == 1:
        display_text.clear()
        code()



ten main je mix 2 kodu:

from machine import Pin, PWM
from time import sleep
# Servo na pinu GP2
servo = PWM(Pin(2))
servo.freq(50)
# Externí tlačítko na GP3 s interním pull-up rezistorem
button = Pin(3, Pin.IN, Pin.PULL_UP)
# Výchozí úhel serva
angle = 0
pressed = False  # Stav tlačítka (abychom předešli falešným stiskům)
def set_angle(angle):
   duty = int(5000 + (angle / 360) * 5000)  # Přepočet úhlu na PWM hodnotu
   servo.duty_u16(duty)
   print(f"Servo otočeno na {angle}°")
# Hlavní smyčka
while True:
   if button.value() == 0 and not pressed:  # Tlačítko je stisknuté (LOW) a předtím nebylo
       angle = 180 if angle == 0 else 0  # Přepnutí mezi 0° a 180°
       set_angle(angle)
       pressed = True  # Uložíme, že tlačítko bylo stisknuté
       sleep(0.1)  # Debounce
   elif button.value() == 1:  # Tlačítko uvolněno (HIGH)
       pressed = False  # Resetujeme stav, aby šlo znovu stisknout

a...

from machine import Pin, PWM, I2C
from time import sleep
from pico_i2c_lcd import I2cLcd  # Tuto knihovnu si musíš stáhnout
# Nastavení I2C pro LCD
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
lcd = I2cLcd(i2c, 0x27, 2, 16)  # Adresu I2C můžeš změnit na 0x3F podle tvého displeje
# Nastavení servomotoru
servo = PWM(Pin(2))
servo.freq(50)
def set_angle(angle):
   duty = int(5000 + (angle / 180) * 5000)  # Přepočet úhlu na PWM
   servo.duty_u16(duty)
   lcd.clear()
   lcd.putstr(f"Angle: {angle} deg")
   sleep(0.5)
# Hlavní cyklus
while True:
   for angle in range(0, 181, 10):
       set_angle(angle)
   for angle in range(180, -1, -10):
       set_angle(angle)

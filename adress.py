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
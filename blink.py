from gpiozero import LED, PWMLED
from time import sleep

red = PWMLED(21)

# while True:
#     red.on()
#     sleep(1)
#     red.off()
#     sleep(1)

red.pulse(fade_in_time=1, fade_out_time=1)
sleep(100)
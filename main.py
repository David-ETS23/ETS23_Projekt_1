from machine import Pin, SoftI2C
import time
import CCS811
import neopixel

#######################################
Co2_i2c = SoftI2C(scl=Pin(5), sda=Pin(4))

Co2_Sensor = CCS811.CCS811(i2c=i2c, addr=90)		

led_ring = neopixel.NeoPixel(Pin(6), 12)

zeit_alt = time.ticks_ms()

#######################################

def Co2_Sensor_abfrage():
      
    if Co2_Sensor.data_ready():
        return(Co2_Sensor.eCO2)
            
#######################################

while True:
    zeit_neu = time.ticks_ms()
    if(time.ticks_diff(zeit_neu, zeit_alt) > 1000):
        zeit_alt = zeit_neu

    Co2_gehalt = Co2_Sensor_abfrage()
    
    if Co2_gehalt <= 1000
    
    led_ring[0] = (0, 255, 0)
    led_ring[1] = (0, 255, 0)
    led_ring[2] = (0, 255, 0)
    led_ring[3] = (0, 255, 0)
    led_ring[4] = (0, 255, 0)
    led_ring[5] = (0, 255, 0)
    led_ring[6] = (0, 255, 0)
    led_ring[7] = (0, 255, 0)
    led_ring[8] = (0, 255, 0)
    led_ring[9] = (0, 255, 0)
    led_ring[10] = (0, 255, 0)
    led_ring[11] = (0, 255, 0)
    led_ring[12] = (0, 255, 0)
    
    if Co2_gehalt > 1000 and < 2000
    
    led_ring[0] = (255, 255, 0)
    led_ring[1] = (255, 255, 0)
    led_ring[2] = (255, 255, 0)
    led_ring[3] = (255, 255, 0)
    led_ring[4] = (255, 255, 0)
    led_ring[5] = (255, 255, 0)
    led_ring[6] = (255, 255, 0)
    led_ring[7] = (255, 255, 0)
    led_ring[8] = (255, 255, 0)
    led_ring[9] = (255, 255, 0)
    led_ring[10] = (255, 255, 0)
    led_ring[11] = (255, 255, 0)
    led_ring[12] = (255, 255, 0)
    
    if Co2_gehalt >= 2000
    
    led_ring[0] = (255, 0, 0)
    led_ring[1] = (255, 0, 0)
    led_ring[2] = (255, 0, 0)
    led_ring[3] = (255, 0, 0)
    led_ring[4] = (255, 0, 0)
    led_ring[5] = (255, 0, 0)
    led_ring[6] = (255, 0, 0)
    led_ring[7] = (255, 0, 0)
    led_ring[8] = (255, 0, 0)
    led_ring[9] = (255, 0, 0)
    led_ring[10] = (255, 0, 0)
    led_ring[11] = (255, 0, 0)
    led_ring[12] = (255, 0, 0)
        
    led_ring.write()

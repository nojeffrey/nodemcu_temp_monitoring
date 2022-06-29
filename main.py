import machine, onewire, ds18x20, time, network, urequests

location = 'ensuite'

ds_pin = machine.Pin(4) #D2 on the NodeMCU
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

# These NodeMCU can act as an AP, disable it:
ap_if = network.WLAN(network.AP_IF)
if ap_if.active():
  ap_if.active(False)

# Connect to WiFi
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('your_ssid', 'your_password')
while not sta_if.isconnected():
  time.sleep(1)

roms = ds_sensor.scan()

#192.168.1.111 is my influxdb server with no authentication configured.
#It will create the measurement `ensuite` automatically.

while True:
  try:
    ds_sensor.convert_temp()
    time.sleep_ms(750)
    for rom in roms:
      data = "{} temp={:.1f}".format(location ,ds_sensor.read_temp(rom))
      urequests.post("http://192.168.1.111:8086/write?db=temps", data=data) 
      time.sleep(60)

  except:
      time.sleep(60)
      continue

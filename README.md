# Nodemcu/ESP8266 temperature monitoring
Micropython code for a Nodemcu/ESP8266 with a DS18B20 temp sensor to post to a InfluxDB server

Follow the wiring diagram here: https://i0.wp.com/randomnerdtutorials.com/wp-content/uploads/2019/06/ds18b20_esp32_single_normal.png?w=750&quality=100&strip=all&ssl=1
Download latest Micropython firmware from https://micropython.org/download
Flash Micropython on to the board:
```
sudo pip install esptool
sudo esptool.py --port /dev/ttyUSB0 erase_flash
sudo esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 esp8266-1m-20220117-v1.18.bin
```
Need to install `urequests`:
```
sudo picocom /dev/ttyUSB0 -b115200
>>> import upip, network
>>> sta_if = network.WLAN(network.STA_IF)
>>> sta_if.active(True)
>>> sta_if.connect(your_ssid', 'your_wireless_password')
>>> upip.install('micropython-urequests')
>>> C-a C-x #to exit
```

Push main.py to flash:
`sudo ampy --port /dev/ttyUSB0 put main.py`


To query from influx:
```
$ influx
> use temps
select * from ensuite
name: ensuite
time                temp
----                ----
1655450392511971840 19.3
1655450453685148747 18.8
1655450514784784107 18.4
1655450575860063626 18.1
...
```

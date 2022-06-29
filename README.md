### Nodemcu/ESP8266 temperature monitoring
Micropython code for a Nodemcu/ESP8266 with a DS18B20 temp sensor to post to a InfluxDB server

Follow the wiring diagram [here:](https://randomnerdtutorials.com/micropython-ds18b20-esp32-esp8266/)

<img src="https://i0.wp.com/randomnerdtutorials.com/wp-content/uploads/2019/06/ds18b20_esp8266_single_normal_F.png?w=559&quality=100&strip=all&ssl=1" width="599" height="763">

Download latest Micropython firmware from https://micropython.org/download

Flash Micropython to the board:
```
sudo pip install esptool ampy
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
```
sudo ampy --port /dev/ttyUSB0 put main.py
```


Need to create the DB `temps` on influxdb server
```
pi@pizero:~ $ influx
Connected to http://localhost:8086 version 1.6.7~rc0
InfluxDB shell version: 1.6.7~rc0
> create database temps
```
Now power up the ESP8266 board somewhere within range and it should post the temp once every 60 seconds to influxdb over wifi.

```
pi@pizero:~ $ influx
Connected to http://localhost:8086 version 1.6.7~rc0
InfluxDB shell version: 1.6.7~rc0
> use temps
Using database temps
> select * from ensuite
name: ensuite
time                temp
----                ----
1655450392511971840 19.3
1655450453685148747 18.8
1655450514784784107 18.4
1655450575860063626 18.1
...
```

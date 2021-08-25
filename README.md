# Filament Environment Sensor
## Based on RP2040 & MicroPython

Currently, this repo supports a simple sensor and display electronic capable of displaying temperature and humidity on a small display, either a 16x02 LCD or 128x64 OLED.

LCD script is trash right now, I need to restore my working copy from another machine in use.





Attribution:
https://github.com/makerportal/rpi-pico-ssd1306
./micropython/data_display/ssd1306.py for the 128x64 OLED driver module
./micropython/data_display/main.py for some elements

https://github.com/tusabez/Pico-Weather-Station
./Weather\ Station\ Using\ DHT11\ and\ Raspberry\ Pi\ Pico/* for DHT11/DHT22 module, 1602/2004 LCD driver, example wiring schematic, and basis of main scripts.
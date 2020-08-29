# PiTrain LED Server
# Copyright(C) 2020 Johan Thelin
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from gpiozero import LED
import time

leds = []

leds.append(LED("GPIO2"))
leds.append(LED("GPIO3"))
leds.append(LED("GPIO4"))
leds.append(LED("GPIO15"))
leds.append(LED("GPIO21"))
leds.append(LED("GPIO20"))
leds.append(LED("GPIO16"))
leds.append(LED("GPIO12"))
leds.append(LED("GPIO26"))
leds.append(LED("GPIO19"))
leds.append(LED("GPIO13"))
leds.append(LED("GPIO6"))
leds.append(LED("GPIO5"))

def all_on():
  for l in leds:
    l.on()
    
def all_off():
  for l in leds:
    l.off()

def house_on():
  leds[0].on()
  leds[1].on()
  leds[4].on()
  leds[7].on()
  
def house_off():
  leds[0].off()
  leds[1].off()
  leds[4].off()
  leds[7].off()

def start_sequence():
  order = [6, 9, 12, 10, 8, 5, 2, 3, 11]
  for interval in [0.4, 0.2, 0.1, 0.05]:
    all_off()
    for i in order:
      leds[i].on()
      time.sleep(interval)
  all_on()
  for x in range(5):
    time.sleep(0.2)
    all_off()
    time.sleep(0.2)
    all_on()
